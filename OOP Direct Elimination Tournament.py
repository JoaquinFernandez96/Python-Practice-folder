import random
from math import floor

# from operator import methodcaller


class player:
    def __init__(self, name: str, luck: int) -> None:
        self.name = "player_" + name
        self.rank = random.randint(1, 101)
        self.speed = random.randint(1, 101)
        self.luck = luck

    def __str__(self):
        return "player name: {0}\nrank: {1}\nspeed: {2}\nluck: {3}".format(
            self.name, self.rank, self.speed, self.luck
        )

    def powerlevel(self):
        return floor(0.60 * self.rank + 0.20 * self.speed + 0.20 * self.luck)


class tournament:
    def __init__(self, players: list[object]) -> None:
        self.players = [i for i in players]
        self.active_bracket = self.players
        self.next_round = []

    def bracket(self):
        i = 1
        while len(self.active_bracket) > 1:
            self.current_match = random.sample(self.active_bracket, 2)
            winner = max(self.current_match, key=lambda x: x.powerlevel())

            self.next_round.append(winner)

            print(
                "match #" + str(i),
                self.current_match[0].name,
                "vs",
                self.current_match[1].name,
                "winner:",
                winner.name,
            )
            i += 1

            self.active_bracket = [
                ele for ele in self.active_bracket if ele not in self.current_match
            ]
        print("\n")
        self.active_bracket = self.next_round
        self.next_round = []

    def play(self):
        # matches_in_bracket = len(self.active_bracket) // 2
        bracket_depth = 1
        while len(self.active_bracket) > 1:
            print("bracket #" + str(bracket_depth))
            self.bracket()
            bracket_depth += 1
        overall_winner = self.active_bracket[0]
        print("overall winner:", overall_winner.name)


player_names = [str(i) for i in range(1, 65)]


players_to_instance = []
for i in player_names:
    players_to_instance.append(player(i, random.randint(1, 101)))
torneo = tournament(players_to_instance)
# print(torneo.active[0])
print(torneo.play())
# print(players_to_instance)
