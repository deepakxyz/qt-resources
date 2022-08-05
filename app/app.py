from PySide2 import QtWidgets, QtGui, QtCore,  QtUiTools
from PySide2.QtWidgets import QApplication
import sys
from utils import resource_path, ui_path
# import CodeEditor
from widgets import FlowLayout, PublishWidget

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
        self.add_collapasable()
        self.add_flow_layout_tab()

    def widgetAdditional(self):
        ico = QtGui.QIcon(self.temp_icon_path) 
        self.ui.tabWidget.setTabIcon(1,ico)
        self.ui.tabWidget.setTabIcon(0,ico)


        # CODE LAYOUT
        # self.code = None
        self.code_editor = CodeEditor()
        self.code_editor.setPlaceholderText('Query')
        self.ui.codeVertical_layout.addWidget(self.code_editor)

    def keyPressEvent(self, e):
        key = e.key()

        widget = QtWidgets.QApplication.focusWidget()
        if widget == self.code_editor:
            if key == QtCore.Qt.Key_Enter or key == QtCore.Qt.Key_Return:
                self.value = self.code_editor.toPlainText()
                self.code_editor.clear()
                self.parse()
                self.appendToTextBrowser()


    def appendToTextBrowser(self):
        style = '''
        <style>
            p{
                color:#439151;
            }
            br { 
                display:block;
                margin-bottom:1px;
                line-height:1px;
            }
        </style>
        '''
        data = f"""{style}>> {self.value} 
        <p>{self.parse_output}</p>
        <br>
        """
        self.ui.textBrowser.insertHtml(data)
        self.ui.textBrowser.moveCursor(QtGui.QTextCursor.End)

    def parse(self):
        if self.value == "all_shows":

            self.parse_output = '''
            File "<string>", line 1, in <module>
            NameError: name 'asdfdsf' is not defined
            '''
        else:
            self.parse_output = "None"

    def add_collapasable(self):
        self.c_w_1 = CollapsibleWidget('Image Gate Resolution')
        self.c_w_2 = CollapsibleWidget('Render Global Setting')

        self.ui.pageLayout.addWidget(self.c_w_1)
        self.ui.pageLayout.addWidget(self.c_w_2)


        self.btn = QtWidgets.QPushButton('Test')
        self.btn1 = QtWidgets.QPushButton('PinkMan')
        self.c_w_1.add_widget(self.btn)

        self.c_w_3 = CollapsibleWidget('Hould Out setting.')
        v = QtWidgets.QLabel('ValueCheck')
        x = QtWidgets.QLabel('Main Itme')
        self.c_w_3.add_widget(v)
        self.c_w_3.add_widget(x)

        self.c_w_1.add_widget(self.c_w_3)

        self.formLayout = QtWidgets.QFormLayout()
        h = QtWidgets.QLabel('Dexter')
        k = QtWidgets.QLineEdit()
        j = QtWidgets.QCheckBox('Pinkam.tv')
        self.formLayout.addRow('Name', h)
        self.formLayout.addRow('Your Name', k)
        self.formLayout.addRow('Website',j )

        self.c_w_2.add_layout(self.formLayout)

    # FLOW LAYOUT
    def add_flow_layout_tab(self):
        self.flow_layout = FlowLayout.FlowLayout(self.ui.tab_2_scroll)

        self.flow_layout.addWidget(PublishWidget.PublishWidget('char_greyman_body_lod100_mdl'))
        self.flow_layout.addWidget(PublishWidget.PublishWidget('char_greyman_body_lod100_mdl'))
        self.flow_layout.addWidget(PublishWidget.PublishWidget('char_greyman_body_lod100_mdl'))
        self.flow_layout.addWidget(PublishWidget.PublishWidget('char_greyman_body_lod100_mdl'))
        self.flow_layout.addWidget(PublishWidget.PublishWidget('char_greyman_body_lod100_mdl'))
       















class CodeEditor(QtWidgets.QPlainTextEdit):
    

    def __init__(self):
        super(CodeEditor, self).__init__()
        

class CollapsibleHeader(QtWidgets.QWidget):

    clicked = QtCore.Signal()

    def __init__(self, text, parent=None):
        super(CollapsibleHeader, self).__init__(parent)

        f_path = "Z:\\dev\\qt_resources\\app\\resources\\my_icons\\forward_arrow.png"
        self.FORWARDARROW = QtGui.QPixmap(f_path)

        d_path = "Z:\\dev\\qt_resources\\app\\resources\\my_icons\\dropdown.png"
        self.DOWNARROW = QtGui.QPixmap(d_path)

        self.set_background_color()
        self.icon_lable = QtWidgets.QLabel()
        self.icon_lable.setFixedWidth(self.FORWARDARROW.width())
        self.icon_lable.setFixedHeight(25)

        self.text_la = QtWidgets.QLabel()
        self.text_la.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.main_layout.setContentsMargins(4,4,4,4)
        self.main_layout.addWidget(self.icon_lable)
        self.main_layout.addWidget(self.text_la)

        self.set_text(text)
        self.set_expanded(False)

    def set_text(self,text):
        self.text_la.setText(f"<b>{text}</b>")

    def set_background_color(self):
        self.setStyleSheet("""
        QWidget { 
            background:#383838;
            
        }
        """)

    def is_expanded(self):
        return self._expanded

    def set_expanded(self, expanded):
        self._expanded = expanded

        if(self._expanded):
            # self.icon_lable.setText('V')
            self.icon_lable.setPixmap(self.DOWNARROW)
        else:
            self.icon_lable.setPixmap(self.FORWARDARROW)

    def mouseReleaseEvent(self, event) -> None:
        self.clicked.emit() 



class CollapsibleWidget(QtWidgets.QWidget):
    def __init__(self, text, parent=None):
        super(CollapsibleWidget, self).__init__(parent)


        self.header_wgt = CollapsibleHeader(text)
        self.header_wgt.clicked.connect(self.on_header_clicked)

        self.body_wgt = QtWidgets.QWidget()
        self.body_wgt.setObjectName('bodyWidget')
        self.body_wgt.setStyleSheet('''
        QWidget#bodyWidget {
            background:#2e2e2e;
            border: 1px solid #404040;
            border-top:none;
        }
        ''')
        self.body_layout = QtWidgets.QVBoxLayout(self.body_wgt)
        self.body_layout.setContentsMargins(4,2,4,2)
        self.body_layout.setSpacing(4)

        # self.body_scroll_area = QtWidgets.QScrollArea()
        # self.body_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.body_scroll_area.setWidgetResizable(True)
        # self.body_scroll_area.setWidget(self.body_wgt)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.addWidget(self.header_wgt)
        self.main_layout.addWidget(self.body_wgt)

        self.set_expanded(False)

    def add_widget(self, widget):
        self.body_layout.addWidget(widget)
    
    def add_layout(self,layout):
        self.body_layout.addLayout(layout)

    def set_expanded(self, expanded):
        self.header_wgt.set_expanded(expanded)
        self.body_wgt.setVisible(expanded)

    def on_header_clicked(self):
        self.set_expanded(not self.header_wgt.is_expanded())

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    style_file_path = resource_path('style.qss')
        
    style_file = QtCore.QFile(style_file_path)
    style_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(style_file)
    app.setStyleSheet(stream.readAll())

    window.show()
    sys.exit(app.exec_())