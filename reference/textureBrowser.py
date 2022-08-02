import sys
import os
from PyQt4 import QtGui, QtCore



class ImageButton(QtGui.QAbstractButton):
    """
    Button which displays a windowbox texture icon and store the path to the full
    res image.
    """
    def __init__(self, image_neutral_path, image_hover, image_down, parent=None):
        super(ImageButton, self).__init__()        
        self.get_and_set_full_res_image_path(image_neutral_path)
        self.neutral_image = QtGui.QPixmap(image_neutral_path)
        self.hover_image = QtGui.QPixmap(image_hover)
        self.down_image = QtGui.QPixmap(image_down)

    def get_and_set_full_res_image_path(self, icon_path):
        """
        Gets the path for the full res texture
        """
        self.image_path = icon_path.replace('/icons/', '/houdini/').replace('.jpg', '.rat')

    def get_image_path(self):
        return self.image_path

    def paintEvent(self, event):
        
        if self.underMouse():
            pixmap = self.hover_image 
        else:
            pixmap = self.neutral_image
        if self.isDown():
            pixmap = self.down_image

        painter = QtGui.QPainter(self)
        painter.drawPixmap(event.rect(), pixmap)

    def sizeHint(self):
        return self.neutral_image.size()



class ImageBrowser(QtGui.QWidget):
    
    def __init__(self):
        super(ImageBrowser, self).__init__()        
        self.initUI()
        
    def initUI(self):   

        folder_path_label = QtGui.QLabel('Folder Path')
        self.folder_browser = QtGui.QLineEdit('/jobs/LIBRARY/3D/WAREHOUSE/WINDOWBOX/rooms/hogwarts/icons')
        folder_browser_btn = QtGui.QPushButton('Browse')

        image_scroll_widget = QtGui.QWidget()
        self.image_icon_layout = QtGui.QGridLayout(image_scroll_widget)

        self.folder_browser.textChanged.connect(self.add_image_icons)
        folder_browser_btn.clicked.connect(self.browse_folders)

        main_layout = QtGui.QVBoxLayout()
        file_browser_layout = QtGui.QHBoxLayout()
        file_browser_layout.addWidget(folder_path_label)
        file_browser_layout.addWidget(self.folder_browser)
        file_browser_layout.addWidget(folder_browser_btn)
        main_layout.addLayout(file_browser_layout)
        scroll_area_0 = QtGui.QScrollArea()
        scroll_area_0.setWidget(image_scroll_widget)
        scroll_area_0.setWidgetResizable(True)
        scroll_area_0.setMinimumSize((5 * 200) + 70, 800) 
        main_layout.addWidget(scroll_area_0)
        self.setLayout(main_layout)    
        
        self.setWindowTitle('Texture Browser')    
        self.add_image_icons()
        self.show()

    def add_image_icons(self):
        icons_path = self.folder_browser.text()
        if not os.path.exists(icons_path):
            return

        self.clear_images()
        
        icons = [image for image in os.listdir(icons_path) if 'room.' in image and image.endswith('jpg')]
        rows = 5
        current_row = -1
        for i in range(len(icons)):
            if i % rows == 0:
                current_row += 1

            index = (current_row * rows) + (i % rows)
            image_neutral_path = '{0}/room.{1}.jpg'.format(icons_path, index)
            image_hover_path = '{0}/room_hover.{1}.jpg'.format(icons_path, index)
            image_down_path = '{0}/room_down.{1}.jpg'.format(icons_path, index)
            image_btn = ImageButton(image_neutral_path, image_hover_path, image_down_path)
            self.image_icon_layout.addWidget(image_btn, current_row, (i % rows))    
            image_btn.clicked.connect(self.set_window_texture)

    def browse_folders(self):
        folder_path = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.folder_browser.setText(folder_path)

    def set_window_texture(self):
        image_path = self.sender().get_image_path()
        print image_path

    def clear_images(self):
        for i in reversed(range(self.image_icon_layout.count())): 
            self.image_icon_layout.itemAt(i).widget().setParent(None)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = ImageBrowser()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()