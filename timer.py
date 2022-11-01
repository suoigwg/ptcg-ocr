import time


class Timer:

    def __init__(self):
        self.last_phase_start = time.time()
        self.last_phase = "INITIALIZED"
        self.all_phases = dict()

    def start_new_phase(self, phase: str):
        print("starting new phase {}".format(phase))
        now = time.time()
        self.all_phases[self.last_phase] = now - self.last_phase_start
        self.last_phase_start = now
        self.last_phase = phase

    def summary(self):
        for phase, time_spent in self.all_phases.items():
            print("phase {} took {} seconds".format(phase, time_spent))
