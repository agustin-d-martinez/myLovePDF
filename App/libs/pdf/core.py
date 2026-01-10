import fitz                     # pymupdf
from typing import Iterable
from pathlib import Path
import shutil

from .page import PageSize, PAGE_SIZES
from .policies import EvenPolicy
from libs.utils.units import mm_to_points
from libs.file.core import check_directory

def add_blank_page(	pdf: str | Path, output_pdf: str | Path, blank_pages: Iterable[int], default_size: PageSize = PAGE_SIZES["A4"], *, inplace: bool = False ):
    """
    Adds a blank page at specified position in a PDF.
    
    :param pdf: Path to PDF to modify
    :type pdf: str | Path
    :param output_pdf: Path to output PDF
    :type output_pdf: str | Path
    :param blank_pages: positions (1-based) to insert blank pages
    :type blank_pages: Iterable[int]
    :param default_size: Default page size. If the PDF has no pages, this size will be used.
    :type default_size: PageSize
    :param inplace: Defines if the normalized PDF replace the original or not. False by default, it creates a copy.
    :type inplace: bool 
    """
    pdf = Path(pdf)
    if not inplace:
        output_pdf = Path(output_pdf)
        check_directory(output_pdf.parent)

    if not pdf.exists():
        raise ValueError("No pdf provided")

    with fitz.open(pdf) as doc:
        if len(doc) > 0:
            page_width = doc[0].rect.width
            page_height = doc[0].rect.height
        else:
            page_width = mm_to_points(default_size.width_mm)
            page_height = mm_to_points(default_size.height_mm)

        offset = 0
        for pos in sorted(blank_pages):
            index = pos - 1 + offset
            doc.insert_page(index, width=page_width, height=page_height)
            offset += 1

        if inplace:
            doc.saveIncr()
        else:
            doc.save(output_pdf)

def _scale_image_to_page(img_w: float, img_h: float, page_w: float, page_h: float ) -> tuple[float, float]:
    scale = min(page_w / img_w, page_h / img_h)
    return img_w * scale, img_h * scale

def img_to_pdf(image: str | Path, output_pdf: str | Path, size: PageSize = PAGE_SIZES["A4"] ) :
    """
    Convert a Image File to a PDF.
    
    :param images: Path to images to convert.
    :type images: Iterable[str | Path]
    :param output_pdf: Path to output PDF.
    :type output_pdf: str | Path
    :param size: Size of the output PDF.
    :type size: PageSize
    """
    image = Path(image)
    if not image.exists():
        raise ValueError("No images provided")

    output_pdf = Path(output_pdf)
    check_directory(output_pdf.parent)

    page_w = mm_to_points(size.width_mm)
    page_h = mm_to_points(size.height_mm)

    with fitz.open() as doc:
        img = fitz.Pixmap(image)
        new_w, new_h = _scale_image_to_page(img.width, img.height, page_w, page_h)

        page = doc.new_page(width=page_w, height=page_h)

        x0 = (page_w - new_w) / 2
        y0 = (page_h - new_h) / 2
        rect = fitz.Rect(x0, y0, x0 + new_w, y0 + new_h)

        page.insert_image(rect, filename=str(image))
        img = None

        doc.save(output_pdf)

def pdf_to_img(pdf: str | Path, output_dir: str | Path ) :
    """
    Convert a PDF to a Image File.
    
    :param pdfs: Path to PDF to convert.
    :type pdfs: str | Path
    :param output_dir: Path to output image dir.
    :type output_dir: str | Path
    """
    output_dir = check_directory(output_dir)

    pdf = Path(pdf)
    if not pdf.exists():
        raise ValueError("No pdf provided")

    subdir = output_dir / pdf.stem
    subdir.mkdir(parents=True, exist_ok=True)

    with fitz.open(pdf) as doc:
        for i, page in enumerate(doc, start=1):
            pix = page.get_pixmap()
            pix.save(subdir / f"{pdf.stem}_{i:03}.png")
            pix = None

def split_pdf(pdf: str | Path, output_pdf: str | Path, pages: Iterable[int], conservar: bool = False):
    """
    Split a PDF into two PDFs. One with the selected pages. The other is optional and contains the rest of the pages.
    
    :param pdf: Path to PDF to split
    :type pdf: str | Path
    :param output_pdf: Path to output PDF
    :type output_pdf: str | Path
    :param pages: pages to extract (1-based)
    :type pages: list
    :param conservar: Description
    :type conservar: bool
    """
    pdf = Path(pdf)
    output_pdf = Path(output_pdf)
    check_directory(output_pdf.parent)

    if not pdf.exists():
        raise ValueError("No pdf provided")

    doc_initial = fitz.open(pdf)
    doc_splitted = fitz.open()
    doc_splitted_extra = fitz.open()

    out_file_extra = output_pdf.with_stem(output_pdf.stem + "_extra") 
    for num_pagina in range(len(doc_initial)):
        if num_pagina + 1 in pages:
            doc_splitted.insert_pdf(doc_initial, from_page=num_pagina, to_page=num_pagina)
        elif conservar :
            doc_splitted_extra.insert_pdf(doc_initial, from_page=num_pagina, to_page=num_pagina)

    if len(doc_splitted) > 0:
        doc_splitted.save(output_pdf)

    if len(doc_splitted_extra) > 0:
        doc_splitted_extra.save(out_file_extra)
    doc_initial.close()
    doc_splitted.close()
    doc_splitted_extra.close()

def split_pages(pdf: str | Path, output_dir: str | Path, pages: Iterable[int] | None = None):
    """Separa hojas específicas de un PDF y las guarda individualmente en la carpeta de salida.

    Parámetros:
    entrada (str): Ruta del archivo PDF de entrada.
    salida (str): Carpeta donde se guardarán los archivos.
    paginas (list): Lista de números de páginas a extraer (base 1).
    """
    pdf = Path(pdf)
    if not pdf.exists():
        raise ValueError("No pdf provided")

    output_dir = check_directory(output_dir)
        
    with fitz.open(pdf) as doc:
        total_pags = len(doc)
        base_name = pdf.stem

        # Si no se especifican páginas, extraemos todas
        if pages is None:
            pages = list(range(1, total_pags + 1))

        for num_pagina in pages:
            if 1 <= num_pagina <= total_pags:
                # Crear un nuevo documento para la página
                with fitz.open() as doc_tmp:
                    doc_tmp.insert_pdf(doc, from_page=num_pagina - 1, to_page=num_pagina - 1)
                    out_file = output_dir / f"{base_name}_pag_{num_pagina}.pdf"
                    doc_tmp.save(out_file)

def join_pdf(pdfs: Iterable[str | Path], output_pdf: str | Path):
    """
    Join two or more PDFs into a single PDF.
    
    :param pdfs: Path to PDF to join.
    :type pdfs: Iterable[str | Path]
    :param output_pdf: Path to output PDF.
    :type output_pdf: str | Path
    """
    output_pdf = Path(output_pdf)
    check_directory(output_pdf.parent)

    doc_final = fitz.open()
    for pdf in pdfs:
        pdf = Path(pdf)
        if not pdf.exists():
            continue

        with fitz.open(pdf) as temp:
            doc_final.insert_pdf(temp)
                
    if len(doc_final) == 0:
        doc_final.close()
        raise ValueError("No pdfs provided")

    doc_final.save(output_pdf)
    doc_final.close()

def evenize_pdf(pdf: str | Path, output_pdf: str | Path | None = None,  policy: EvenPolicy = EvenPolicy.PAD_START, inplace = False):
    """
    Transforms a pdf into a even format. It has 2 policies: Padding in the start or in the end
    
    :param pdf: Path pdf to make even.
    :type pdf: str | Path
    :param output_pdf: Path to output pdf.
    :type output_pdf: str | Path
    :param policy: policy for padding of even files.
    :type policy: EvenPolicy
    :param inplace: Defines if the normalized PDF replace the original or not. False by default, it creates a copy.
    :type inplace: bool 

    """
    pdf = Path(pdf)

    if inplace:
        tmp_pdf = pdf.with_suffix(".tmp.pdf")
        output_path = tmp_pdf
    else:
        output_path = Path(output_pdf)
        check_directory(output_path.parent)

    with fitz.open(pdf) as doc:
        if len(doc) % 2 == 0:
            if not inplace:
                doc.save(output_path)
            return

        new_doc = fitz.open()

        if policy == EvenPolicy.PAD_START:
            new_doc.new_page()

        new_doc.insert_pdf(doc)

        if policy == EvenPolicy.PAD_END:
            new_doc.new_page()

        new_doc.save(output_path)

    if inplace:
        shutil.move(tmp_pdf, pdf)
    
def normalize_pdfs(pdfs: Iterable[str | Path], output_dir: str | Path,  policy: EvenPolicy = EvenPolicy.PAD_START, inplace: bool = False):
    """
    Transforms a list pdf into a even format and saves it in output_dir. It has 2 policies: Padding in the start or in the end
    
    :param pdfs: Description
    :type pdfs: Iterable[str | Path]
    :param output_dir: Description
    :type output_dir: str | Path
    :param policy: Description
    :type policy: EvenPolicy
    :param inplace: Defines if the normalized PDF replace the original or not. False by default, it creates a copy
    :type inplace: bool 
    """
    if not inplace:
        output_dir = check_directory(output_dir)

    for pdf in pdfs:
        pdf = Path(pdf)
        if not pdf.exists():
            continue

        if policy == EvenPolicy.NONE:
            continue

        out = output_dir / f"{pdf.stem}_even.pdf" if not inplace else None

        pad = "start" if policy == EvenPolicy.PAD_START else "end"
        evenize_pdf(pdf, out, pad=pad, inplace=inplace)

def pdf_info(pdf: str | Path) -> dict:
    """
    Returns basic information about a PDF.
    """
    pdf = Path(pdf)
    if not pdf.exists():
        raise FileNotFoundError(pdf)

    with fitz.open(pdf) as doc:
        first_page = doc[0]
       
        width = first_page.rect.width
        height = first_page.rect.height

        return {
            "path": pdf,
            "pages": len(doc),
            "page_size": (width, height),
            "metadata": doc.metadata,
        }

def rotate_pages(pdf: str | Path, output_pdf: str | Path, pages: Iterable[int], angle: int) -> Path:
    """
    Rotate selected pages of a PDF.
    Pages are zero-based.
    Angle must be multiple of 90.
    """
    if angle % 90 != 0:
        raise ValueError("Angle must be multiple of 90")

    pdf = Path(pdf)
    output_pdf = Path(output_pdf)
    check_directory(output_pdf.parent)

    with fitz.open(pdf) as doc:
        for page_number in pages:
            if 0 <= page_number < len(doc):
                page = doc[page_number]
                page.set_rotation((page.rotation + angle) % 360)

        doc.save(output_pdf)

    return output_pdf
