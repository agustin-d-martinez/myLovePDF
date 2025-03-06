import fitz  # pymupdf
import os
from mutagen.id3 import APIC, ID3, TIT2, TPE1, TCOM, TPE2, TRCK, USLT, TCON, TDRC, TALB, ID3TimeStamp

A4_WIDTH, A4_HEIGHT = 595, 842  

import os

def renombrar_template(archivos, template, inicial=1):
	"""
	Renombra los archivos según un template.
	
	Parámetros:
	  archivos (list): Lista de rutas de archivos a renombrar.
	  template (str): Cadena de texto que define el nuevo nombre. Debe incluir "XXX"
					  para indicar dónde se insertará el número. Ejemplo: "trabajo practico N°XXX"
	  inicial (int): Número a partir del cual se numeran los archivos.
	  
	Si el template no contiene "XXX", se añadirá el número al final del nombre.
	Se conserva la extensión original del archivo.
	"""
	for i, archivo in enumerate(archivos, start=inicial):
		if not os.path.exists(archivo):
			print(f"Advertencia: No se encontró '{archivo}', se omitirá.")
			continue
		
		# Obtener la extensión del archivo
		_, ext = os.path.splitext(archivo)
		
		# Si el template contiene "XXX", se reemplaza por el número actual
		if "XXX" in template:
			nuevo_nombre = template.replace("XXX", str(i))
		else:
			nuevo_nombre = template + str(i)
		
		# Se conserva la extensión original
		nuevo_nombre += ext
		
		# Se obtiene el directorio donde se encuentra el archivo original
		dir_archivo = os.path.dirname(archivo)
		nueva_ruta = os.path.join(dir_archivo, nuevo_nombre)
		
		try:
			os.rename(archivo, nueva_ruta)
			print(f"Renombrado: '{archivo}' → '{nueva_ruta}'")
		except Exception as e:
			print(f"Error al renombrar '{archivo}': {e}")

def agregar_hojas_blanco(entrada, salida, paginas):
	"""
	Agrega páginas en blanco a un PDF en las posiciones indicadas.
	
	Parámetros:
	  entrada (str): Ruta del PDF original.
	  salida (str): Ruta del PDF resultante.
	  paginas (list): Lista de posiciones (1-based) donde se insertarán las páginas en blanco.
	"""
	if not os.path.exists(entrada):
		print(f"Error: No se encontró '{entrada}'")
		return

	doc = fitz.open(entrada)
	
	# Obtener dimensiones para la página en blanco: usar la primera página si existe,
	# de lo contrario, se usa tamaño A4 (595 x 842 puntos)
	if len(doc) > 0:
		rect = doc[0].rect
	else:
		rect = fitz.Rect(0, 0, A4_WIDTH, A4_HEIGHT)
	
	# Ordenamos las posiciones para insertar de forma ascendente
	paginas = sorted(paginas)
	
	# offset se utiliza para ajustar la posición al insertar páginas adicionales
	offset = 0
	for pos in paginas:
		# pos es 1-based; convertimos a índice 0-based y sumamos offset
		indice = (pos - 1) + offset
		doc.insert_page(indice, width=rect.width, height=rect.height)
		offset += 1
		print(f"Insertada página en blanco en la posición {indice + 1}")

	doc.save(salida)
	doc.close()
	print(f"PDF modificado guardado como '{salida}'")

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

def unir_pdfs(entradas, salida, archivo_par:int = 0):
	"""Une los PDF de entrada en un único PDF.

	Parámetros:
	entradas (str): Ruta de los archivos PDF de entrada.
	salida (str): Nombre del archivo de salida.
	archivo_par (int): Si es 0, se unen los pdf. 
		Si es 1 se agrega una hoja blanca al inicio para que el archivo sea par.
		Si es 2 se agrega una hoja blanca al final para que el archivo sea par.
	"""
	if not entradas:
		print("Error: La lista de PDFs está vacía.")
		return
	doc_final = fitz.open()

	for pdf in entradas:
		if os.path.exists(pdf):
			doc_temp = fitz.open(pdf)
			if archivo_par == 1 and len(doc_temp) % 2 != 0 :
				doc_final.new_page()
	
			doc_final.insert_pdf(doc_temp)

			if archivo_par == 2 and len(doc_temp) % 2 != 0 :
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

def getMusicTags(archivo) -> dict[str]:
	"""
	Devuelve un diccionario con los metadatos básicos de un archivo MP3.
	Se intentan obtener: título, artista, álbum, compositor, artista del álbum,
	género, track (número/total), letra, año y portada.
	
	Si un tag no está presente, su valor será None. Para la portada, se devuelve
	un diccionario con 'mime', 'desc' y 'size' o None si no existe.
	"""
	try:
		audio = ID3(archivo)
	except Exception as e:
		#print(f"Error al abrir {archivo}: {e}")
		return {}
	tags_frames = {
		"title": "TIT2",
		"artist": "TPE1",
		"album": "TALB",
		"composer": "TCOM",
		"album_artist": "TPE2",
		"genre": "TCON",
		"track": "TRCK",
		"lyrics": "USLT",
		"year": "TDRC"
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
			tags[key] = ""

	# Procesar portada (APIC)
	apic_frame = audio.get("APIC:")
	if apic_frame:
		tags["cover"] = apic_frame.data  # Bytes de la imagen
	else:
		tags["cover"] = ""

	return tags

def setMusicTags(archivo, tags):
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
		 'cover': "cover.jpg"   <-- Ruta de la imagen para la portada
		 
	Se eliminan los frames existentes para evitar duplicados y se agrega la portada
	usando el frame APIC si se especifica.
	"""
	try:
		audio = ID3(archivo)
	except Exception:
		audio = ID3()

	# Eliminar frames existentes para evitar duplicados
	for frame in ["TIT2", "TPE1", "TALB", "TCOM", "TPE2", "TCON", "TRCK", "USLT", "TDRC", "APIC"]:
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
	
	# Procesar portada: si 'cover' existe en tags, se asume que es la ruta al archivo de imagen.
	if "cover" in tags and tags["cover"]:
		cover_path = tags["cover"]
		if os.path.exists(cover_path):
			ext = os.path.splitext(cover_path)[1].lower()
			mime = "image/jpeg"
			if ext == ".png":
				mime = "image/png"
			try:
				with open(cover_path, "rb") as img_file:
					data = img_file.read()
				audio.add(APIC(encoding=3,mime=mime,type=3, desc="",data=data))
			except Exception as e:
				print("Error al agregar la portada:", e)
		else:
			print(f"Advertencia: No se encontró la imagen de portada '{cover_path}'.")
	
	audio.save(archivo)