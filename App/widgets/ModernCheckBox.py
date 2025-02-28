from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ModernCheckBox(QCheckBox):
	def __init__(self, parent, text: str = None,  
			  widht = 60 ,
			  height = 28,
			  bg_color = "#777",
			  circle_color = "#DDD",
			  active_color = "#00BCff",
			  animation_curve = QEasingCurve.Type.OutQuint) :	#OutBounce
		QCheckBox.__init__(self,parent=parent)
		self.setFixedSize(widht, height)
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self._circle_radio = int(height * 4 / 5)
		#colors
		self._bg_color = bg_color
		self._circle_color = circle_color
		self._active_color = active_color


		#Animation
		self._circle_position = 3
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
			self.animation.setEndValue(self.width() - 26)
		else:
			self.animation.setEndValue(3)
		self.animation.start()

	def paintEvent(self, w):
		p = QPainter(self)
		p.setRenderHint(QPainter.RenderHint.Antialiasing)

		p.setPen(Qt.NoPen)

		#rectangle
		rect = QRect(0,0,self.width(),self.height())

		if self.isChecked() :
			#draw br
			p.setBrush(QColor(self._active_color))
			p.drawRoundedRect(0,0,rect.width(),self.height(),self.height()/2,self.height()/2)

			#draw circle
			p.setBrush(QColor(self._circle_color))
			p.drawEllipse(self._circle_position ,3,self._circle_radio,self._circle_radio)
		else:
			#draw br
			p.setBrush(QColor(self._bg_color))
			p.drawRoundedRect(0,0,rect.width(),self.height(),self.height()/2,self.height()/2)

			#draw circle
			p.setBrush(QColor(self._circle_color))
			p.drawEllipse(self._circle_position,3,self._circle_radio,self._circle_radio)
		
		p.end()	#end draw


		