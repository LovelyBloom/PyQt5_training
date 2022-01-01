from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		label = QLabel("Using Singals to 'listen'\n and Slots to 'tell' what to do")

		label.setAlignment(Qt.AlignCenter)

		self.setCentralWidget(label)

		# Signals
		self.windowTitleChanged.connect(self.onWindowTitleChange)
		self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
		self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
		self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))

		self.setWindowTitle("Signals and Slots")

	def onWindowTitleChange(self, s):
		print(s)
	
	def my_custom_fn(self, a="HELLLO!", b=5):
		print(a, b)

	#override
	def contextMenuEvent(self, event):
		print("Context menu event!")
		super(MainWindow, self).contextMenuEvent(event)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()