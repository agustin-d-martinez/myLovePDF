def _codec_to_ffmpeg(codec: str) -> str:
    match codec.lower():
        case "mp3":
            return "libmp3lame"
        case "aac":
            return "aac"
        case "ogg" | "vorbis":
            return "libvorbis"
        case _:
            raise ValueError(f"Unsupported audio codec: {codec}")
