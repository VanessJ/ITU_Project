
from PyQt5 import QtCore
from PyQt5 import QtGui
from pyqt5_plugins.examplebuttonplugin import QtGui

from view.MachineButton import MachineButton
from view.HallCheckBox import HallCheckBox
from model.Machine import Machine
from model.Hall import Hall
from view.interface import *
from PySide2 import *
from qt_material import *


class MainWindow(QMainWindow):
    def __init__(self, factory):
        QMainWindow.__init__(self)
        self._factory = factory
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
        self.ui.home_button.clicked.connect(lambda: self.reroute(self.ui.main_menu_page))
        self.ui.halls_button.clicked.connect(lambda: self.halls_page())
        self.ui.machines_button.clicked.connect(lambda: self.reroute(self.machines_page()))
        self.ui.stats_button.clicked.connect(lambda: self.reroute(self.ui.tests_page))
        self.ui.settings_button.clicked.connect(lambda: self.reroute(self.ui.settings_page))

        self.ui.main_menu_halls_button.clicked.connect(lambda: self.halls_page())
        self.ui.main_menu_machines_button.clicked.connect(lambda: self.reroute(self.machines_page()))
        self.ui.main_menu_stats_button.clicked.connect(lambda: self.reroute(self.ui.tests_page))
        self.ui.main_menu_settings_button.clicked.connect(lambda: self.reroute(self.ui.settings_page))
        self.ui.add_hall_button.clicked.connect(lambda: self.add_hall_page())
        self.ui.add_machine_button.clicked.connect(lambda: self.add_machine_page())
        self.ui.add_machine_back_button.clicked.connect(lambda: self.machines_page())
        self.ui.add_hall_back_button.clicked.connect(lambda: self.halls_page())
        self.ui.settings_back_button.clicked.connect(lambda: self.reroute(self.back_route))
        self.ui.statistics_back_button.clicked.connect(lambda: self.reroute(self.back_route))
        self.ui.machine_info_back_button.clicked.connect(lambda: self.machines_page())

        # halls search bar
        self.ui.search_bar_2.setPlaceholderText("Search")
        self.ui.search_bar_2.textChanged.connect(self.find_hall)

        # machines search bar
        self.ui.search_bar_3.setPlaceholderText("Search")
        self.ui.search_bar_3.textChanged.connect(lambda: self.find_machine())

        # status bar text updating
        self.ui.home_button.clicked.connect(lambda: self.clicked_button_bar("Welcome to Main Menu..."))
        self.ui.halls_button.clicked.connect(lambda: self.clicked_button_bar("Here you can find all halls and info about them..."))
        self.ui.machines_button.clicked.connect(lambda: self.clicked_button_bar("Table of all machines..."))
        self.ui.stats_button.clicked.connect(lambda: self.clicked_button_bar("Statistics of all machines combined..."))
        self.ui.settings_button.clicked.connect(lambda: self.clicked_button_bar("Welcome to Settings page..."))
        self.ui.add_hall_button.clicked.connect(lambda: self.clicked_button_bar("Fill out the form and click CONFIRM to add a new hall..."))
        self.ui.add_machine_button.clicked.connect(lambda: self.clicked_button_bar("Fill out the form and click CONFIRM to add a new machine..."))
        self.ui.machine_info_back_button.clicked.connect(lambda: self.clicked_button_bar("Table of all machines..."))
        self.ui.add_hall_back_button.clicked.connect(lambda: self.clicked_button_bar("Here you can find all halls and info about them..."))
        self.ui.add_machine_back_button.clicked.connect(lambda: self.clicked_button_bar("Table of all machines..."))
        self.ui.confirm_add_button_machine.clicked.connect(lambda: self.clicked_button_bar("Machine sucessfully added..."))
        self.ui.confirm_add_button.clicked.connect(lambda: self.clicked_button_bar("Hall sucessfully added..."))
        self.ui.main_menu_halls_button.clicked.connect(lambda: self.clicked_button_bar("Here you can find all halls and info about them..."))
        self.ui.main_menu_machines_button.clicked.connect(lambda: self.clicked_button_bar("Table of all machines..."))
        self.ui.main_menu_stats_button.clicked.connect(lambda: self.clicked_button_bar("Statistics of all machines combined..."))
        self.ui.main_menu_settings_button.clicked.connect(lambda: self.clicked_button_bar("Welcome to Settings page..."))


        def move_window(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header_frame.mouseMoveEvent = move_window

        self.ui.menu_button.clicked.connect(lambda: self.slideLeftMenu())

    def add_hall_page(self):
        self.reroute(self.ui.add_hall_form)
        self.ui.confirm_add_button.clicked.connect(lambda: self.create_hall())

    def add_machine_page(self):
        self.reroute(self.ui.add_machine_form)
        self.ui.confirm_add_button_machine.clicked.connect(lambda: self.create_machine())

    def create_hall(self):
        hall_name = self.ui.add_hall_name.text()
        hall_city = self.ui.add_hall_city.text()
        hall_street = self.ui.add_hall_street.text()
        hall_id = self.ui.add_hall_id.text()
        name = hall_name + " " + hall_id
        address = hall_city + hall_street
        hall = Hall(name, address)
        self._factory.add_hall(hall)
        self.halls_page()

    def create_machine(self):
        machine_name = self.ui.add_machine_name.text()
        machine_id = self.ui.add_machine_id.text()
        machine_sensor = self.ui.add_machine_sensor.text()
        name = machine_name + " " + machine_id
        machine = Machine(name)
        machine.sensor = machine_sensor
        self._factory.monitored_hall().add_machine(machine)
        self.machines_page()


    def find_machine(self):
        name = self.ui.search_bar_3.text().lower()
        for row in range(self.ui.machines_table.rowCount()):
            item = self.ui.machines_table.item(row, 0)
            self.ui.machines_table.setRowHidden(row, name not in item.text().lower())

    def find_hall(self):
        name = self.ui.search_bar_2.text().lower()
        for row in range(self.ui.halls_table.rowCount()):
            item = self.ui.halls_table.item(row, 0)
            self.ui.halls_table.setRowHidden(row, name not in item.text().lower())

    def halls_page(self):
        self.reroute(self.ui.halls_list_page)
        self.print_halls_table()

    def machines_page(self):
        self.reroute(self.ui.machines_list_page)
        hall = self._factory.monitored_hall()
        self.print_machines_table(hall)

    def print_machines_table(self, hall):
        self.ui.machines_table.setRowCount(0)
        self.ui.machines_table.verticalHeader().hide()

        for machine in hall.machines:
            row_pos = self.ui.machines_table.rowCount()
            button = MachineButton(machine)
            button.setText("Details")

            self.ui.machines_table.insertRow(row_pos)
            self.ui.machines_table.setItem(row_pos, 0, QTableWidgetItem(machine.identification))
            if machine.is_operating():
                self.ui.machines_table.setItem(row_pos, 1, QTableWidgetItem("Operating"))
            else:
                self.ui.machines_table.setItem(row_pos, 1, QTableWidgetItem("Not operating"))
            self.ui.machines_table.setItem(row_pos, 2, QTableWidgetItem(str(machine.temperature)))
            self.ui.machines_table.setItem(row_pos, 3, QTableWidgetItem(str(machine.nas)))
            self.ui.machines_table.setCellWidget(row_pos, 4, button)
            button.clicked.connect(lambda: self.machine_button_pressed())

    def machine_button_pressed(self):
        button = self.focusWidget()
        machine = button.machine
        self.machine_info_page(machine)



    def machine_info_page(self, machine):
        self.reroute(self.ui.machine_info_page)
        self.ui.m_info_id.setText(machine.identification)
        self.ui.m_info_hall.setText(self._factory.monitored_hall().name)
        self.ui.m_info_sensor.setText(machine.sensor)



    def print_halls_table(self):
        self.ui.halls_table.setRowCount(0)
        self.ui.halls_table.verticalHeader().hide()

        for hall in self._factory.halls:
            check_box = HallCheckBox(hall)
            row_pos = self.ui.halls_table.rowCount()
            self.ui.halls_table.insertRow(row_pos)
            self.ui.halls_table.setItem(row_pos, 0, QTableWidgetItem(hall.name))
            self.ui.halls_table.setItem(row_pos, 1, QTableWidgetItem(str(len(hall.machines))))
            self.ui.halls_table.setItem(row_pos, 2, QTableWidgetItem(hall.address))
            self.ui.halls_table.setCellWidget(row_pos, 3, check_box)
            if hall.monitored:
                check_box.setChecked(True)

            check_box.stateChanged.connect(lambda: self.handle_halls_checkbox())

    def handle_halls_checkbox(self):
        check_box = self.focusWidget()
        if check_box.isChecked():
            self._factory.monitor(check_box.hall)
            self.print_halls_table()

    def halls_checkbox(self, checkbox, hall):
        if checkbox.isChecked():
            self._factory.monitor(hall)
            self.print_halls_table()

    def slideLeftMenu(self):
        width = self.ui.left_menu_frame.width()

        if width == 40:
            newWidth = 155
        else:
            newWidth = 40

        self.animation = QPropertyAnimation(self.ui.left_menu_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

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




    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


    def clicked_button_bar(self, text):
        self.ui.status_bar.setText(text)
