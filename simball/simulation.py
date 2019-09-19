class Simulation:
    def __init__(self, game):
        self.game = game

    def run(self, number_of_sims):
        for i in range(number_of_sims):
            self.game.play_ball()
            self.game.home_team.store_fpts()
            self.game.away_team.store_fpts()

    def player_outcomes(self):
        outcomes = {
            "team": [],
            "player": [],
            "game": [],
            "fpts": [],
        }
        for j, batter in enumerate(self.game.home_team.lineup):
            for i, fpts in enumerate(batter.fpts_collection):
                outcomes["team"].append("home")
                outcomes["player"].append(batter.name)
                outcomes["game"].append(i)
                outcomes["fpts"].append(fpts)
        for j, batter in enumerate(self.game.away_team.lineup):
            print(batter.name)
            for i, fpts in enumerate(batter.fpts_collection):
                outcomes["team"].append("away")
                outcomes["player"].append(batter.name)
                outcomes["game"].append(i)
                outcomes["fpts"].append(fpts)
        return outcomes
