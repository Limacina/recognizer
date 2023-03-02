import random
from Transition import Transition as Tr

class Analyser:
    def __init__(self, text):
        self.text = list(text)
        self.current_state = 1
        self.alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ' ', 'a', 'p', 'm']
        self.range = self.alphabet[:-5]
        self.trans = [
            Tr(1, self.alphabet[:2], 2),
            Tr(1, list(self.alphabet[2]), 4),
            Tr(2, self.range, 3),
            Tr(3, list(self.alphabet[-5]), 6),
            Tr(4, self.alphabet[:4], 5),
            Tr(5, list(self.alphabet[-5]), 6),
            Tr(6, self.alphabet[:6], 7),
            Tr(7, self.range, 8),
            Tr(8, list(self.alphabet[-4]), 9),
            Tr(9, self.alphabet[-3:-1], 10),
            Tr(10, list(self.alphabet[-1]), 11)
        ]

    def base_check(self):
        if len(self.text) == 0:
            return 'Empty string? Are you serious?..'
        for i in self.text:
            if i not in self.alphabet:
                return 'Unknown symbol: ' + i
        if len(self.text) != 8:
            return 'Fail...'

    def analyse(self):
        current_input = self.text.pop(0)
        marker = False
        for tr in self.get_possible_transition(self.current_state):
            if current_input in tr.get_transition():
                self.current_state = tr.get_final()
                marker = True
                break
        if not marker:
            return 'Fail...'
        if len(self.text) != 0:
            return self.analyse()
        else:
            return "Match!"

    def get_possible_transition(self, state):
        possible_transitions = []
        for tr in self.trans:
            if tr.get_base() == state:
                possible_transitions.append(tr)
        return possible_transitions

    def get_random(self):
        self.current_state = 1
        self.text = ''
        while self.current_state != 11:
            possible_transitions = self.get_possible_transition(self.current_state)
            trans_number = random.randint(0, len(possible_transitions) - 1)
            self.text += possible_transitions[trans_number].get_random_transition()
            self.current_state = possible_transitions[trans_number].get_final()
        return self.text