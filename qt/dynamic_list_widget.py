from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QApplication
from functools import partial
import sys

from basic_window.basic_widget import BasicWidget

class CustomList(BasicWidget):
    def __init__(self):
        super(CustomList).__init__()




class DynamicListWidgetItem(QtWidgets.QWidget):
    def __init__(self, label_text, size):
        super(DynamicListWidgetItem, self).__init__()
        # self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        self.text = label_text
        widget_label = QtWidgets.QLabel(label_text)
        widget_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)

        self.button = QtWidgets.QPushButton('-')
        self.button.setFixedSize(QtCore.QSize(size, size))
        self.button.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)

        self.cb = QtWidgets.QSpinBox()
        self.cb.setFixedSize(QtCore.QSize(size,size))
        self.cb.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(widget_label)
        layout.addWidget(self.cb)
        layout.addWidget(self.button)
        self.setLayout(layout)


class DynamicListWidget(QtWidgets.QWidget):
    def __init__(self, token, size=32):
        super(DynamicListWidget, self).__init__()
        self.setWindowTitle(f'{token} List')
        self.token = token
        self.size = size
        self.layout = QtWidgets.QVBoxLayout()
        # self.layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize)
        self.setLayout(self.layout)
        self.add_item_button = QtWidgets.QPushButton('+')
        self.add_item_button.setFixedSize(QtCore.QSize(size, size))
        self.item_list_widget = QtWidgets.QListWidget()
        # self.item_list_widget.setVerticalScrollBarPolicy(QtGui.Qt.ScrollBarAlwaysOff)
        # self.item_list_widget.setHorizontalScrollBarPolicy(QtGui.Qt.ScrollBarAlwaysOff)
        self.item_list_widget.setAlternatingRowColors(True)
        # self.item_list_widget.setSizeAdjustPolicy(self.item_list_widget.AdjustToContents)
        self.item_list_widget.currentItemChanged.connect(self.current_item_changed)
        self.layout.addWidget(self.item_list_widget)
        self.layout.addWidget(self.add_item_button)
        self.add_item_button.clicked.connect(self.add_item)
        # self.set_size()
        # self.resize(self.sizeHint())
        # set

    @property
    def current_value(self):
        return self.item_list_widget.itemWidget(self.item_list_widget.currentItem()).text if self.item_list_widget.currentItem() else None

    def current_item_changed(self):
        print(self.current_value)

    def add_item(self):
        text, ok = QtWidgets.QInputDialog.getText(self, f'Add {self.token}', f'{self.token} name')
        if ok:
            new_item = QtWidgets.QListWidgetItem()
            widget = DynamicListWidgetItem(str(text), self.size)
            widget.button.clicked.connect(partial(self.delete_button, new_item))
            new_item.setSizeHint(widget.sizeHint())
            self.item_list_widget.addItem(new_item)
            self.item_list_widget.setItemWidget(new_item, widget)
            self.item_list_widget.setCurrentItem(new_item)
            # self.set_size()

    def set_size(self):
        self.item_list_widget.setMinimumWidth(self.item_list_widget.sizeHintForColumn(0))
        if self.item_list_widget.count():
            self.item_list_widget.setFixedHeight(self.item_list_widget.sizeHintForRow(0) * self.item_list_widget.count() + 2)
        else:
            self.item_list_widget.setFixedHeight(0)
        self.setFixedHeight(self.sizeHint().height())

    def delete_button(self, sender):
        self.item_list_widget.takeItem(self.item_list_widget.row(sender))
        # self.set_size()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = DynamicListWidget('test')
    window.show()

    app.exec_()



