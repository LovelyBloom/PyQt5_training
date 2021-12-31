from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.show()

app.exec_()