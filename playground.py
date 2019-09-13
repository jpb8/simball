from simball import Batter, Game

p1 = Batter(1, "Joe Ballard", None)
p2 = Batter(2, "Sam Manc", p1)
p1.next = p2
p3 = Batter(3, "Stave Ballard", None)
p4 = Batter(4, "Becky Ballard", p3)
p3.next = p4

g = Game(p1, p3, None)

g.play_ball()

