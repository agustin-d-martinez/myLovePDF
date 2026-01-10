from mutagen.id3 import APIC, ID3, TIT2, TPE1, TCOM, TPE2, TRCK, USLT, TCON, TDRC, TALB, TMOO
from typing import TypedDict, Optional
import mimetypes


class MusicTags(TypedDict):
    title: str
    artist: str
    album: str
    composer: str
    album_artist: str
    genre: str
    track: str
    year: str
    mood: str
    lyrics: str
    cover: bytes

def get_music_tags(file: str) -> MusicTags:
    """
    Devuelve un diccionario con los metadatos básicos de un archivo MP3.
    Se intentan obtener: título, artista, álbum, compositor, artista del álbum,
    género, track (número/total), letra, año y portada.
    
    Si un tag no está presente, su valor será None. Para la portada, se devuelve
    un diccionario con 'mime', 'desc' y 'size' o None si no existe.
    """
    try:
        audio = ID3(file)
    except Exception as e:
        raise ValueError(f"No se pudo leer el archivo MP3: {file}") from e
    tags_frames = {
        "title": "TIT2",
        "artist": "TPE1",
        "album": "TALB",
        "composer": "TCOM",
        "album_artist": "TPE2",
        "genre": "TCON",
        "track": "TRCK",
        "year": "TDRC",
        "mood": "TMOO"
    }
    tags = {}
    for key, frame_id in tags_frames.items():
        frame = audio.get(frame_id)
        if frame:
            try:
                if key == "year":
                    tags[key] = str(frame.text[0])
                else:
                    tags[key] = frame.text[0] if isinstance(frame.text, list) else frame.text
            except Exception:
                tags[key] = str(frame)
        else:
            tags[key] = None

    apic_frame = audio.getall("USLT")
    if apic_frame:
        tags["lyrics"] = apic_frame[0].text	# Se toma el primero
    else:
        tags["lyrics"] = None

    apic_frame = audio.get("APIC:")			# Procesar portada (APIC)
    if apic_frame:
        tags["cover"] = {
            "mime": apic_frame.mime,
            "desc": apic_frame.desc,
            "data": apic_frame.data,
        }
    else:
        tags["cover"] = None

    return tags

def set_music_tags(file: str, tags: dict) :
    """
    Actualiza o agrega metadatos en un archivo MP3.
    
    Parámetros:
    archivo (str): Ruta del archivo MP3.
    tags (dict): Diccionario con las siguientes claves (valores de ejemplo):
        'title': "Mi Canción"
        'artist': "Mi Artista"
        'album': "Mi Álbum"
        'composer': "Mi Compositor"
        'album_artist': "Artista del Álbum"
        'genre': "Pop"
        'track': "1/10"  (puede ser string o número/total)
        'lyrics': "Letra completa..."
        'year': "2021"
        'mood': "triste"
        'cover': "cover.jpg"
        
    Se eliminan los frames existentes para evitar duplicados y se agrega la portada
    usando el frame APIC si se especifica.
    """
    try:
        audio = ID3(file)
    except Exception as e:
        raise ValueError(f"No se pudo abrir el archivo MP3: {file}") from e
    
    # Eliminar frames existentes para evitar duplicados
    for frame in ["TIT2", "TPE1", "TALB", "TCOM", "TPE2", "TCON", "TRCK", "USLT", "TDRC", "APIC","TMOO"]:
        audio.delall(frame)

    if "title" in tags and tags["title"]:
        audio.add(TIT2(encoding=3, text=tags["title"]))
    if "artist" in tags and tags["artist"]:
        audio.add(TPE1(encoding=3, text=tags["artist"]))
    if "album" in tags and tags["album"]:
        audio.add(TALB(encoding=3, text=tags["album"]))
    if "composer" in tags and tags["composer"]:
        audio.add(TCOM(encoding=3, text=tags["composer"]))
    if "album_artist" in tags and tags["album_artist"]:
        audio.add(TPE2(encoding=3, text=tags["album_artist"]))
    if "genre" in tags and tags["genre"]:
        audio.add(TCON(encoding=3, text=tags["genre"]))
    if "track" in tags and tags["track"]:
        audio.add(TRCK(encoding=3, text=tags["track"]))
    if "lyrics" in tags and tags["lyrics"]:
        audio.add(USLT(encoding=3, lang="XXX", desc="", text=tags["lyrics"]))
    if "year" in tags and tags["year"]:
        audio.add(TDRC(encoding=3, text=str(tags["year"])))
    if "mood" in tags and tags["mood"]:
        audio.add(TMOO(encoding=3, text=str(tags["mood"])))
    if "cover" in tags and tags["cover"]:		# Procesar portada: si 'cover' existe en tags, se asume bytes de PNG.
        mime, _ = mimetypes.guess_type("cover.png")
        audio.add(APIC(encoding=3,mime=mime,type=3, desc="",data=tags["cover"]))	
    audio.save(file)
