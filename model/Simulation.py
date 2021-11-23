import random

class Simulation:

    def __init__(self, machine_group):
        self._machine_group = machine_group

    def start_all(self):
        for machine in self._machine_group:
            machine.turn_on()

    # updates temperatures of currently operating machines
    def operating_update(self):
        for machine in self._machine_group:
            if machine.is_operating():
                tmp_change = random.randint(1, 5)
                machine.temperature = machine.temperature + tmp_change
                if machine.temperature > 120:
                    machine.temperature = 120

    def runtime_update(self):
        for machine in self._machine_group:
            if machine.is_operating():
                machine.runtime += 1

    # updates temperatures of currently stopped machines
    def stopped_update(self):
        for machine in self._machine_group:
            if machine.is_operating() is False:
                tmp_change = random.randint(1, 3)
                machine.temperature = machine.temperature - tmp_change
                if machine.temperature < 0:
                    machine.temperature = 0
        machine.runtime = 0

    # updates nas values of currently filtering machines
    def filtering_update(self):
        for machine in self._machine_group:
            if machine.is_filtering():
                nas_change = random.randint(0, 2)
                machine.nas = machine.nas - nas_change
                if machine.nas < 0:
                    machine.nas = 0

    # updates nas values of not filtering machines
    def not_filtering_update(self):
        for machine in self._machine_group:
            if machine.is_filtering() is False:
                nas_change = random.randint(0, 2)
                machine.nas = machine.nas + nas_change
                if machine.nas > 12:
                    machine.nas = 12







