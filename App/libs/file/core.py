from typing import Iterable
from pathlib import Path

def check_directory(dir: str | Path, *, exist_ok: bool = True) -> Path:
    dir = Path(dir)
    if dir.exists() and not dir.is_dir():
        raise NotADirectoryError(dir)
    dir.mkdir(parents=True, exist_ok=exist_ok)

    return dir

def search_file_tipe(origin_path: str | Path, ext: str, *, recursive: bool = False):
    origin_path = check_directory(origin_path)

    pattern = f"**/*{ext}" if recursive else f"*{ext}"

    return [
        str(path.relative_to(origin_path))
        for path in origin_path.glob(pattern)
        if path.is_file()
    ]


def delete_files(paths: Iterable[str | Path], *, missing_ok: bool = True, dry_run: bool = False) -> list[Path]:
    """
    Deletes files. Returns list of deleted files.
    """
    deleted: list[Path] = []

    for p in paths:
        p = Path(p)

        if not p.exists():
            if missing_ok:
                continue
            raise FileNotFoundError(p)

        if not p.is_file():
            continue

        if dry_run:
            deleted.append(p)
            continue

        p.unlink()
        deleted.append(p)

    return deleted


def rename_files( files: Iterable[str | Path], template: str, start: int = 1) :
    """
    Rename a list of files using a template with numbering.
     
    :param files: Path to files to rename
    :type files: Iterable[str | Path]
    :param template: string with the template formateting. 
    Use "XXX" as a placeholder for the number. If not "XXX" is found, the number is appended at the end.
    :type template: str
    :param start: First value for numbering
    :type start: int
    :return: Description
    :rtype: bool
    """
    for i, file in enumerate(files, start=start):
        file = Path(file)
        if not file.exists():
            continue

        number = str(i)
        name = template.replace("XXX", number) if "XXX" in template else template + number
        new_file = file.with_name(name + file.suffix)

        try:
            file.rename(new_file)
        except Exception:
            continue
