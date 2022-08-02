from turtle import update
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QApplication
from functools import partial
import sys

class ListSearch(QtWidgets.QWidget):
    def __init__(self):
        super(ListSearch, self).__init__()
        self.setWindowTitle('ttext')
    


        self.item_list = ['Model', 'Rig', 'Texture', 'Scan', 'Fx', 'CFX', 'Tex', 'Texx']
        # SERACH
        self.search_le = QtWidgets.QLineEdit()
        self.search_le.setPlaceholderText('Search')
        
        # LINE EDIT COMPLETER
        names = self.item_list
        completer = QtWidgets.QCompleter(names)
        self.search_le.setCompleter(completer)
        self.search_le.textChanged.connect(self.update)


        # LIST WIDGET
        self.list_widget = QtWidgets.QListWidget()
        self.list_widget.setAlternatingRowColors(True)
        

        # MAIN LAYOUT
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.search_le)
        self.main_layout.addWidget(self.list_widget)


        self.add_items(self.item_list)

    def update(self):
        query = self.search_le.text()
        updated_list = []
        if len(query) > 0:
            for i in  self.item_list:
                if query in i:
                    updated_list.append(i)
        else:
            updated_list = self.item_list

        self.list_widget.clear()
        self.add_items(updated_list)

    def add_items(self, item_list):
        for item in item_list:
            new_item = QtWidgets.QListWidgetItem()
            widget = CustomeListItem(str(item))
            new_item.setSizeHint(widget.sizeHint())
            widget.button.clicked.connect(partial(self.btn_clicked, new_item))
            self.list_widget.addItem(new_item)
            self.list_widget.setItemWidget(new_item, widget)
            # self.list_widget.setCurrentItem()

    def btn_clicked(self, sender):
        # self.list_widget.takeItem(self.list_widget.row(sender))
        print(self.current_value)

    @property
    def current_value(self):
        return self.list_widget.itemWidget(self.list_widget.currentItem()).text if self.list_widget.currentItem() else None
    

class CustomeListItem(QtWidgets.QWidget):
    def __init__(self, lable_text):
        super(CustomeListItem, self).__init__()

        self.text = lable_text
        lable = QtWidgets.QLabel(lable_text)
        self.button = QtWidgets.QPushButton(lable_text)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(lable)
        layout.addWidget(self.button)
        self.setLayout(layout)



if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = ListSearch()
    window.show()

    app.exec_()
