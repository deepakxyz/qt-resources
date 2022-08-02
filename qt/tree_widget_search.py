from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QApplication
from functools import partial
import sys

class TreeSearch(QtWidgets.QWidget):
    def __init__(self):
        super(TreeSearch, self).__init__()
        self.setWindowTitle('Tree Search')

        self.search_le = QtWidgets.QLineEdit()
        self.search_le.setPlaceholderText('Search')


        self.tree_widget = QtWidgets.QTreeWidget()
        self.tree_widget