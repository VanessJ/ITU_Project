
from PyQt5 import QtCore
from PyQt5 import QtGui
from pyqt5_plugins.examplebuttonplugin import QtGui

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
        self.back_route = self.ui.main_menu_page
        QSizeGrip(self.ui.size_grip)
        self.ui.minimze_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.resize_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        # navigation
        self.ui.halls_button.clicked.connect(lambda: self.reroute(self.ui.halls_list_page))
        self.ui.machines_button.clicked.connect(lambda: self.reroute(self.ui.machines_list_page))
        self.ui.stats_button.clicked.connect(lambda: self.reroute(self.ui.tests_page))
        self.ui.settings_button.clicked.connect(lambda: self.reroute(self.ui.settings_page))

        self.ui.main_menu_halls_button.clicked.connect(lambda: self.reroute(self.ui.halls_list_page))
        self.ui.main_menu_machines_button.clicked.connect(lambda: self.reroute(self.ui.machines_list_page))
        self.ui.main_menu_stat_button.clicked.connect(lambda: self.reroute(self.ui.tests_page))
        self.ui.main_menu_settings_button.clicked.connect(lambda: self.reroute(self.ui.settings_page))
        self.ui.add_hall_button.clicked.connect(lambda: self.reroute(self.ui.add_hall_form))
        self.ui.add_machine_button.clicked.connect(lambda: self.reroute(self.ui.add_machine_form))
        self.ui.add_machine_back_button.clicked.connect(lambda: self.reroute(self.back_route))
        self.ui.add_hall_back_button.clicked.connect(lambda: self.reroute(self.back_route))
        self.ui.settings_back_button.clicked.connect(lambda: self.reroute(self.back_route))
        self.ui.statistics_back_button.clicked.connect(lambda: self.reroute(self.back_route))
        self.ui.machine_info_back_button.clicked.connect(lambda: self.reroute(self.back_route))

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.resize_window_button.setIcon(QtGui.QIcon(u":/prefix/icons/albums.png"))
        else:
            self.showMaximized()
            self.ui.resize_window_button.setIcon(QtGui.QIcon(u":/prefix/icons/copy.png"))

    def reroute(self, route):
        previous_page = self.ui.stackedWidget.currentWidget()
        self.ui.stackedWidget.setCurrentWidget(route)
        if previous_page is not self.ui.stackedWidget.currentWidget():
            self.back_route = previous_page




