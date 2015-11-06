## example - create a highscore table indexable by score, name and species

from multidex import MultiIndex

from operator import attrgetter
from collections import namedtuple

HighScore = namedtuple("HighScore", "name score species")

class HighScores(object):
    __metaclass__ = MultiIndex

    # specify index name and getter
    alt_indexes = dict(
        species=attrgetter("species"),
        score=attrgetter("score")
    )
        
score_idx = HighScores()

highscores = [
    HighScore("terry", 200, "cat"),
    HighScore("jill", 1900, "human"),
    HighScore("zoooby", 100, "cat"),
    HighScore("chilax", 100, "human"),
]

for score in highscores:
    score_idx[score.name] = score

for species in ["cat", "human"]:
    print("Top %s scores" % species)
    for highscore in sorted(score_idx.find("species", species), key=attrgetter("score"), reverse=True):
        print("*** %s *** %s" % (highscore.name, highscore.score))
