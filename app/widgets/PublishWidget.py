import os
from PySide2 import QtWidgets


class PublishWidget(QtWidgets.QWidget):
    def __init__(self, text):
        super().__init__()
        self.main_layout = QtWidgets.QVBoxLayout()

        self.main_widget = QtWidgets.QWidget()
        self.main_widget.setObjectName('mainWidget')
        self.main_widget.setStyleSheet('''
        QWidget#mainWidget{
            background:#252525;
            border-radius:12px;
            border: 1px solid #000;
        }
        QWidget#mainWidget:hover{

            background:#cdcdcd;
        }
        
        ''')
        self.sub_layout = QtWidgets.QVBoxLayout()
        self.main_widget.setLayout(self.sub_layout)

        self.header_widget = QtWidgets.QLabel(text)
        self.body_widget = QtWidgets.QPushButton('Published')
        self.sub_layout.addWidget(self.header_widget)
        self.sub_layout.addWidget(self.body_widget)


        self.main_layout.addWidget(self.main_widget)
        self.setLayout(self.main_layout)
