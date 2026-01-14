# This Python file uses the following encoding: utf-8
import sys
import tempfile
import requests
from pathlib import Path
import re
from typing import Optional, Tuple
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import ctypes

from ui_design import Ui_MainWindow

from customWidgets.ButtonListWidget import ButtonListWidget 
import libs.file as file
import libs.pdf as pdf
import libs.image as img
import libs.media as media
import libs.music as msc
from download_thread import DownloadWorker 

# Important:
# You need to run the following command to generate the ui_form.py file:
#     pyside6-rcc .\Icons\resources.qrc -o .\Icons\resources.py
# pyside6-designer
# from Icons import resources
# pyinstaller --onefile --windowed --ico=resources/Icons/app_icon.ico  mainwindow.py

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set Window Icon
        self.setWindowTitle("ILovePDF")
        self.setWindowIcon(QIcon(":/Icons/App_icon.ico"))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('AgustinM.MyLovePDF.app')	# Permite que cambie el logo del taskbar
        # self.ui.main_frame.setAttribute(Qt.WA_StyledBackground, True)

        # Set Stylesheets
        self._set_styles()
        self._set_icons()

        # Set GRIP
        self.grip = QSizeGrip(self)
        self.grip.resize(10, 10)

        # Set Drag
        self.dragStartPos = None
        self.dragPos = None
        self.normalGeometry = self.geometry()
        self.drag_state = self.DRAG_NONE
        self.dragRatioX = None
        self.ignoreRelease = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui.exit_frame.mousePressEvent = self._titleBar_mousePressEvent
        self.ui.exit_frame.mouseMoveEvent = self._titleBar_mouseMoveEvent
        self.ui.exit_frame.mouseReleaseEvent = self._titleBar_mouseReleaseEvent
        self.ui.exit_frame.mouseDoubleClickEvent = self._titleBar_mouseDoubleClickEvent

        # TODO Add resize from up, down, left and right

        # -----------------------------------------------------------
        # Set Connect Functions
        # -----------------------------------------------------------
        # Exit menu
        self.ui.close_button.clicked.connect(self.close)
        self.ui.minimize_button.clicked.connect(self.showMinimized)
        self.ui.maximize_button.clicked.connect(self.update_window_size)

        # Left Menu
        buttons = [ self.ui.pdf_button,
                   self.ui.img_button,
                   self.ui.file_button,
                   self.ui.video_button,]
        self.menu_group = QButtonGroup(self)
        for i, button in enumerate(buttons):
            self.menu_group.addButton(button, i)
        self.menu_group.idClicked.connect(self.ui.stackedWidget.setCurrentIndex)
    
        self._open_menu_width = self.ui.l_widget.width()
        self.ui.menu_button.clicked.connect(self.left_menu_toggle)

        # Pdf   
        self.ui.joinPdf_EvenPolicy_comboBox.hide()
        self.ui.JoinPdf_ApplyEven_Button.hide()
        self.ui.JoinPdf_ApplyEvenLabel.hide()
        self.ui.JoinPdf_Button.clicked.connect(self.join_pdf_clicked)
        self.ui.JoinPdf_selFile.clicked.connect(self._file_select)

        self.ui.SplitPdf_selFile.clicked.connect(self._file_select)
        self.ui.SplitPdf_Button.clicked.connect(self.split_pdf_clicked)

        self.ui.ExtractPdf_selFile.clicked.connect(self._file_select)
        self.ui.ExtractPdf_Button.clicked.connect(self.extract_sheets_clicked)

        self.ui.BlankPdf_selFile.clicked.connect(self._file_select)
        self.ui.BlankPdf_Button.clicked.connect(self.blank_sheet_clicked)

        # File
        self.ui.FileRname_selFile.clicked.connect(self._file_select)
        self.ui.FileRname_Button.clicked.connect(self.rename_files_clicked)
        self.ui.FileRname_Button.clicked.connect(self.ui.FileRname_In.listWidget.clear)

        # Img
        self.ui.ImgPdf_selFile.clicked.connect(self._file_select)
        self.ui.ImgPdf_Button.clicked.connect(self.img_to_pdf_clicked)

        self.ui.PdfImg_selFile.clicked.connect(self._file_select)
        self.ui.PdfImg_Button.clicked.connect(self.pdf_to_img_clicked)

        self.ui.ImgExt_selFile.clicked.connect(self._file_select)
        self.ui.ImgExt_Button.clicked.connect(self.img_ext_clicked)

        self.ui.ImgRsize_selFile.clicked.connect(self._file_select)
        self.ui.ImgRsize_In.editingFinished.connect(self._update_img_res)
        self.ui.ImgRsize_Button.clicked.connect(self.resize_img_clicked)

        # Video/Media
        self._thumb_pixmap_cache = {}
        self.ui.VidDown_listFrame.hide()
        self.ui.VidDown_all_checkBox.hide()
        self.ui.VidDown_progressBar.hide()                                      
        self.ui.VidDown_Button.clicked.connect(self.video_download_clicked)
        self.ui.VidDown_list.currentItemChanged.connect( lambda current, _: self.on_playlist_item_changed(current) )
        self.ui.VidDown_In.editingFinished.connect(self.update_from_url)

        self.ui.MP3toMP4_selFile.clicked.connect(self._file_select)
        self.ui.MP3toMP4_Button.clicked.connect(self.mp4_to_mp3_clicked)

        self.ui.VidTag_selFile.clicked.connect(self._file_select)               
        self.ui.VidTag_Update.clicked.connect(self._update_music_folder)
        self.ui.VidTag_In.editingFinished.connect(self._update_music_folder)
        self.ui.VidTag_List.listWidget.itemSelectionChanged.connect(self._update_selected_music)
        self.ui.VidTag_Button.clicked.connect(self.video_tag_clicked)

    # ----------------------------------------------
    # Maximize/Restore Functions
    # ----------------------------------------------
    # DEFINE DRAG STATES
    DRAG_NONE = 0
    DRAG_ARMING = 1  
    DRAGGING = 2
    def update_window_size(self, checked):
        if checked:
            self.normalGeometry = self.geometry()
            self.showMaximized()
            self.grip.hide()
        else:
            self.showNormal()
            self.grip.show()
    
    def _titleBar_mousePressEvent(self, event: QMouseEvent):
        if event.button() != Qt.MouseButton.LeftButton:
            return

        # Start values of drag and release logic
        self.drag_state = self.DRAG_ARMING
        self.dragStartPos = event.globalPosition().toPoint()
        if self.isMaximized():
            self.dragRatioX = event.position().x() / self.width()
        else:
            self.dragRatioX = None
        self.dragPos = self.dragStartPos - self.frameGeometry().topLeft()
        event.accept()
    
    def _titleBar_mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() != Qt.MouseButton.LeftButton:
            return
        
        # dragg logic         
        dist = (event.globalPosition().toPoint() - self.dragStartPos).manhattanLength()
        if self.drag_state == self.DRAG_NONE or dist < 10:
            return
        self.drag_state = self.DRAGGING

        # if maximized, restore and move
        if self.isMaximized():
            self.ui.maximize_button.setChecked(False)
            self.update_window_size(False)

            normal_widht = self.normalGeometry.width()
            mouse_x = event.globalPosition().toPoint().x()
            mouse_y = event.globalPosition().toPoint().y()

            x = int(mouse_x - self.dragRatioX * normal_widht)
            self.move(x, mouse_y)

            self.dragPos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            self.dragRatioX = None
            event.accept()
            return
        self.move(event.globalPosition().toPoint() - self.dragPos)
        event.accept()

    def _titleBar_mouseReleaseEvent(self, event: QMouseEvent):
        # Ignore mouse Release. Used in double click maximize.
        if self.ignoreRelease:
            self.ignoreRelease = False
            self.drag_state = self.DRAG_NONE
            event.accept()
            return
        
        # If not dragging, do nothing
        if self.drag_state != self.DRAGGING:
            event.accept()
            return
        
        # if dragging, check "snap to maximize" 
        self.drag_state = self.DRAG_NONE
        if event.globalPosition().toPoint().y() <= 5:
            self.ui.maximize_button.setChecked(True)
            self.update_window_size(True)
        else:
            self.ui.maximize_button.setChecked(False)
            self.update_window_size(False)
        event.accept()

    def _titleBar_mouseDoubleClickEvent(self, event: QMouseEvent):
        # Double click maximize/restore logic
        self.ignoreRelease = True
        is_not_maximized = not self.isMaximized()
        self.ui.maximize_button.setChecked(is_not_maximized)
        self.update_window_size(is_not_maximized)
        event.accept()

    def resizeEvent(self, event):
        self.grip.move(
            self.width() - self.grip.width(),
            self.height() - self.grip.height(),
        )
        return super().resizeEvent(event)

    def left_menu_toggle(self, checked: bool):
        self.left_menu_animation = QPropertyAnimation(self.ui.l_widget, b"maximumWidth")
        self.left_menu_animation.setDuration(250)
        self.left_menu_animation.setEasingCurve(QEasingCurve.Type.InOutQuart)

        end_val = self._open_menu_width if checked else 50
        #end_val = 180 if checked else 40
        start_val = self.ui.l_widget.maximumWidth()

        self.left_menu_animation.setStartValue(start_val)
        self.left_menu_animation.setEndValue(end_val)
        self.left_menu_animation.start()

    # ----------------------------------------------
    # PDF Functions
    # ----------------------------------------------
    def blank_sheet_clicked(self):
        input_path = self.ui.BlankPdf_In.text()
        if not input_path:
            self._error_message("No se ingresó ningún archivo.")
            return
        sheets = self._get_ranges(self.ui.BlankPdf_Sheets.text())
        if not sheets:
            self._error_message("No se cargaron rangos correctos")
            return
        inplace = self.ui.BlankPdf_Inplace_Button.isChecked()
        if not inplace:
            output_path = self._save_file("Archivo PDF (*.pdf)")
            if not output_path:
                return
        
        try:
            pdf.add_blank_page(input_path, output_path, sheets, inplace=inplace)
        except Exception as e:
            self._error_message(f"Fallo al añadir hojas en blanco en el PDF:\n{e}")
            return

        QMessageBox().information(self,"PDF generado", "Hojas en blanco añadidas con éxito.")

    def split_pdf_clicked(self):
        input_path = self.ui.SplitPdf_In.text()
        if not input_path:
            self._error_message("No se ingresó ningún archivo.")
            return
        sheets = self._get_ranges(self.ui.SplitPdf_Sheets.text())
        if not sheets:
            self._error_message("No se cargaron rangos correctos")
            return
        
        output_path = self._save_file("Archivo PDF (*.pdf)")
        if not output_path:
            return
        
        try:
            pdf.split_pdf(input_path, output_path, sheets)
        except Exception as e:
            self._error_message(f"Fallo al separar el PDF:\n{e}")
            return

        QMessageBox().information(self,"PDF Generado", "PDF separado con éxito.")

    def join_pdf_clicked(self):
        even_policy_dict = {0: pdf.EvenPolicy.PAD_START, 1: pdf.EvenPolicy.PAD_END}

        input_path = [Path(p) for p in self._get_listwidget_text(self.ui.JoinPdf_In.listWidget)]
        if len(input_path) == 0:
            self._error_message("No se ingresó ningún archivo.")
            return
        elif len(input_path) == 1:
            self._error_message("No se ingresaron suficientes archivos.")
            return

        is_even = self.ui.JoinPdf_isEven_Button.isChecked()
        policy = even_policy_dict[self.ui.joinPdf_EvenPolicy_comboBox.currentIndex()]
        apply_all = self.ui.JoinPdf_ApplyEven_Button.isChecked()

        output_path = self._save_file("Archivo PDF (*.pdf)")
        if not output_path:
            return

        try:
            if is_even and apply_all:
                tmp_ctx = tempfile.TemporaryDirectory()
                tmpdir = Path(tmp_ctx.name)

                new_input_path: list[Path] = []
                for i, path in enumerate(input_path):
                    tmp_pdf = tmpdir / f"even_{i}.pdf"
                    pdf.evenize_pdf(path, output_path=tmp_pdf, policy=policy)
                    new_input_path.append(tmp_pdf)
                input_path = new_input_path
            else:
                tmp_ctx = None

            pdf.join_pdf(input_path, output_path)
            if is_even and not apply_all:
                pdf.evenize_pdf(output_path, policy=policy, inplace=True)
        except Exception as e:
            self._error_message(f"Fallo al unir los PDF:\n{e}")
            return
        finally:
            if tmp_ctx:
                tmp_ctx.cleanup()
        QMessageBox().information(self, "PDF generado", "PDFs unidos con éxito.")

    def extract_sheets_clicked(self):
        input_path = self.ui.ExtractPdf_In.text()
        if not input_path:
            self._error_message("No se ingresó ningún PDF")
            return
        
        output_path = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta", "")
        if not output_path:
            return
        
        if self.ui.ExtractPdf_All_Button.isChecked():
            sheets = None
        else:
            sheets = self._get_ranges(self.ui.ExtractPdf_Sheets.text())
        
        try:
            pdf.split_pages(input_path, output_path, sheets)
        except Exception as e:
            self._error_message(f"Fallo al extraer páginas de PDF:\n{e}")
            return
        QMessageBox().information(self,"PDF generado", "Hojas extraidas con éxito.")

    # ----------------------------------------------
    # Video/Media Functions
    # ----------------------------------------------
    def video_download_clicked(self):
        url = self.ui.VidDown_In.text()
        if not url:
            self._error_message("No se ingresaron URLs.")
            return
        only_audio = self.ui.VidDown_OnlyAudio.isChecked()
        title = self.ui.VidDown_Title.text()

        format = ".mp3" if only_audio else ".mp4"
        output_path = self._save_file(f"Archivo {format.upper()[1:]} File (*{format}))", title)
        if not output_path:
            return
        
        resolution = self.ui.VidDown_res.currentText()
        if resolution == "Best Resolution":
            resolution = None
            
        self.ui.VidDown_Button.hide()
        self.ui.VidDown_progressBar.setValue(0)
        self.ui.VidDown_progressBar.show()

        self.download_thread = DownloadWorker(url=url, output_path=output_path, only_audio=only_audio, resolution=resolution)
        self.download_thread.progress.connect(self.ui.VidDown_progressBar.setValue)
        self.download_thread.finished.connect(self._download_finish)
        self.download_thread.error.connect(self._download_error)

        self.download_thread.start()

    def _download_error(self, msg):
        self.ui.VidDown_Button.show()
        self.ui.VidDown_progressBar.hide()
        self._error_message(f"Error durante la descarga:\n{msg}")

    def _download_finish(self):
        print("paso")
        self.ui.VidDown_Button.show()
        self.ui.VidDown_progressBar.hide()
        QMessageBox().information(self, "Archivo descargado", f"Archivo Descargado con éxito.")

    def update_from_url(self):
        url = self.ui.VidDown_In.text().strip()
        if not url:
            return

        try:
            raw_data = media.get_video_info(url)
        except Exception:
            return

        self._video_data = media.normalize_videos(raw_data)

        if len(self._video_data) > 1:
            self._setup_playlist()
        else:
            self._setup_single_video(self._video_data[0])

    def _setup_single_video(self, video):
        self.ui.VidDown_listFrame.hide()
        self.ui.VidDown_all_checkBox.hide()

        self._update_common_fields(video)
        self._viddown_update_thumbnail(video)

    def _setup_playlist(self):
        self.ui.VidDown_listFrame.show()
        self.ui.VidDown_all_checkBox.show()
        self.ui.VidDown_list.clear()

        for video in self._video_data:
            item = QListWidgetItem(video.get("title", "Sin título"))
            item.setData(Qt.ItemDataRole.UserRole, video)
            self.ui.VidDown_list.addItem(item)

        self.ui.VidDown_list.setCurrentRow(0)

    def _viddown_update_thumbnail(self, video: dict):
        thumb_url = video.get("thumbnail")
        if not thumb_url:
            thumb_url = media.get_thumbnail_url(video)

        if thumb_url in self._thumb_pixmap_cache:
            pixmap = self._thumb_pixmap_cache[thumb_url]
        else:
            pixmap = self._get_pixmap_from_url(thumb_url)
            if not pixmap:
                return
            self._thumb_pixmap_cache[thumb_url] = pixmap

        self.ui.VidDown_Thumb.setPixmap(
            pixmap.scaled(
                self.ui.VidDown_Thumb.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

    def on_playlist_item_changed(self, current: QListWidgetItem):
        if not current:
            return

        video = current.data(Qt.ItemDataRole.UserRole)
        if not video:
            return

        self._update_common_fields(video)
        self._viddown_update_thumbnail(video)

    def _update_common_fields(self, video: dict):
        self.ui.VidDown_Title.setText(video.get("title", "Sin título"))

        duration = media.format_duration(video.get("duration"))
        size = media.get_estimated_size(video)

        self.ui.VidDown_dur.setText(duration)
        self.ui.VidDown_size.setText(size)

    def _viddown_update_thumbnail_from_url(self, thumb_url: str):
        if not thumb_url:
            return

        if thumb_url in self._thumb_pixmap_cache :
            pixmap = self._thumb_pixmap_cache [thumb_url]
        else:
            pixmap = self._get_pixmap_from_url(thumb_url)
            if pixmap:
                self._thumb_pixmap_cache[thumb_url] = pixmap

        if pixmap:
            self.ui.VidDown_Thumb.setPixmap(
                pixmap.scaled(
                    self.ui.VidDown_Thumb.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            )

    def mp4_to_mp3_clicked(self):   
        input_path = self.ui.MP3toMP4_In.text()
        if not input_path and not input_path.endswith(".mp4"):
            self._error_message("No se ingresó ningún archivo MP4.")
            return
        output_path = self._save_file(".mp3")
        if not output_path:
            return
        
        try:
            media.extract_audio(input_path, output_path )
        except Exception as e:
            self._error_message("Error al convertir a MP3.")
            return
        QMessageBox().information(self, "Archivo generado", f"Audio extraido con éxito.")

    def video_tag_clicked(self):   
        item = self.ui.VidTag_List.listWidget.currentItem()
        if not item:
            self._error_message("No se seleccionó ninguna canción")
            return

        base_dir = Path(self.ui.VidTag_In.text())
        input_path = base_dir / item.text()

        if not input_path.exists():
            self._error_message("No se seleccionó ningún archivo.")
            return

        tags = {
            "title": self.ui.VidTag_Title.text(),
            "artist": self.ui.VidTag_Intr.text(),
            "album": self.ui.VidTag_Alb.text(),
            "composer": self.ui.VidTag_Comp.text(),
            "album_artist": self.ui.VidTag_IntrAlb.text(),
            "genre": self.ui.VidTag_Genre_comboBox.currentText(),
            "track": f"{self.ui.VidTag_Track.value()}/{self.ui.VidTag_TrackAll.value()}",
            "lyrics": self.ui.VidTag_Lyrics.toPlainText(),
            "year": self.ui.VidTag_Year.text(),
            "mood": self.ui.VidTag_Mood.text(),
        }

        pixmap = self.ui.VidTag_Cover.pixmap()
        if pixmap:
            buffer = QBuffer()
            buffer.open(QIODevice.OpenModeFlag.WriteOnly)
            pixmap.save(buffer, "PNG")
            tags["cover"] = bytes(buffer.data())
            buffer.close()

        try:
            msc.set_music_tags(input_path, tags)
        except Exception as e:
            self._error_message("Error al actualizar MP3.")
            return
        QMessageBox.information(self,"Archivo Actualizado","Música guardada con éxito.")

    def _update_music_folder(self):
        self.ui.VidTag_List.listWidget.clear()
        folder = self.ui.VidTag_In.text()
        if not folder:
            return
        music_list = file.search_file_tipe(folder, ".mp3", recursive=True)
        self.ui.VidTag_List.listWidget.addItems(music_list)

    def _update_selected_music(self):
        items = self.ui.VidTag_List.listWidget.selectedItems()
        if not items:
            self._clear_music_fields()
            return

        base_dir = Path(self.ui.VidTag_In.text())
        input_path = base_dir / items[0].text()

        tags = msc.get_music_tags(input_path)

        self.ui.VidTag_Title.setText(tags.get("title", ""))
        self.ui.VidTag_Intr.setText(tags.get("artist", ""))
        self.ui.VidTag_Alb.setText(tags.get("album", ""))
        self.ui.VidTag_Comp.setText(tags.get("composer", ""))
        self.ui.VidTag_IntrAlb.setText(tags.get("album_artist", ""))
        self.ui.VidTag_Lyrics.setPlainText(tags.get("lyrics", ""))
        self.ui.VidTag_Year.setText(tags.get("year", ""))

        track, total = self._parse_track_tag(tags.get("track", ""))
        self.ui.VidTag_Track.setValue(track)
        self.ui.VidTag_TrackAll.setValue(total)

        self.ui.VidTag_Genre_comboBox.setCurrentText(tags.get("genre", ""))
        self.ui.VidTag_Mood.setText(tags.get("mood", ""))

        self._update_cover(tags.get("cover"))

    def _clear_music_fields(self):
        self.ui.VidTag_Title.clear()
        self.ui.VidTag_Intr.clear()
        self.ui.VidTag_Alb.clear()
        self.ui.VidTag_Comp.clear()
        self.ui.VidTag_IntrAlb.clear()
        self.ui.VidTag_Lyrics.clear()
        self.ui.VidTag_Year.clear()
        self.ui.VidTag_Track.setValue(0)
        self.ui.VidTag_TrackAll.setValue(0)
        self.ui.VidTag_Genre_comboBox.setCurrentIndex(0)
        self.ui.VidTag_Mood.clear()
        self.ui.VidTag_Cover.setPixmap(self.ui.VidTag_Cover.default_pixmap)

    def _update_cover(self, cover):
        pixmap = self.ui.VidTag_Cover.default_pixmap

        if isinstance(cover, dict):
            data = cover.get("data")
            if data:
                pm = QPixmap()
                if pm.loadFromData(data):
                    pixmap = pm

        self.ui.VidTag_Cover.setPixmap(
            pixmap.scaled(self.ui.VidTag_Cover.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        )

    def _parse_track_tag(self, tag: str) -> Tuple[Optional[int], Optional[int]]:
        if not tag:
            return None, None

        tag = tag.strip()

        match = re.search(r"(\d+)\s*(?:/|of|-)\s*(\d+)", tag, re.IGNORECASE)
        if match:
            return int(match.group(1)), int(match.group(2))

        match = re.search(r"(\d+)", tag)
        if match:
            return int(match.group(1)), None

        return None, None

    # ----------------------------------------------
    # Files Functions
    # ----------------------------------------------
    def rename_files_clicked(self):
        input_path = self._get_listwidget_text(self.ui.FileRname_In.listWidget)
        if len(input_path) == 0:
            self._error_message("No se ingresó ningún archivo.")
            return
        try:
            file.rename_files(input_path, 
                              self.ui.FileRname_Template.text(),
                              self.ui.FileRname_Num.value())
        except Exception as e:
            self._error_message(f"Fallo al renombrar los archivos:\n{e}")
            return

        QMessageBox().information(self,"Archivos renombrados", "Archivos renombrados con éxito.")

    # ----------------------------------------------
    # Image Functions
    # ----------------------------------------------
    def img_to_pdf_clicked(self):
        input_path = self.ui.ImgPdf_In.text()
        if len(input_path) == 0:
            self._error_message("No se ingresó ningún archivo.")
            return
        output_path = self._save_file("Archivo PDF (*.pdf)")
        if not output_path:
            return
        
        try:
            pdf.img_to_pdf(input_path,output_path)
        except Exception as e:
            self._error_message(f"Fallo al convertir imágenes a PDF:\n{e}")
            return
        QMessageBox().information(self,"Archivos generados", "PDF's creados con éxito.")

    def pdf_to_img_clicked(self):
        input_path = self.ui.PdfImg_In.text()
        if len(input_path) == 0:
            self._error_message("No se ingresó ningún archivo.")
            return
        output_path = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta", "")
        if not output_path:
            return
        
        try:
            pdf.pdf_to_img(input_path,output_path)
        except Exception as e:
            self._error_message(f"Fallo al convertir PDF en imágenes:\n{e}")
            return
        QMessageBox().information(self,"Archivos generados", "Imágenes creadas con éxito.")

    def img_ext_clicked(self):
        input_path = self.ui.ImgExt_In.text()
        if not input_path :
            self._error_message("No se ingresó ningún archivo.")
            return
        
        ext = self.ui.ImgExt_comboBox.currentText()
        try:
            img.change_img_ext(input_path, ext)
        except Exception as e:
            self._error_message("Error al cambiar la extensión de la imagen.")
            return
        
        QMessageBox().information(self,"Archivos generados", "Imagen modificada con éxito.")

    def resize_img_clicked(self):   # TODO
        input_path = Path(self.ui.ImgRsize_In.text())

        try:
            width = int(self.ui.ImgRsize_NW.text())
            height = int(self.ui.ImgRsize_NH.text())
        except Exception as e:
            self._error_message("Resolución inválida")
            return
        
        if width <= 0 or height <= 0:
            self._error_message("Resolución de salida incorrecta")
            return

        suggested = input_path.with_stem(input_path.stem + "_scaled")
        output_path = self._save_file("Images (*.png *.jpg *.jpeg *.bmp)", str(suggested))
        if output_path is None:
            return  
        try:
            img.resize_image(input_path, (width, height), output_path)
        except Exception as e:
            self._error_message(f"Fallo al reescalar la imagen:\n{e}")
            return
        QMessageBox().information(self,"Imagen reescalada", "Imagen reescalada con éxito.")

    def _update_img_res(self):
        input_path = self.ui.ImgRsize_In.text()
        try:
            resolution = img.get_image_size(input_path)
        except Exception as e:
            self.ui.ImgRsize_AW.setText("")
            self.ui.ImgRsize_AH.setText("")
            return
        
        self.ui.ImgRsize_AW.setText(str(resolution[0]))
        self.ui.ImgRsize_AH.setText(str(resolution[1]))

    # ----------------------------------------------
    # Helpers
    # ----------------------------------------------
    def _get_listwidget_text( self, listWidget: QListWidget ) -> list[str] : 
        ret = [listWidget.item(i).text() for i in range(listWidget.count()) ]
        return ret

    def _save_file(self, filter, suggested_name:str = "") -> str:
        file_path , _ =  QFileDialog.getSaveFileName(self,"Guardar Archivo", suggested_name , filter)
        if not file_path:
            return None
        return file_path		

    def _error_message(self, mensaje: str) -> None:
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Critical)  
        msg.setWindowTitle("Error")
        msg.setText(mensaje)
        msg.exec()  

    def _file_select(self):
        sender_map = {
            self.ui.JoinPdf_selFile: ("pdf", self.ui.JoinPdf_In.listWidget, True),
            self.ui.SplitPdf_selFile: ("pdf", self.ui.SplitPdf_In, False),
            self.ui.ExtractPdf_selFile: ("pdf", self.ui.ExtractPdf_In, False),
            self.ui.BlankPdf_selFile: ("pdf", self.ui.BlankPdf_In, False),
            self.ui.FileRname_selFile: ("all", self.ui.FileRname_In.listWidget, True),
            self.ui.ImgExt_selFile: ("img", self.ui.ImgExt_In, False),
            self.ui.ImgPdf_selFile: ("img", self.ui.ImgPdf_In, False),
            self.ui.ImgRsize_selFile: ("img", self.ui.ImgRsize_In, False),
            self.ui.PdfImg_selFile: ("pdf", self.ui.PdfImg_In, False),
            self.ui.MP3toMP4_selFile: ("mp4", self.ui.MP3toMP4_In, False),
            self.ui.VidTag_selFile: ("dir", self.ui.VidTag_In, False),
        }
        sender = self.sender()
        if sender not in sender_map:
            return

        file_type, target_widget, multiple = sender_map[sender]
        if file_type == "dir":
            directory = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta de música", "")
            if not directory:
                return

            target_widget.setText(directory)

            self._update_music_folder()
            return

        filters = {
            "pdf": "Archivos PDF (*.pdf)",
            "img": "Image Files (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)",
            "mp4": "MP4 Video Files (*.mp4)",
            "all": "All Files (*)",
        }

        if multiple:
            files, _ = QFileDialog.getOpenFileNames(
                self, "Seleccionar Archivo", "", filters[file_type]
            )
            if not files:
                return
            target_widget.addItems(files)
        else:
            file, _ = QFileDialog.getOpenFileName(
                self, "Seleccionar Archivo", "", filters[file_type]
            )
            if not file:
                return
            target_widget.setText(file)

        if sender == self.ui.ImgRsize_selFile:
            self._update_img_res()

    def _get_pixmap_from_url(self, url: str) -> QPixmap | None:
        if not url:
            return None

        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None

        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        return pixmap

    def _get_ranges(self,string: str) -> list[int] :
        lista = set()
        for number in string.split(","):
            if '-' in number:
                start, stop = map(int,number.split('-'))
                lista.update(range(start,stop + 1))
            else :
                lista.add(int(number))
        return sorted(lista)

    def _set_styles(self, theme:str ="dark"):
        qss = ""

        # Base (estructura)
        qss += self._load_qss(":/styles/base/base.qss")

        # Widgets
        qss += self._load_qss(":/styles/widgets/buttons.qss")
        qss += self._load_qss(":/styles/widgets/inputs.qss")
        qss += self._load_qss(":/styles/widgets/lists.qss")
        qss += self._load_qss(":/styles/widgets/tabs.qss")
        qss += self._load_qss(":/styles/widgets/custom.qss")

        # Theme (solo colores)
        qss += self._load_qss(f":/styles/themes/{theme}.qss")

        QApplication.instance().setStyleSheet(qss)

    def _load_qss(self, resource_path: str) -> str:
        file = QFile(resource_path)
        if not file.open( QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            return
        stream = QTextStream(file)
        return stream.readAll()

    def _set_icons(self, theme: str = "dark"):
        qss = ":/Icons/"

        if theme == "dark":
            icons = {
                "add": QIcon(qss + "add_file_w.png"),
                "delete": QIcon(qss + "delete_w.png"),
                "up": QIcon(qss + "up_arrow_w.png"),
                "down": QIcon(qss + "down_arrow_w.png"),
                "reload": QIcon(qss + "reload_w.png"),
                "no_img": QPixmap(qss + "no_image_w.png"),
            }
        else:
            icons = {
                "add": QIcon(qss + "add_file.png"),
                "delete": QIcon(qss + "delete.png"),
                "up": QIcon(qss + "up_arrow.png"),
                "down": QIcon(qss + "down_arrow.png"),
                "reload": QIcon(qss + "reload.png"),
                "no_img": QPixmap(qss + "no_image.png"),
            }

        # Buttons
        scaled_cover = icons["no_img"].scaled(self.ui.VidTag_Cover.size(), 
                                              Qt.AspectRatioMode.KeepAspectRatio, 
                                              Qt.TransformationMode.SmoothTransformation )
        scaled_thumb = icons["no_img"].scaled(self.ui.VidTag_Cover.size(), 
                                              Qt.AspectRatioMode.KeepAspectRatio, 
                                              Qt.TransformationMode.SmoothTransformation )

        self.ui.VidTag_Cover.setDefaultPixmap(scaled_cover) 
        self.ui.VidTag_Cover.setPixmap(scaled_cover)
        self.ui.VidDown_Thumb.setPixmap(scaled_thumb)
        self.ui.VidTag_Update.setIcon(icons["reload"])

        # All ButtonListWidget 
        for blw in self.findChildren(ButtonListWidget):
            blw.setIcons(
                icons["add"],
                icons["delete"],
                icons["up"],
                icons["down"],
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())