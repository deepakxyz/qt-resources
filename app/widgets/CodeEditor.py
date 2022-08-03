
from PySide2 import QtCore
from PySide2 import QtWidgets




    

        

class CodeEditor(QtWidgets.QPlainTextEdit):
    

    def __init__(self):
        super(CodeEditor, self).__init__()
        

    # def keyPressEvent(self, key_event):
    #     key = key_event.key()
    #     ctrl = key_event.modifiers() == QtCore .Qt.ControlModifier
    #     if ctrl:
    #         if key == QtCore.Qt.Key_Enter or key == QtCore.Qt.Key_Return:
    #             self.value = (self.toPlainText())
    #             print(self.value)
    #             self.clear()

    #     super(CodeEditor, self).keyPressEvent(key_event)
    
