from PySide2 import QtWidgets, QtGui, QtCore,  QtUiTools
from PySide2.QtWidgets import QApplication
import sys
from utils import resource_path, ui_path

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Flint App')
        self.button = QtWidgets.QPushButton("Push for Window")
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_path('mainwindow.ui'))
        self.setCentralWidget(self.ui)

        self.temp_icon_path = "Z:\\dev\\qt_resources\\app\\resources\\my_icons\\tab_header.png"

        # self.setMinimumSize(2200, 1400)
        self.widgetAdditional()
    def widgetAdditional(self):
        ico = QtGui.QIcon(self.temp_icon_path) 
        self.ui.tabWidget.setTabIcon(1,ico)
        self.ui.tabWidget.setTabIcon(0,ico)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    style_file_path = resource_path('style.qss')
        
    style_file = QtCore.QFile(style_file_path)
    style_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(style_file)
    app.setStyleSheet(stream.readAll())

    window.show()
    app.exec_()