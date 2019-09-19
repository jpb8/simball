class Team:
    def __init__(self, name, lineup):
        self.name = name
        self.score = 0
        self.lineup = lineup

    def store_fpts(self):
        for batter in self.lineup:
            batter.store_fpts()

    def rotate_order(self):
        ab = self.lineup.pop(0)
        self.lineup.append(ab)
        return ab
