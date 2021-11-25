from threading import Thread
from model.Machine import Machine
from model.Machine_group import MachineGroup
from model.Simulation import Simulation
from view.MainWindow import MainWindow
import time
import schedule
import sys
import os
from view.interface import *
from PySide2 import *
from qt_material import *


def set_labels(gui_window, machine):
    gui_window.ui.label_name.setText(machine.identification)
    gui_window.ui.label_temperature.setText(str(machine.temperature))
    gui_window.ui.label_nas.setText(str(machine.nas))
    gui_window.ui.label_time.setText(str(machine.runtime))


if __name__ == "__main__":
    schedule.every(5).seconds.do(lambda: sim.operating_update())
    schedule.every(1).seconds.do(lambda: sim.stopped_update())
    schedule.every(10).seconds.do(lambda: sim.not_filtering_update())
    schedule.every(1).seconds.do(lambda: sim.filtering_update())
    schedule.every(1).seconds.do(lambda: sim.runtime_update())

    machine1 = Machine("M1")
    machine2 = Machine("M2")
    machine3 = Machine("M3")

    group_all = MachineGroup("Hall A")
    group_all.add_machine(machine1)
    group_all.add_machine(machine2)
    group_all.add_machine(machine3)

    sim = Simulation(group_all.machines)
    sim.start_all()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.stackedWidget.setCurrentWidget(window.ui.main_menu_page)
    window.show()
    while True:
        QApplication.processEvents()
        schedule.run_pending()
        time.sleep(0.05)

    app.exec_()








