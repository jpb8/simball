class Diamond:
    def __init__(self):
        self.bases = [False, False, False]
        self.outcome_translator = {
            "single": 1,
            "double": 2,
            "triple": 3,
            "home_run": 3,
            "walk": 1,
        }

    def handle_outcome(self, outcome, batter):
        total_bases = self.outcome_translator[outcome]
        rbis = 0
        for base in range(total_bases):
            score = self.bases.pop()
            if score:
                rbis += 1
                score.current_fpts += 2
            self.bases.insert(0, batter)
            batter = False
        return rbis

    def clear_bases(self):
        self.bases = [False, False, False]




