from collections import Counter
import itertools


class Game(object):
    def __init__(self, matches=10):
        self.matches: int = matches
        self.registry: Counter = Counter()

    def play(self):
        all_players: list = [Cooperator(), Cheater(), Copycat(), Grudger(), Detective(),
                             UpsideDown(), Sequence(), Careful()]
        for player1, player2 in itertools.combinations(all_players, 2):
            dec_hist1: list = []
            dec_hist2: list = []
            for i in range(self.matches):
                dec_hist1.append(player1.make_decision(dec_hist2))
                dec_hist2.append(player2.make_decision(dec_hist1))
                if dec_hist1[-1] and dec_hist2[-1]:
                    self.registry.update({player1.name: 2, player2.name: 2})
                elif dec_hist1[-1] and not dec_hist2[-1]:
                    self.registry.update({player1.name: -1, player2.name: 3})
                elif not dec_hist1[-1] and dec_hist2[-1]:
                    self.registry.update({player1.name: 3, player2.name: -1})

    def top3(self):
        dict_registry: dict = dict(self.registry.most_common(3))
        for i in dict_registry:
            print(i, dict_registry[i])


class Player:
    def __init__(self, name=""):
        self.name: str = name


class Cheater(Player):
    def __init__(self):
        super().__init__("Cheater")

    @staticmethod
    def make_decision(other_decision: list) -> bool:
        return False


class Cooperator(Player):
    def __init__(self):
        super().__init__("Cooperator")

    @staticmethod
    def make_decision(other_decision: list) -> bool:
        return True


class Copycat(Player):
    def __init__(self):
        super().__init__("Copycat")

    @staticmethod
    def make_decision(other_decision: list) -> bool:
        if len(other_decision) == 0:
            return True
        return other_decision[-1]


class Grudger(Player):
    def __init__(self):
        super().__init__("Grudger")

    @staticmethod
    def make_decision(other_decision: list) -> bool:
        if False in other_decision:
            return False
        return True


class Detective(Player):
    def __init__(self):
        super().__init__("Detective")
        self.decisions = [True, True, False, True]

    def make_decision(self, other_decision: list) -> bool:
        if False in other_decision:
            return other_decision[-1]
        elif self.decisions:
            return self.decisions.pop()
        return False


class UpsideDown(Player):
    def __init__(self):
        super().__init__("UpsideDown")

    @staticmethod
    def make_decision(other_decision: list) -> bool:
        return not other_decision


class Sequence(Player):
    def __init__(self):
        super().__init__("Sequence")

    @staticmethod
    def make_decision(other_decision: list) -> bool:
        if len(other_decision) % 2 == 0:
            return False
        return True


class Careful(Player):
    def __init__(self):
        super().__init__("Careful")
        self.decisions = [True, True, True, True]

    def make_decision(self, other_decision: list) -> bool:
        if False in other_decision:
            return False
        elif self.decisions:
            return self.decisions.pop()
        return False


if __name__ == "__main__":
    gm = Game()
    gm.play()
    gm.top3()
