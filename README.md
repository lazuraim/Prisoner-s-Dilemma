# Day 02 - Python Bootcamp




|  | Both cooperate | 1 cheats, 2 cooperates | 1 cooperates, 2 cheats | Both cheat |
|------------|----------|----------|----------|---------|
| Operator 1 | +2 candy | +3 candy | -1 candy | 0 candy |
| Operator 2 | +2 candy | -1 candy | +3 candy | 0 candy |

If everyone is cooperating and puts candy in a machine as agreed,
everyone gets a reward. But both participants also have a temptation to
cheat and only pretend to put a candy into machine, because in this case
their group will get 3 candy back, just taking one candy from a second
group. The problem is, if both operators decide to play dirty, then nobody
will get anything.

Five models of behavior:

| Behavior type | Player Actions                                                                                                                                                                                         |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cheater       | Always cheats                                                                                                                                                                                          |
| Cooperator    | Always cooperates                                                                                                                                                                                      |
| Copycat       | Starts with cooperating, but then just repeats whatever the other guy is doing                                                                                                                         |
| Grudger       | Starts by always cooperating, but switches to Cheater forever if another guy cheats even once                                                                                                          |
| Detective     | First four times goes with [Cooperate, Cheat, Cooperate, Cooperate],  and if during these four turns another guy cheats even once -  switches into a Copycat. Otherwise, switches into Cheater himself |

-----

You need to model a system with seven
classes - `Game`, `Player` and five behavior types (subclassed from `Player`).

The skeleton for a `Game` class looks like this:

```python
from collections import Counter

class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        # simulate number of matches
        # equal to self.matches

    def top3(self):
        # print top three
```

Here, `registry` is used to keep track of the current number of candy
during the game, while `player1` and `player2` are instances of 
subclasses of `Player` (each being one of 5 behavior types). Calling 
`play()` method of a `Game` instance should perform a simulation
of a specified number of matches between players of a given behavior.

Method `top3()` should print current top three player's behaviors
along with their current score, like:

```
cheater 10
detective 9
grudger 8
```

By default, your code when run should simulate 10 matches (one call of
`play()`) between every pair of two players with *different* behavior
types (total 10 rounds by 10 matches each, no matches between two
copies of the same behavior) and print top three winners after the 
whole game.

You are strongly encouraged to experiment around with different
behaviors and writing your own behavior class (this is graded as a
bonus). You can get even more bonus points if an instance of your 
class performs better in the same "contest between each pair of
players" check that at least three of five provided behaviors.

Don't forget that the only thing a player can do on each turn is
either cooperate or cheat, based on a history of a current game.
