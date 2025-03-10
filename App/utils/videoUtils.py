from pytubefix import YouTube
import requests
from io import BytesIO
import os
import moviepy.editor as mp

def mp4_a_mp3(mp4, mp3):
	clip = mp.VideoFileClip(mp4)
	clip.audio.write_audiofile(mp3, codec='libx264')
	clip.close()

def unir_audio_video(path_audio, path_video, salida):
	audio = mp.AudioFileClip(path_audio)
	video = mp.VideoFileClip(path_video)
	final = video.set_audio(audio)
	final.write_videofile(salida, codec= 'libx264' ,audio_codec='aac', preset='veryfast')
	audio.close()
	video.close()

def descargar_audio(url, salida):
	yt = YouTube(url, use_oauth=False, allow_oauth_cache=True)
	path, nombre = os.path.split(os.path.splitext(salida)[0])
	
	archivo_final = f"{nombre}.mp3"
	salida_final = os.path.join(path, archivo_final)

	audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4") \
								  .order_by('abr').desc().first()		# Descargar el mejor stream de audio
	archivo_tmp = f"{nombre}_tmp.mp4"
	ruta_tmp = os.path.join(path, archivo_tmp)
	audio_stream.download(output_path=path, filename=archivo_tmp)
		
	clip = mp.AudioFileClip(ruta_tmp)
	clip.write_audiofile(salida_final, codec='libmp3lame')
	clip.close()
	os.remove(ruta_tmp)

def descargar_video(url, salida):
	yt = YouTube(url, use_oauth=False, allow_oauth_cache=True)
	path, nombre = os.path.split(os.path.splitext(salida)[0])
	
	archivo_final = f"{nombre}.mp4"
	salida_final = os.path.join(path, archivo_final)

	# Filtrar streams que tengan resolución <= 1080p
	progressive_streams = [
		s for s in yt.streams.filter(progressive=True, file_extension="mp4") 
		if s.resolution and int(s.resolution.replace("p", "")) <= 1080
	]
	adaptive_streams = [
		s for s in yt.streams.filter(adaptive=True, only_video=True, file_extension="mp4") 
		if s.resolution and int(s.resolution.replace("p", "")) <= 1080
	]
	
	# Seleccionar el stream de mayor resolución (dentro del límite)
	stream_progresivo = sorted(
		progressive_streams, key=lambda s: int(s.resolution.replace("p", "")), reverse=True
	)[0] if progressive_streams else None
	
	stream_video_only = sorted(
		adaptive_streams, key=lambda s: int(s.resolution.replace("p", "")), reverse=True
	)[0] if adaptive_streams else None

	if stream_video_only is not None:
		# Comparar resoluciones de los streams disponibles
		res_progresiva = int(stream_progresivo.resolution.replace("p", "")) if stream_progresivo else 0
		res_adaptativa = int(stream_video_only.resolution.replace("p", ""))
		
		if res_adaptativa > res_progresiva:
			archivo_vid_tmp = f"{nombre}_vid.mp4"
			archivo_aud_tmp = f"{nombre}_aud.mp4"
			ruta_vid_tmp = os.path.join(path, archivo_vid_tmp)
			ruta_aud_tmp = os.path.join(path, archivo_aud_tmp)
			
			# Descargar video (sin audio) y el mejor audio por separado
			stream_video_only.download(output_path=path, filename=archivo_vid_tmp)
			stream_audio = yt.streams.filter(only_audio=True, file_extension="mp4") \
										.order_by('abr').desc().first()
			stream_audio.download(output_path=path, filename=archivo_aud_tmp)
			
			# Combinar video y audio (se asume que unir_audio_video usa FFmpeg internamente)
			unir_audio_video(ruta_aud_tmp, ruta_vid_tmp, salida_final)
			os.remove(ruta_vid_tmp)
			os.remove(ruta_aud_tmp)
			return
		if stream_progresivo:	# Si no hay opción adaptativa
			stream_progresivo.download(output_path=path, filename=archivo_final)
	

def obtenerTituloPortadaVideo(url):
	yt = YouTube(url, use_oauth=False, allow_oauth_cache=True)
	titulo = yt.title
	miniatura_url = yt.thumbnail_url
	response = requests.get(miniatura_url)
	if response.status_code == 200:
		miniatura = BytesIO(response.content).read()
	else :
		miniatura = b""
	return titulo , miniatura