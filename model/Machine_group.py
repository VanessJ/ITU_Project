
class MachineGroup:

    def __init__(self, name):
        self._name = name
        self._machines = []

    # name getter
    @property
    def name(self):
        return self._name

    # machines getter
    @property
    def machines(self):
        return self._machines

    @name.setter
    def name(self, name):
        self._name = name

    # selects machine from group by id
    def get_by_id(self, identification):
        for machine in self._machines:
            if machine.identification == identification:
                return machine
        return None

    def add_machine(self, machine):
        self._machines.append(machine)

    def print_values(self):
        for machine in self._machines:
            print(machine.identification)
            if machine.is_operating():
                print("\tCurrently operating")
            if machine.is_filtering():
                print("\tCurrently filtering")
            print("\tTemperature: " + str(machine.temperature) + "°C")
            if machine.is_operating() and machine.temperature >= 120:
                print("\tStopping operation")
                machine.turn_off()
            if machine.is_operating() is False and machine.temperature <= 50:
                print("\tTurning on")
                machine.turn_on()
            print("\tNAS value: " + str(machine.nas))
            if machine.is_filtering() and machine.nas <= 3:
                print("\tStopping filtration")
                machine.stop_filtering()
            if machine.is_filtering() is False and machine.nas >= 12:
                print("\tStarting filtration")
                machine.filter()
            print("")


