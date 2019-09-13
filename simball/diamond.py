class Diamond:
    def __init__(self, ab):
        self.ab = ab
        self.first = False
        self.second = False
        self.third = False

    def handle_outcome(self, outcome):
        if outcome in ["bb", "single"]:
            pass

