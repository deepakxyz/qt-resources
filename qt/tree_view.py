from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QApplication
from  utils import resource_path
import sys



class StandardItem(QtGui.QStandardItem):
    def __init__(self,text='', font_size =12, set_bold=False, color=QtGui.QColor(0,0,0)):
        super().__init__()

        fnt = QtGui.QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(text)
        icon_path =(resource_path('folder.png'))
        ico = QtGui.QIcon(icon_path)
        self.setIcon(ico)
        self.setSizeHint(QtCore.QSize(100,35))



class TreeView(QtWidgets.QWidget):
    def __init__(self):
        super(TreeView, self).__init__()
        self.setWindowTitle('QTreeView')

        self.tree_view = QtWidgets.QTreeView()
        self.tree_view.setHeaderHidden(True)
        # self.tree_view.setItemsExpandable( False )
        self.tree_view.setAlternatingRowColors(True)
        self.tree_view.setUniformRowHeights( True )
        self.tree_view.setAnimated(True)

        self.tree_model = QtGui.QStandardItemModel()
        self.root_node = self.tree_model.invisibleRootItem()

        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.main_layout.addWidget(self.tree_view)


        creature = StandardItem('creature')
        muscle= StandardItem('muscle')
        creature.appendRow(muscle)


        self.root_node.appendRow(creature)

        self.tree_view.setModel(self.tree_model)
        self.tree_view.expandAll()
        self.tree_view.doubleClicked.connect(self.getValue)

    def getValue(self, val):
        print(val.data(), val.row(), val.column())


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = TreeView()
    window.show()

    app.exec_()
