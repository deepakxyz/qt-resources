from qtswitch.qt4 import QtGui, QtCore


class CollapsibleWidget(QtGui.QWidget):
    """
    Widget that can be expanded or hidden.
    """
    change_shading_mode = QtCore.Signal(str)
    def __init__(self, widget_name, app=None):
        super(CollapsibleWidget, self).__init__()
        
        self.auto_switch = True
        self.visible = True
        self.widgets = []
        collapse_btn = QtGui.QPushButton('  {0}:'.format(widget_name))

        if app == 'Maya':
            collapse_btn.setStyleSheet("Text-align:left; font: bold")
            collapse_btn.setStyleSheet('background-color: rgb(150, 150, 150); font: bold; text-align: left 18px; color: rgb(50,50,50)')

        elif app == 'Houdini':            
            collapse_btn.setStyleSheet("Text-align:left; font: bold")
            collapse_btn.setStyleSheet('font: bold; text-align: left 18px; color: rgb(50,50,50)')

        window_frame = QtGui.QFrame()
        self.widgets.append(window_frame)

        if app == 'Maya':
            window_frame.setStyleSheet("QPushButton { background-color: rgb(100, 100, 100)}")
            self.setStyleSheet("QFrame {background-color: rgb(80, 80, 80)}");

        if app == 'Houdini':
            self.setStyleSheet("QFrame {  background-color: rgb(225, 225, 225)}")
            #self.setStyleSheet("QFrame { border:1px solid rgb(130, 130, 130);}");

        collapse_btn.clicked.connect(self.change_widget_visibility)
        self.main_widget_layout = QtGui.QVBoxLayout()
        main_layout = QtGui.QVBoxLayout()
        main_layout.addWidget(collapse_btn)
        window_frame.setLayout(self.main_widget_layout)
        main_layout.addWidget(window_frame)

        self.setLayout(main_layout)        

    def create_horizontal_line(self):
        """
        Creates a horizontal line using a QFrame.

        :return: A horizontal line.
        :rtype: QFrame
        """
        h_line = QtGui.QFrame()
        h_line.setFrameShape(QtGui.QFrame.HLine)
        h_line.setFrameShadow(QtGui.QFrame.Plain)
        return h_line

    def get_all_widgets(self, layout=None):
        """
        Get all the widgets in the widget layout and assigns it to a variable.

        :parameters:
            layout: QLayout
                (Optional) The layout to get the widgets for. Default is the main layout.

        """
        if not layout:
            layout = self.main_widget_layout
        for i in range (layout.count()):
            child = layout.itemAt(i)
            if child.widget() is not None:
                self.widgets.append(child.widget())
            elif child.layout() is not None:
                self.get_all_widgets(child.layout())

    def change_widget_visibility(self):
        """ Turn on/off the widget visibility """    
        self.visible = not self.visible  
        for widget in self.widgets: widget.setVisible(self.visible)

    def update_neighbours_and_corners(self, neighbour_distance, keep_corners_linked):
        """
        Updates the variables which determin the neighbour distance and whether to keep
        corners lined.

        :parameters:
            neighbour_distance: float
                The maximum distance between neighbouring windows.
            keep_corners_linked: bool
                Wheter to keep corner windows connected or not.
        """
        self.neighbour_distance = neighbour_distance
        self.keep_corners_linked = keep_corners_linked