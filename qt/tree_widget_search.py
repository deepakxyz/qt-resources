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
        # self.tree_widget

        # MAIN LAYOUT
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.search_le)
        self.main_layout.addWidget(self.tree_widget)

        self.item_dict = {
            "cfx":{
                "playblast",
                "publish_otla", 
                "cfx_rig"
            },
            "fx":{
                "pyro_setup", 
                "rain_setup",
                "vdb_cloud"
            }, 
            "animation":{
                "blockout animation", 
                "refined animation"
            }
        }

        self.addItem(self.item_dict)




    def addItem(self, item_dict):
        for item in item_dict.keys():
            new_item = QtWidgets.QTreeWidgetItem()
            # new_item.setCheckState(0, QtCore.Qt.CheckState())
            widget = CustomTreeWidgetItem(item)

            self.tree_widget.addTopLevelItem(new_item)
            self.tree_widget.setItemWidget(new_item,0, widget)

            for child in item_dict[item]:
                child_item = QtWidgets.QTreeWidgetItem([child])
                widget = CustomTreeWidgetItem(child)
                
                child_item.setCheckState(0, QtCore.Qt.CheckState())
                new_item.addChild(child_item)

                # self.tree_widget.addTopLevelItem(new_item)
                # self.tree_widget.setItemWidget(new_item,0, widget)



class CustomTreeWidgetItem(QtWidgets.QWidget):
    def __init__(self, lable_text):
        super(CustomTreeWidgetItem, self).__init__()

        self.text = lable_text
        lable = QtWidgets.QLabel(lable_text)
        self.chkb = QtWidgets.QCheckBox()

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(lable)
        layout.addStretch()
        layout.addWidget(self.chkb)
        self.setLayout(layout)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = TreeSearch()
    window.show()

    app.exec_()
