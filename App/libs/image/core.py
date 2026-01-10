from PIL import Image
from pathlib import Path
from typing import Tuple

def change_img_ext(image: str | Path, extension: str):
    """
    Change the extension of an image file.
    
    :param image: Path to image to convert.
    :type image: str | Path
    :param extension: extension to use (including dot, e.g. ".jpg").
    :type extension: str
    """
    image = Path(image)
    if not image.exists():
        raise ValueError("No images provided")
    
    out_file = image.with_suffix(extension)

    img = Image.open(image)
    if img.mode in ("RGBA","P"):
        img = img.convert("RGB")
    img.save(out_file)

def resize_image(image: str | Path, size: Tuple[int, int], output: str | Path | None = None,  scale: bool = True, keep_aspect: bool = True ):
    """
    Resize an image.

    :param image: Path to the image.
    :param size: (width, height).
    :param scale: Whether to resize or not.
    :param keep_aspect: Keep aspect ratio if True.
    :param output: Output path (if None, overwrites).
    """
    image = Path(image)
    if not image.exists():
        raise ValueError("Image does not exist")

    if not scale:
        return image

    output = Path(output) if output else image

    with Image.open(image) as img:
        if keep_aspect:
            img.thumbnail(size, Image.Resampling.LANCZOS)
        else:
            img = img.resize(size, Image.Resampling.LANCZOS)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.save(output)

    return output

def get_image_size(image: str | Path) -> Tuple[int, int]:
    """
    Get image dimensions.

    :param image: Path to the image.
    :return: (width, height)
    """
    image = Path(image)
    if not image.exists():
        raise ValueError("Image does not exist")

    with Image.open(image) as img:
        return img.size
