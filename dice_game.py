import random
class Dice:
    def __init__(self):
        self.value = 0
    def roll(self):
        self.value = random.randint(1,6)
        return self.value
    
class Dice_Game:
    def __init__(self):
        self.die1 = Dice()
        self.die2 = Dice()
        self.die3 = Dice()
        self.fixed = [False, False, False]
        self.tupled_out = False
        self.score = 0
    def reset_game(self):
        self.die1 = Dice()
        self.die2 = Dice()
        self.die3 = Dice()
        self.fixed = [False, False, False]
        self.tupled_out = False
        self.score = 0
    def roll_dice(self):
        if not self.fixed[0]:
            self.die1.roll()
        if not self.fixed[1]:
            self.die2.roll()
        if not self.fixed[2]:
            self.die3.roll()    
    def check_tuple_out(self):
        values = [self.die1.value, self.die2.value, self.die3.value]
        if values[0] == values[1] == values[2]:
            self.tupled_out = True
            return True
        return False
    def fix_dice(self):
        values = [self.die1.value, self.die2.value, self.die3.value]
        for i in range(3):
            if values.count(values[i]) == 2:
                self.fixed = [values[j] == values[i] for j in range(3)]
                break
        if self.tupled_out:
            self.fixed = [True, True, True]
    def calculate_score(self):
        if self.tupled_out:
            self.score = 0
        else:
            values = [self.die1.value, self.die2.value, self.die3.value]
            self.score = sum(values[i] for i in range(3))
    def play_turn(self):
        print("Starting a new turn!")
        self.roll_dice()
        while True:
            print(f'Dice values:{self.die1.value, self.die2.value, self.die3.value}')
            if self.check_tuple_out():
                print('Tupled out, Turn ends with 0')
                self.score = 0
                break
            self.fix_dice()
            print(f'Fixed dice:{self.fixed}')
            decision = input('Do you want to re-roll unfixed dice?(y/n):').strip().lower()
            if decision != 'y':
                break
            self.roll_dice()

        self.calculate_score()
        print(f'Turn ends with a score of: {self.score}')
        return self.score
if __name__ == "__main__":
    print("Welcome")
    game = Dice_Game()
    while True:
        score = game.play_turn()
        print(f'Your score of this turn is {score}')
        play_again = input("Do you want to play another turn?(y/n):").strip().lower()
        if play_again != 'y':
            print("Goodbye!")
            break
        game.reset_game()
