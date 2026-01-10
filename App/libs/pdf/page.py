from dataclasses import dataclass

@dataclass(frozen=True)
class PageSize:
    width_mm: float
    height_mm: float

PAGE_SIZES = {
    "A5": PageSize(148, 210),
    "A4": PageSize(210, 297),
    "A3": PageSize(297, 420),
    'A2': PageSize(420.0, 594.0),
    'A1': PageSize(594.0, 841.0),
    'A0': PageSize(841.0, 1189.0),
}
