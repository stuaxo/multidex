# Multidex
Simple Multi Index Dictionaries for python.

Dictionary with secondary indexes.

Ideal for many "small data" situations where data fits into memory, and you want a fast lookup for various fields.


Specify extra indexes and their getters then use as a normal dict, to do lookups using the additional fields use the ```find```  method.

Toy example

```python
from collections import namedtuple
from operator import attrgetter
from multidex import MultiIndex

HighScore = namedtuple("HighScore", "name score species")
highscores = [
    HighScore("terry", 200, "cat"),
    HighScore("jill", 1900, "human"),
    HighScore("zoooby", 100, "cat"),
    HighScore("chilax", 100, "human"),
]


class HighScores(object):
    __metaclass__ = MultiIndex
    alt_indexes = dict(
        species=attrgetter("species"),
        score=attrgetter("score")
    )


score_idx = HighScores(**{score.name: score for score in highscores})
print score_idx.find("score", 100)
(HighScore(name='chilax', score=100, species='human'), HighScore(name='zoooby', score=100, species='cat'))
```
