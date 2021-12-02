from win10toast import ToastNotifier

class Factory:
    def __init__(self):
        self._halls = []
        self._notifier = ToastNotifier()

    def add_hall(self, hall):
        self._halls.append(hall)
        hall.notifier = self._notifier

    def manage_halls(self):
        for h in self._halls:
            h.manage_machines()

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
