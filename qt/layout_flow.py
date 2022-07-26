"""PySide6 port of the widgets/layouts/flowlayout example from Qt v6.x"""

import sys
from PySide6.QtCore import Qt, QMargins, QPoint, QRect, QSize
from PySide6.QtWidgets import QApplication, QLayout, QPushButton, QSizePolicy, QWidget
from PySide6 import QtWidgets



class CustomWidget(QWidget):
    def __init__(self, name):
        super().__init__()
        self.setStyleSheet('''
        QWidget#mainWidget{
            background:red;
        };
        ''')

        self.setObjectName('mainWidget')

        # header layout
        self.header_text = QtWidgets.QLabel(name)
        self.header_btn = QtWidgets.QPushButton()
        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.addWidget(self.header_text)
        self.header_layout.addWidget(self.header_btn)

        # body
        self.body_text = QtWidgets.QLabel(name + "_grey")
        self.body_layout = QtWidgets.QVBoxLayout()
        self.body_layout.addWidget(self.body_text)

        # mainlayout 
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addLayout(self.body_layout)

        self.setLayout(self.main_layout)





class Window(QWidget):
    def __init__(self):
        super().__init__()

        flow_layout = FlowLayout(self)
        # CUSTOM WIDGET
        self.cs_wgt  = CustomWidget('Test1')
        flow_layout.addWidget(self.cs_wgt)
        flow_layout.addWidget(CustomWidget('Test2'))
        flow_layout.addWidget(CustomWidget('Test3'))
        flow_layout.addWidget(CustomWidget('Test4'))
        flow_layout.addWidget(CustomWidget('Test5'))

        self.setWindowTitle("Flow Layout")


class FlowLayout(QLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

        if parent is not None:
            self.setContentsMargins(QMargins(0, 0, 0, 0))

        self._item_list = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self._item_list.append(item)

    def count(self):
        return len(self._item_list)

    def itemAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list[index]

        return None

    def takeAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientation(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self._do_layout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self._do_layout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self._item_list:
            size = size.expandedTo(item.minimumSize())

        size += QSize(2 * self.contentsMargins().top(), 2 * self.contentsMargins().top())
        return size

    def _do_layout(self, rect, test_only):
        x = rect.x()
        y = rect.y()
        line_height = 0
        spacing = self.spacing()

        for item in self._item_list:
            style = item.widget().style()
            layout_spacing_x = style.layoutSpacing(
                QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Horizontal
            )
            layout_spacing_y = style.layoutSpacing(
                QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Vertical
            )
            space_x = spacing + layout_spacing_x
            space_y = spacing + layout_spacing_y
            next_x = x + item.sizeHint().width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0

            if not test_only:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        return y + line_height - rect.y()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Window()
    main_win.show()
    sys.exit(app.exec())