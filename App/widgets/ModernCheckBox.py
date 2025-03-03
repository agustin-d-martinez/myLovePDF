from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ModernCheckBox(QCheckBox):
	def __init__(self, parent, text: str = None,  
			  width = 60 ,
			  height = 28,
			  bg_color = "#777",
			  circle_color = "#DDD",
			  active_color = "#00BCff",
			  animation_curve = QEasingCurve.Type.OutQuint) :	#OutBounce
		QCheckBox.__init__(self,parent=parent)
		# self.setFixedSize(width, height)
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self._circle_radio = int(height * 2/5)
		#colors
		self._bg_color = bg_color
		self._circle_color = circle_color
		self._active_color = active_color


		#Animation
		self._circle_start = int(height*0.2)
		self._circle_end = width - height
		self._circle_position = self._circle_start
		self.animation = QPropertyAnimation(self,b"circle_position",self)
		self.animation.setEasingCurve(animation_curve)
		self.animation.setDuration(500)

		#connects
		self.stateChanged.connect(self.start_animation)
	
	#setter and getter of animation property
	@Property(float) # Get
	def circle_position(self):
		return self._circle_position
	
	@circle_position.setter
	def circle_position(self, pos):
		self._circle_position = pos
		self.update()

	# Set the hit area
	def hitButton(self, pos : QPoint):
		return self.contentsRect().contains(pos)

	def start_animation(self, value):
		self.animation.stop()
		if value:
			self.animation.setEndValue(self._circle_end)
		else:
			self.animation.setEndValue(self._circle_start)
		self.animation.start()

	def paintEvent(self, w):
		width = self.width()
		height = self.height() // 2

		p = QPainter(self)
		p.setRenderHint(QPainter.RenderHint.Antialiasing)

		p.setPen(Qt.NoPen)

		#rectangle
		rect = QRect(0,0,width,height)


		#draw br
		if self.isChecked() :
			p.setBrush(QColor(self._active_color))
		else:
			p.setBrush(QColor(self._bg_color))

		p.drawRoundedRect(0,height,width, height, height/2, height/2)

		#draw circle
		p.setBrush(QColor(self._circle_color))
		p.drawEllipse(self._circle_position, height + (height - self._circle_radio)/2 ,self._circle_radio, self._circle_radio)

		text = self.text()
		if text:
			# Configuramos el color y la fuente para el texto
			p.setPen(Qt.black)  # O el color que prefieras
			font = p.font()
			font.setPointSize(10)  # O el tamaño deseado
			p.setFont(font)
			# Dibujar el texto centrado en el rectángulo del widget
			p.drawText(rect, Qt.AlignmentFlag.AlignLeft, text)

		p.end()	#end draw

	def resizeEvent(self, event):
		super().resizeEvent(event)
		height = self.height() // 2
		width = self.width()

		self.setFixedSize(width, 2* height)

		self._circle_start = int(height*0.2)
		self._circle_end = width - height
		self._circle_radio = int(height * 4/5)

		self.update()


		