from simball import Batter, Game, Diamond, Simulation

hp1 = Batter(1, "home batter 8", None)
hp2 = Batter(2, "home batter 7", hp1)
hp3 = Batter(2, "home batter 6", hp2)
hp4 = Batter(2, "home batter 5", hp3)
hp5 = Batter(2, "home batter 4", hp4)
hp6 = Batter(2, "home batter 3", hp5)
hp7 = Batter(2, "home batter 2", hp6)
hp8 = Batter(2, "home batter 1", hp7)
hp1.next = hp8
ap1 = Batter(1, "away batter 8", None)
ap2 = Batter(2, "away batter 7", ap1)
ap3 = Batter(2, "away batter 6", ap2)
ap4 = Batter(2, "away batter 5", ap3)
ap5 = Batter(2, "away batter 4", ap4)
ap6 = Batter(2, "away batter 3", ap5)
ap7 = Batter(2, "away batter 2", ap6)
ap8 = Batter(2, "away batter 1", ap7)
ap1.next = ap8
d = Diamond()

g = Game(hp8, ap8, d, 8)
s = Simulation(game=g)

s.run(250)
outcomes = s.player_outcomes()

import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(outcomes)
# print(df)
sns.boxplot(y='fpts', x='player',
            data=df,
            palette="colorblind",
            hue='team')
plt.show()
