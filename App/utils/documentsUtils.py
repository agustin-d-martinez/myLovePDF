import fitz  # pymupdf
import os
#from PIL import Image
#import sys

def renombrar(archivos , nombre , numerar = True, inicial = 1 , post_idx = False):
	"""Renombra archivos con un nombre base, opcionalmente numerándolos.

	Parámetros:
	archivos (list): Lista de archivos a renombrar (rutas completas o nombres).
	nombre (str): Nuevo nombre base sin extensión.
	numerar (bool): Si es True, agrega un número al nombre.
	inicial (int): Número inicial si numerar es True.
	post_idx (bool): Si es True, el número se coloca después del nombre y antes de la extensión.
					 Si es False, el número se coloca antes del nombre.
	"""
	for i, archivo in enumerate(archivos, start=inicial):
		if not os.path.exists(archivo):
			print(f"Advertencia: No se encontró '{archivo}', se omitirá.")
			continue
		
		ruta, ext = os.path.splitext(archivo)  # Obtener extensión del archivo
		dir_archivo = os.path.dirname(archivo)  # Directorio del archivo
		
		if numerar:
			if post_idx:
				nuevo_nombre = f"{nombre} #{i}{ext}"
			else:
				nuevo_nombre = f"{i}.{nombre}{ext}"
		else:
			nuevo_nombre = f"{nombre}{ext}"  # Si no se numera, solo usa el nombre base

		nueva_ruta = os.path.join(dir_archivo, nuevo_nombre)

		try:
			os.rename(archivo, nueva_ruta)
			print(f"Renombrado: '{archivo}' → '{nueva_ruta}'")
		except Exception as e:
			print(f"Error al renombrar '{archivo}': {e}")

A4_WIDTH, A4_HEIGHT = 595, 842  


def imagenes_a_pdf(imagenes, salida, scale_widht = A4_WIDTH , scale_height = 842 ):
	"""Convierte una lista de imágenes en un archivo PDF.

	Parámetros:
	imagenes (list): Lista de rutas de imágenes a convertir.
	salida (str): Ruta del archivo PDF de salida.
	"""
	if not imagenes:
		print("Error: La lista de imágenes está vacía.")
		return

	doc = fitz.open()

	for imagen in imagenes:
		if os.path.exists(imagen):
			img_doc = fitz.open()  # Documento temporal
			img_doc.insert_page(0, width=scale_widht, height=scale_height)  # Página A4 en blanco
			rect = img_doc[0].rect  # Rectángulo de la página
			
			# Obtener el tamaño de la imagen
			img = fitz.Pixmap(imagen)
			img_width, img_height = img.width, img.height

			# Escalar la imagen manteniendo la proporción
			scale = min(A4_WIDTH / img_width, A4_HEIGHT / img_height)
			new_width = img_width * scale
			new_height = img_height * scale

			# Centrar la imagen en la página
			x0 = (A4_WIDTH - new_width) / 2
			y0 = (A4_HEIGHT - new_height) / 2
			x1 = x0 + new_width
			y1 = y0 + new_height
			img_rect = fitz.Rect(x0, y0, x1, y1)

			# Insertar la imagen escalada en la página
			img_doc[0].insert_image(img_rect, filename=imagen)
			
			# Agregar la página con la imagen al documento final
			doc.insert_pdf(img_doc)
			img_doc.close()
		else:
			print(f"Advertencia: No se encontró '{imagen}' y será omitida.")

	if len(doc) > 0:
		doc.save(salida)
		print(f"PDF guardado como '{salida}'")
	else:
		print("Error: No se pudo generar el PDF de salida.")

	doc.close()


def separar_pdf(entrada, salida, paginas, conservar= False, salida_extra = None):
	if not os.path.exists(entrada):
		print(f"Error: No se encontró '{entrada}'")
		return

	doc_inicial = fitz.open(entrada)
	doc_salida = fitz.open()
	doc_salida_extra = fitz.open()

	for num_pagina in range(len(doc_inicial)):
		if num_pagina + 1 in paginas:
			doc_salida.insert_pdf(doc_inicial, from_page=num_pagina, to_page=num_pagina)
		elif conservar :
			doc_salida_extra.insert_pdf(doc_inicial, from_page=num_pagina, to_page=num_pagina)

	if len(doc_salida) > 0:
		doc_salida.save(salida)
		print(f"Guardado: {salida}")
	if len(doc_salida_extra) > 0:
		print(f"Guardado: {salida_extra}")

	doc_inicial.close()
	doc_salida.close()
	doc_salida_extra.close()

def separar_hojas(entrada, salida, paginas = None):
	"""Separa hojas específicas de un PDF y las guarda individualmente en la carpeta de salida.

	Parámetros:
	entrada (str): Ruta del archivo PDF de entrada.
	salida (str): Carpeta donde se guardarán los archivos.
	paginas (list): Lista de números de páginas a extraer (base 1).
	"""

	if not os.path.exists(entrada):
		print(f"Error: No se encontró '{entrada}'")
		return

	if not os.path.exists(salida):
		os.makedirs(salida)  # Crea la carpeta si no existe
		
	 # Abrir el documento de entrada
	with fitz.open(entrada) as doc_inicial:
		total_paginas = len(doc_inicial)
		nombre_base = os.path.splitext(os.path.basename(entrada))[0]

		# Si no se especifican páginas, extraemos todas
		if paginas is None:
			paginas = list(range(1, total_paginas + 1))

		for num_pagina in paginas:
			if 1 <= num_pagina <= total_paginas:
				# Crear un nuevo documento para la página
				with fitz.open() as doc_tmp:
					doc_tmp.insert_pdf(doc_inicial, from_page=num_pagina - 1, to_page=num_pagina - 1)
					archivo_salida = os.path.join(salida, f"{nombre_base}_pag_{num_pagina}.pdf")
					doc_tmp.save(archivo_salida)
					print(f"Guardado: {archivo_salida}")
			else:
				print(f"Advertencia: La página {num_pagina} está fuera de rango y será omitida.")

def unir_pdfs(entradas, salida, inicial_par=False , final_par=False):
	
	if not entradas:
		print("Error: La lista de PDFs está vacía.")
		return
	doc_final = fitz.open()

	for pdf in entradas:
		if os.path.exists(pdf):
			doc_temp = fitz.open(pdf)
			if inicial_par and len(doc_temp) % 2 != 0 :
				doc_final.new_page()
	
			doc_final.insert_pdf(doc_temp)

			if final_par and len(doc_temp) % 2 != 0 :
				doc_final.new_page()

			doc_temp.close()
		else:
			print(f"Advertencia: No se encontró '{pdf}' y será omitido.")

	if len(doc_final) > 0:
		doc_final.save(salida)
		print(f"PDF guardado como '{salida}'")
	else:
		print("Error: No se pudo generar el PDF de salida.")
		doc_final.close()
		return

	doc_final.close()

	print(f"PDFs combinados y guardados en '{salida}'")