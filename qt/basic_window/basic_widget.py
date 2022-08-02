from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QApplication
import sys
import os

class BasicWidget(QtWidgets.QWidget):
    def __init__(self):
        super(BasicWidget, self).__init__()

        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.setMinimumSize(400,520) 



if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = BasicWidget()
    window.show()

    app.exec_()




