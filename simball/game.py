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
        while self.inning < 10:
            self.away_ab = self.half_inning(self.away_ab)
            self.home_ab = self.half_inning(self.home_ab)
        print("game")

    def half_inning(self, ab):
        outs = 0
        while outs < 3:
            outcome = ab.ab()
            if outcome in ["k", "bbo"]:
                print("out", ab.name, outcome)
                outs += 1
            elif outcome == "home_run":
                print("home_run", ab.name, outcome)
            elif outcome == "triple":
                print("triple", ab.name, outcome)
            elif outcome == "double":
                print("double", ab.name, outcome)
            elif outcome == "single":
                print("single", ab.name, outcome)
            elif outcome == "walk":
                print("walk", ab.name, outcome)
            else:
                print("IDK", ab.name, outcome)
            ab = ab.next
        self.inning += 0.5
        print(self.inning)
        return ab
