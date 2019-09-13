class Simulation:
    def __init__(self, game):
        self.game = game

    def run(self, number_of_sims):
        for i in number_of_sims:
            self.game.play_ball()
