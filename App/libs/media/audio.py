import yt_dlp
from pathlib import Path
import subprocess

from .ffmpeg import _codec_to_ffmpeg
from libs.file.core import check_directory

def download_audio(url: str, output_path: str | Path, quality: str = "192", codec: str = "mp3", progress_hook = None) -> None:
    """
    Descarga solo audio y lo convierte al codec deseado.
    """
    output_path = Path(output_path)
    check_directory(output_path.parent)
    
    output_dir = output_path.parent          
    filename = output_path.stem or "%(title)s"             

    audio_options = {
        "format": "ba",
        "outtmpl": f"{filename}.%(ext)s",
        "paths": {"home": str(output_dir)},
        "progress_hooks": [progress_hook],
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": codec,
            "preferredquality": quality,
        }],
    }

    with yt_dlp.YoutubeDL(audio_options) as ydl:
        ydl.download([url])

def extract_audio(video: str | Path, output_audio: str | Path, codec: str = "mp3", quality: str = "2") -> None:
    """
    Extrae el audio de un video usando ffmpeg.

    :param video: archivo de entrada (video)
    :type video: str | Path
    :param output_audio: archivo de salida (audio)
    :type output_audio: str | Path
    :param codec: codec de audio (ej: mp3, aac, vorbis)
    :type codec: str
    :param quality: calidad para codecs VBR (ej: 0–9 en mp3)
    :type quality: str
    """
    video = Path(video)
    output_audio = Path(output_audio)

    if not video.exists():
        raise FileNotFoundError(f"Input video not found: {video}")

    output_audio.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ffmpeg",
        "-i", str(video),
        "-vn",
        "-acodec", _codec_to_ffmpeg(codec),
        "-q:a", quality,
        "-y",
        str(output_audio),
    ]

    subprocess.run(cmd, check=True)

