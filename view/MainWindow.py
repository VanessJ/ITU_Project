from view.interface import *
from PySide2 import *
from qt_material import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon(":/prefix/icons/hammer.png"))
        self.setWindowTitle("MM")
        QSizeGrip(self.ui.size_grip)
        self.ui.minimze_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.resize_window_button.clicked.connect(lambda: self.restore_or_maximize_window())


    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.resize_window_button.setIcon(QtGui.QIcon(u":/prefix/icons/albums.png"))
        else:
            self.showMaximized()
            self.ui.resize_window_button.setIcon(QtGui.QIcon(u":/prefix/icons/copy.png"))