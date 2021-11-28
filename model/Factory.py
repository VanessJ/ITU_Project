class Factory:
    def __init__(self):
        self._halls = []

    def add_hall(self, hall):
        self._halls.append(hall)

    def get_machine(self, machine):
        hall = self.monitored_hall()
        machine = hall.get_by_id(machine.identification)

    def monitor(self, hall):
        for h in self._halls:
            h.stop_monitoring()
        for h in self._halls:
            if h is hall:
                h.monitor()

    def monitored_hall(self):
        for h in self._halls:
            if h.monitored:
                return h
    @property
    def halls(self):
        return self._halls
