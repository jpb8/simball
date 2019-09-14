class Game:
    def __init__(self, home_ab, away_ab, diamond, lineup_cnt=9):
        self.score = {"away": [], "home": []}
        self.home_ab = home_ab
        self.away_ab = away_ab
        self.home_score = 0
        self.away_score = 0
        self.diamond = diamond
        self.lineup_cnt = lineup_cnt
        self.inning = 1
        self.complete = False

    def generate_outcome_percentages(self):
        pass

    def play_ball(self):
        self.inning = 1
        while self.inning < 10:
            self.away_ab = self.half_inning(self.away_ab)
            self.diamond.clear_bases()
            self.home_ab = self.half_inning(self.home_ab)
            self.diamond.clear_bases()

    def half_inning(self, ab):
        outs = 0
        while outs < 3:
            outcome = ab.ab()
            if outcome in ["k", "bbo"]:
                outs += 1
            elif outcome == "home_run":
                rbis = self.diamond.handle_outcome(outcome, ab)
                ab.current_fpts += 14 + (rbis * 2)
            elif outcome == "triple":
                rbis = self.diamond.handle_outcome(outcome, ab)
                ab.current_fpts += 8 + (rbis * 2)
            elif outcome == "double":
                rbis = self.diamond.handle_outcome(outcome, ab)
                ab.current_fpts += 5 + (rbis * 2)
            elif outcome == "single":
                rbis = self.diamond.handle_outcome(outcome, ab)
                ab.current_fpts += 3 + (rbis * 2)
            elif outcome == "walk":
                rbis = self.diamond.handle_outcome(outcome, ab)
                ab.current_fpts += 2 + (rbis * 2)
            else:
                print("IDK", ab.name, outcome)
            ab = ab.next
        self.inning += 0.5
        return ab
