import random


class Diamond:
    def __init__(self):
        self.bases = [False, False, False]
        self.outcome_translator = {
            "single": 1,
            "double": 2,
            "triple": 3,
            "home_run": 4,
            "walk": 1,
        }

    def handle_outcome(self, outcome, batter):
        """
        Handles the Outcome of an At Bat
        :param outcome: The outcome of the At Bat
        :param batter: The Batter object who hs responsible for the outcome
        :return: Total Number of RBIs as int
        """
        # TODO: Add in BaseRunning probabilities (Double Play, 1-3 on a Single, 1-H on a double ect.)
        total_bases = self.outcome_translator[outcome]
        rbis = 0
        # account for Extra Taken Base (XTB%)
        if outcome in ["single", "double"] and random.randint(1,100) < 50:
            score = self.bases.pop()
            self.bases.insert(0, False)
            if score:
                rbis += 1
                score.current_fpts += 2
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




