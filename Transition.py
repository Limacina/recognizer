import random

class Transition:
    def __init__(self, base, trans, fin):
        self.base_state = base
        self.transition = trans
        self.final_state = fin

    def get_base(self):
        return self.base_state

    def get_transition(self):
        return self.transition

    def get_random_transition(self):
        if len(self.transition) == 0:
            return str(self.transition[0])
        else:
            return str(self.transition[random.randint(0, len(self.transition) - 1)])

    def get_final(self):
        return self.final_state