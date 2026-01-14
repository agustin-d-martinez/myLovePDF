import yt_dlp
from pathlib import Path
import re
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
        "extract_flat": "in_playlist",
        "noplaylist": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(url, download=False)

def normalize_videos(info: dict) -> list[dict]:
    """
    Devuelve una lista de videos, independientemente
    de si la URL es video único o playlist.
    """
    if info.get("_type") == "playlist":
        return [v for v in info["entries"] if v]
    return [info]

def get_estimated_size(video: dict) -> str:
    size = (
        video.get("filesize")
        or video.get("filesize_approx")
    )

    if not size:
        return "—"

    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024

    return f"{size:.1f} TB"

def format_duration(seconds: int | None) -> str:
    if not seconds:
        return "--:--"

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    if h:
        return f"{h:d}:{m:02d}:{s:02d}"
    return f"{m:d}:{s:02d}"

_YT_ID_RE = re.compile(r"(?:v=|\/)([0-9A-Za-z_-]{11})")
def get_thumbnail_url(video: dict) -> str | None:
    # 1. Caso ideal
    video_id = video.get("id")

    # 2. Playlist (extract_flat)
    if not video_id:
        url = video.get("url", "")
        match = _YT_ID_RE.search(url)
        if match:
            video_id = match.group(1)

    if not video_id:
        return None

    return f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"

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

def get_thumbnail_url(video_url: str) -> str | None:
    """
    Devuelve la URL del thumbnail de un video.
    Hace una extracción mínima (sin descargar contenido).
    """
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "noplaylist": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
    except Exception:
        return None

    return info.get("thumbnail")


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

    if resolution:
        fmt = (
            f"bv*[vcodec^=avc1][height<={resolution}]/"
            f"bv*[height<={resolution}]/"
            "best"
        )
    else:
        fmt = "bv*[vcodec^=avc1]/bv*/best"


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


