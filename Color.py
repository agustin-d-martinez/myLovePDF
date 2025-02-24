import fitz  # PyMuPDF
import os

def separar_pdf_manual(pdf_entrada, salida_color, salida_bn, paginas_color):
    """Separa un PDF en color y blanco/negro según una lista de páginas indicadas manualmente."""
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_pdf = os.path.join(carpeta_actual, pdf_entrada)
    ruta_color = os.path.join(carpeta_actual, salida_color)
    ruta_bn = os.path.join(carpeta_actual, salida_bn)

    if not os.path.exists(ruta_pdf):
        print(f"Error: No se encontró '{ruta_pdf}'")
        return

    doc = fitz.open(ruta_pdf)
    doc_color = fitz.open()
    doc_bn = fitz.open()

    for num_pagina in range(len(doc)):
        if num_pagina + 1 in paginas_color:
            doc_color.insert_pdf(doc, from_page=num_pagina, to_page=num_pagina)
        else:
            doc_bn.insert_pdf(doc, from_page=num_pagina, to_page=num_pagina)

    if len(doc_color) > 0:
        doc_color.save(ruta_color)
        print(f"Guardado: {ruta_color}")
    if len(doc_bn) > 0:
        doc_bn.save(ruta_bn)
        print(f"Guardado: {ruta_bn}")

    doc.close()
    doc_color.close()
    doc_bn.close()

# 🔹 USO: Especifica las páginas a color (en base 1)
paginas_a_color = [1,2,3,4,9,10,21,22,23,24,29,30,33,34,35,36,39,40,45,46,47,48,49,50,51,52,53,54
                    ,63,64,65,66,67,68,71,72,105,106,109,110,115,116,119,120,121,122,125,126,127,128,129,130,131,132]  
separar_pdf_manual("resultado.pdf", "color.pdf", "blanco_negro.pdf", paginas_a_color)
