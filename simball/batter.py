import random


class Batter:
    def __init__(self, pid, name, next_in_order, single=.22, double=.09, triple=.025, home_run=.05,
                 walk=.1, strikeout=.14, bbo=.35):
        self.pid = pid
        self.name = name
        self.next = next_in_order
        self.current_fpts = 0
        self.outcomes = {
            "single": single,
            "double": double,
            "triple": triple,
            "home_run": home_run,
            "walk": walk,
            "k": strikeout,
            "bbo": bbo,
        }
        self.fpts_collection = []

    def ab(self):
        total = sum(v for k, v in self.outcomes.items())
        r = random.uniform(0, total)
        numb = 0
        for k, v in self.outcomes.items():
            if numb + v >= r:
                return k
            numb += v
        assert "ab did not come to an outcome!!!"
