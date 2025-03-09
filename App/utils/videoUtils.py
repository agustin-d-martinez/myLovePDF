from pytubefix import YouTube
import requests
from io import BytesIO
import os
import moviepy.editor as mp

def mp4_a_mp3(mp4, mp3):
	clip = mp.VideoFileClip(mp4)
	clip.audio.write_audiofile(mp3, codec='libmp3lame')
	clip.close()

def unir_audio_video(path_audio, path_video, salida):
	audio = mp.AudioFileClip(path_audio)
	video = mp.VideoFileClip(path_video)
	final = video.set_audio(audio)
	final.write_videofile(salida, codec= 'mpeg4' ,audio_codec='libvorbis')

def descargar_video(url, salida, formato="mp4"):
	yt = YouTube(url, use_oauth=False, allow_oauth_cache=True)
	path, nombre = os.path.split(os.path.splitext(salida)[0])
	
	archivo_final = f"{nombre}.{formato}"
	salida_final = os.path.join(path, archivo_final)

	if formato == "mp3":
		# Descargar el mejor stream de audio
		audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4") \
								  .order_by('abr').desc().first()
		archivo_tmp = f"{nombre}_tmp.mp4"
		ruta_tmp = os.path.join(path, archivo_tmp)
		audio_stream.download(output_path=path, filename=archivo_tmp)
		
		mp4_a_mp3(ruta_tmp, salida_final)			# Convertir a mp3 
		os.remove(ruta_tmp)
	
	elif formato == "mp4": 
		# Intentar obtener un stream adaptativo (video sin audio) de mayor resolución
		stream_progresivo = yt.streams.filter(progressive=True, file_extension="mp4") \
									  .order_by('resolution').desc().first()
		stream_video_only = yt.streams.filter(adaptive=True, only_video=True, file_extension="mp4") \
									  .order_by('resolution').desc().first()
		
		if stream_video_only is not None:
			# Convertir la resolución (p.ej. "1080p") a número
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
				
				unir_audio_video(ruta_aud_tmp,ruta_vid_tmp,salida_final)	# Combinar video y audio 
				os.remove(ruta_vid_tmp)
				os.remove(ruta_aud_tmp)
				return
			
		stream_progresivo.download(output_path=path, filename=archivo_final)	# Si no hay mayor calidad, usar el stream progresivo

#descargar_video_alta_resolucion("https://www.youtube.com/watch?v=oTRJNfjh_iU", "E:\\Agustin\\Downloads\\prueba2.mp3","mp3")

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