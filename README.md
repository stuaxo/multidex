# multidex
Simple Multi Index Dictionaries for python.

Dictionary that keeps indexes data by other keys.

Ideal for many "small data" situations where data fits into memory, and you want a fast lookup for various fields.


Specify extra indexes and their getters then use as a normal dict, to do lookups using the additional fields use the ```find```  method.

Toy example

```python
class HighScores(MultiIndex):
    __metaclass__ = MultiIndex
    alt_indexes = dict(
        species=operator.attrgetter("species"),
        score=operator.attrgetter("score")
    )
        
score_idx = HighScores(score.name: score for score in scores)
print score_idx.find("score")
(HighScore(name='zoooby', score=100, species='cat'),
 HighScore(name='chilax', score=100, species='cat'))
 
print score_idx.find("score", 1900)
(HighScore(name='jill', score=1900, species='human'),)

del d['zoooby']
d.find("species", "cat")
(HighScore(name='chilax', score=100, species='cat'),)
```
