from random import randint


class MontyHallGame:
    def __init__(self, strat=1):
        self.strat = strat

    def initialize(self):
        self.true_door = randint(1, 3)
        self.considered_doors = [1, 2, 3]
        self.false_doors = [1, 2, 3]
        self.false_doors.remove(self.true_door)
        self.game_doors = self.false_doors[:]

        self.door = randint(1, 3)  # door chosen by player
        if self.door in self.game_doors:
            self.game_doors.remove(self.door)

    def close_door(self):
        close_id = randint(0, len(self.game_doors) - 1)
        goat_door = self.game_doors[close_id]
        self.considered_doors.remove(goat_door)
        return self.game_doors[close_id]

    def strat_1(self):
        '''keep the door'''
        pass

    def strat_2(self):
        '''change door'''
        self.considered_doors.remove(self.door)
        self.door = self.considered_doors[0]

    def strat_3(self):
        '''random'''
        choose_id = randint(0, 1)
        self.door = self.considered_doors[choose_id]

    def result(self):
        return int(self.door == self.true_door)

    def simulate(self):
        self.initialize()
        self.close_door()
        if self.strat == 1:
            self.strat_1()
        elif self.strat == 2:
            self.strat_2()
        else:
            self.strat_3()
        return self.result()

    def simulate_n(self, n):
        total = 0
        for _ in range(n):
            total += self.simulate()
        return total / n  # ratio of success with strategy k;

player_1 = MontyHallGame(strat=1)
player_2 = MontyHallGame(strat=2)
player_3 = MontyHallGame(strat=3)

n=100_000

print("Keep your choice strategy: {}% success.".format(player_1.simulate_n(n)*100))
print("Change your choice strategy: {}% success.".format(player_2.simulate_n(n)*100))
print("Re-randomize your choice after the goat door was opened strategy: {}% success.".format(player_3.simulate_n(n)*100))
