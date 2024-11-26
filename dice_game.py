import random

class Dice:
    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value


class DiceGame:
    def __init__(self):
        self.dice = [Dice() for _ in range(3)]
        self.fixed = [False, False, False]
        self.tupled_out = False
        self.score = 0

    def roll_dice(self):
        for i in range(3):
            if not self.fixed[i]:
                self.dice[i].roll()

    def check_tuple_out(self):
        values = [die.value for die in self.dice]
        if values[0] == values[1] == values[2]:
            self.tupled_out = True
            return True
        return False

    def fix_dice(self):
        values = [die.value for die in self.dice]
        for i in range(3):
            if values.count(values[i]) == 2:
                self.fixed = [values[j] == values[i] for j in range(3)]
                break

    def calculate_score(self):
        if self.tupled_out:
            self.score = 0
        else:
            self.score = sum(die.value for i, die in enumerate(self.dice) if not self.fixed[i])

    def play_turn(self):
        print("Starting a new turn!")
        self.roll_dice()
        while True:
            print(f"Dice values: {[die.value for die in self.dice]}")
            if self.check_tuple_out():
                print("You tupled out! Turn ends with 0 points.")
                self.score = 0
                break

            self.fix_dice()
            print(f"Fixed dice: {self.fixed}")
            if all(self.fixed):
                print("All dice are fixed. Turn ends.")
                break

            decision = input("Do you want to re-roll unfixed dice? (y/n): ").strip().lower()
            if decision != 'y':
                break

            self.roll_dice()

        self.calculate_score()
        print(f"Turn ends with a score of: {self.score}")
        return self.score


if __name__ == "__main__":
    print("Welcome to the Dice Game!")
    game = DiceGame()
    while True:
        score = game.play_turn()
        print(f"Your score this turn: {score}")
        play_again = input("Do you want to play another turn? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break