import resource
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QApplication
import sys

from qt-resource.basic_window.basic_widget import BasicWidget


class CustomList(BasicWidget):
    def __init__(self):
        super(CustomList).__init__()



if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = BasicWidget()
    window.show()

    app.exec_()



