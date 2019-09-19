from .diamond import Diamond


class Game:
    def __init__(self, home_team, away_team, lineup_cnt=9):
        self.score = {"away": [], "home": []}
        self.home_team = home_team # should these be there own Objects?
        self.away_team = away_team # should these be there own Objects?
        self.diamond = Diamond()
        self.lineup_cnt = lineup_cnt
        self.inning = 1
        self.complete = False

    def play_ball(self):
        self.inning = 1
        while self.inning < 10:
            self.half_inning("a")
            self.diamond.clear_bases()
            self.half_inning("h")
            self.diamond.clear_bases()

    def half_inning(self, team):
        if team == "a":
            team_ab = self.away_team
        else:
            team_ab = self.home_team
        outs = 0
        while outs < 3:
            ab = team_ab.rotate_order()
            outcome = ab.ab()
            rbis = 0
            if outcome in ["k", "bbo"]:
                outs += 1
            elif outcome == "home_run":
                rbis = self.diamond.handle_outcome(outcome, ab)
                ab.current_fpts += 10 + (rbis * 2)
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
            team_ab.score += rbis
        self.inning += 0.5
