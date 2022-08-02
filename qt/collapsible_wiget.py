from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
import sys

class CollapsableWiget(QtWidgets.QWidget):
    def __init__(self):
        super(CollapsableWiget, self).__init__()
        self.setWindowTitle('Collapse')

        layout = QtWidgets.QVBoxLayout()
        container = Container("Group")
        layout.addWidget(container)

        content_layout = QtWidgets.QGridLayout(container.contentWidget)

        btn = QtWidgets.QPushButton('Push Me')
        ckb  = QtWidgets.QCheckBox()

        content_layout.addWidget(btn)
        content_layout.addWidget(ckb)

        # layout1 = QtWidgets.QVBoxLayout()
        container_1 = Container('Main Group')
        layout.addWidget(container_1)

        content_layout_1 = QtWidgets.QGridLayout(container_1.contentWidget)

        label = QtWidgets.QLabel('WoW')
        btn1 = QtWidgets.QPushButton('Push me')

        content_layout_1.addWidget(label)
        content_layout_1.addWidget(btn1)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addLayout(layout)
        # self.main_layout.addLayout(layout1)


class Header(QtWidgets.QWidget):
    """Header class for collapsible group"""

    def __init__(self, name, content_widget):
        """Header Class Constructor to initialize the object.
        Args:
            name (str): Name for the header
            content_widget (QtWidgets.QWidget): Widget containing child elements
        """
        super(Header, self).__init__()
        self.content = content_widget
        self.expand_ico = QtGui.QPixmap(":teDownArrow.png")
        self.collapse_ico = QtGui.QPixmap(":teRightArrow.png")

        stacked = QtWidgets.QStackedLayout(self)
        stacked.setStackingMode(QtWidgets.QStackedLayout.StackAll)
        background = QtWidgets.QLabel()
        background.setStyleSheet("QLabel{ background-color: rgb(93, 93, 93); border-radius:2px}")

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(widget)

        self.icon = QtWidgets.QLabel()
        self.icon.setPixmap(self.expand_ico)
        layout.addWidget(self.icon)
        layout.setContentsMargins(11, 0, 11, 0)

        font = QtGui.QFont()
        font.setBold(True)
        label = QtWidgets.QLabel(name)
        label.setFont(font)

        layout.addWidget(label)
        layout.addItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        stacked.addWidget(widget)
        stacked.addWidget(background)
        background.setMinimumHeight(layout.sizeHint().height() * 1.5)

    def mousePressEvent(self, *args):
        """Handle mouse events, call the function to toggle groups"""
        self.expand() if not self.content.isVisible() else self.collapse()

    def expand(self):
        self.content.setVisible(True)
        self.icon.setPixmap(self.expand_ico)

    def collapse(self):
        self.content.setVisible(False)
        self.icon.setPixmap(self.collapse_ico)


class Container(QtWidgets.QWidget):
    """Class for creating a collapsible group similar to how it is implement in Maya
        Examples:
            Simple example of how to add a Container to a QVBoxLayout and attach a QGridLayout
            >>> layout = QtWidgets.QVBoxLayout()
            >>> container = Container("Group")
            >>> layout.addWidget(container)
            >>> content_layout = QtWidgets.QGridLayout(container.contentWidget)
            >>> content_layout.addWidget(QtWidgets.QPushButton("Button"))
    """
    def __init__(self, name, color_background=False):
        """Container Class Constructor to initialize the object
        Args:
            name (str): Name for the header
            color_background (bool): whether or not to color the background lighter like in maya
        """
        super(Container, self).__init__()
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self._content_widget = QtWidgets.QWidget()
        if color_background:
            self._content_widget.setStyleSheet(".QWidget{background-color: rgb(73, 73, 73); "
                                               "margin-left: 2px; margin-right: 2px}")
        header = Header(name, self._content_widget)
        layout.addWidget(header)
        layout.addWidget(self._content_widget)

        # assign header methods to instance attributes so they can be called outside of this class
        self.collapse = header.collapse
        self.expand = header.expand
        self.toggle = header.mousePressEvent

    @property
    def contentWidget(self):
        """Getter for the content widget
        Returns: Content widget
        """
        return self._content_widget


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = CollapsableWiget()
    window.show()

    app.exec_()
