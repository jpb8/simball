class Simulation:
    def __init__(self, game):
        self.game = game

    def run(self, number_of_sims):
        for i in range(number_of_sims):
            self.game.play_ball()
            home_b = self.game.home_ab
            away_b = self.game.away_ab
            for i in range(self.game.lineup_cnt):
                home_b.store_fpts()
                away_b.store_fpts()
                away_b = away_b.next
                home_b = home_b.next

    def player_outcomes(self):
        outcomes = {
            "team": [],
            "player": [],
            "game": [],
            "fpts": [],
        }
        home_b = self.game.home_ab
        away_b = self.game.away_ab
        for i in range(self.game.lineup_cnt):
            for i, fpts in enumerate(home_b.fpts_collection):
                outcomes["team"].append("home")
                outcomes["player"].append(home_b.name)
                outcomes["game"].append(i)
                outcomes["fpts"].append(fpts)
            for i, fpts in enumerate(away_b.fpts_collection):
                outcomes["team"].append("away")
                outcomes["player"].append(away_b.name)
                outcomes["game"].append(i)
                outcomes["fpts"].append(fpts)
            away_b = away_b.next
            home_b = home_b.next
        return outcomes
