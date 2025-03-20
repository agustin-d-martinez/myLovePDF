from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class ModernLineEdit(QWidget):
	def __init__(self , placeholder_text = "" , parent = None):
		super().__init__(parent)
		self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
		
		# Margen para el texto al estar arriba. Punto inicial del QLineEdit.
		self._text_margin = 8
		self._current_mode = "IN"  # Estado inicial (placeholder centrado)

		#lineEdit
		self._line_edit = QLineEdit(self)

		# StyleSheet Recomendado. Por compatibilidad se puede modificar desde el main llamando a LineEdit()
		## self._line_edit.setStyleSheet("QLineEdit{border-radius:5px;border: 2px solid grey}QLineEdit::focus {border: 2px solid red}")

		#label
		self._label = QLabel(placeholder_text, self)
		self._label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
		self._label.setStyleSheet("color: grey; background-color: transparent;")
		self._label.show()

		#animacion
		self._animation = QPropertyAnimation(self._label , b"pos", self)
		self._animation.setDuration(200)
		self._animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

		#eventos del lineEdit reescritos
		self._line_edit.focusInEvent = self._on_focus_in
		self._line_edit.focusOutEvent = self._on_focus_out
		
	def resizeEvent(self, event):
		"""Coloca el QLineEdit y la etiqueta en posiciones apropiadas."""
		super().resizeEvent(event)

		inner_rect = QRect(0 , self._text_margin , self.width() , self.height() - self._text_margin)
		self._line_edit.setGeometry(inner_rect)
		self._label.move(self._label_position())

	def _on_focus_in(self, event):
		# Llamamos al focusInEvent original del QLineEdit
		QLineEdit.focusInEvent(self._line_edit, event)
		self._label.setStyleSheet("color: #B71C1C; background-color: white;")
		self._current_mode = "UP"
		self._animation.stop()
		self._animation.setStartValue(self._label.pos())
		self._animation.setEndValue(self._label_position())
		self._animation.start()

	def _on_focus_out(self, event):
		QLineEdit.focusOutEvent(self._line_edit, event)
		self._label.setStyleSheet("color: grey;")
		# Si no hay texto, regresamos la etiqueta al centro
		if not self._line_edit.text():
			self._label.setStyleSheet("background-color: transparent;")
			self._current_mode = "IN"
			self._animation.stop()
			self._animation.setStartValue(self._label.pos())
			self._animation.setEndValue(self._label_position())
			self._animation.start()


	def _label_position(self):
		'''Devuelve la posicion del label del estado actual. Pueden agregarse nuevos estados para nuevas animaciones'''
		if self._current_mode == "UP":
			return QPoint(5, 0)
		elif self._current_mode == "IN":
			x = 7
			y = self._text_margin + (self._line_edit.height() - self._label.height()) // 2
			return QPoint(x, y)

	# Métodos de LineEdit
	def text(self):
		return self._line_edit.text()

	def setText(self, txt):
		self._line_edit.setText(txt)

	def lineEdit(self):
		return self._line_edit

	

