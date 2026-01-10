from libs.pdf.page import PageSize

PT_PER_INCH = 72.0
MM_PER_INCH = 25.4

# -------------------------------
## Funciones internas
# -------------------------------
def mm_to_points(value: float) -> float:
    """
    Convierte una medida a puntos PDF.

    Parámetros:
      value (float): valor numérico

    Retorna:
      float: valor en puntos
    """
    return value * PT_PER_INCH / MM_PER_INCH
def page_size_to_points(size: PageSize) -> tuple[float, float]:
    return (
        mm_to_points(size.width_mm),
        mm_to_points(size.height_mm),
    )
