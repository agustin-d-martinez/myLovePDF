import yt_dlp
from pathlib import Path
from libs.file.core import check_directory

def get_video_info(url: str) -> dict:
    """
    Extrae toda la metadata disponible de una URL usando yt-dlp.
    No descarga contenido.
    Retorna el dict crudo de yt-dlp.
    """
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return info

def normalize_videos(info: dict) -> list[dict]:
    """
    Devuelve una lista de videos, independientemente
    de si la URL es video único o playlist.
    """
    if info.get("_type") == "playlist":
        return [v for v in info["entries"] if v]
    return [info]

VALID = {144, 240, 360, 480, 720, 1080, 1440, 2160}
def get_resolutions(video_info: dict) -> list[int]:
    formats = video_info.get("formats")
    if not formats:
        return []

    resolutions = {
        f["height"]
        for f in formats
        if f.get("vcodec") not in (None, "none")
        and isinstance(f.get("height"), int)
        and f["height"] in VALID
    }

    return sorted(resolutions)

def summarize_formats(video_info: dict) -> list[dict]:
    """
    Devuelve info resumida de todos los formatos de video.
    """
    formatos = []

    for f in video_info.get("formats", []):
        if f.get("vcodec") in (None, "none"):
            continue

        formatos.append({
            "format_id": f["format_id"],
            "ext": f.get("ext"),
            "height": f.get("height"),
            "fps": f.get("fps"),
            "vcodec": f.get("vcodec"),
            "acodec": f.get("acodec"),
            "filesize": f.get("filesize") or f.get("filesize_approx"),
        })

    return formatos

def download_video(url: str, output_path: str | Path, resolution: int | None = None, with_thumbnail: bool = False, progress_hook = None) -> None:
    """
    Descarga un video compatible universal (H.264 + audio).
    """
    output_path = Path(output_path)
    check_directory(output_path.parent)
    
    output_dir = output_path.parent          
    filename = output_path.stem or "%(title)s"             

    fmt = "bv*[vcodec^=avc1]"
    if resolution:
        fmt += f"[height<={resolution}]"
    fmt += "+ba"

    video_options = {
        "format": fmt,
        "merge_output_format": "mp4",
        "outtmpl": f"{filename}.%(ext)s",
        "paths": {"home": str(output_dir)},
        "progress_hooks": [progress_hook],
    }

    if with_thumbnail:
        video_options.update({
            "writethumbnail": True,
            "postprocessors": [
                {"key": "EmbedThumbnail"},
                {"key": "FFmpegMetadata"},
            ],
        })

    with yt_dlp.YoutubeDL(video_options) as ydl:
        ydl.download([url])

def _progress_bar(d):
    if d["status"] == "downloading":
        print(d["_percent_str"], d["_speed_str"])
    elif d["status"] == "finished":
        print("Descarga terminada")


