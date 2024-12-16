import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
        self.exp = 0
        self.history = []  # Store the score history for analysis
    def reset_game(self):
        self.die1 = Dice()
        self.die2 = Dice()
        self.die3 = Dice()
        self.fixed = [False, False, False]
        self.tupled_out = False
        self.score = 0
        self.exp = 0
    def roll_dice(self):
        if not self.fixed[0]:
            self.die1.roll()
        if not self.fixed[1]:
            self.die2.roll()
        if not self.fixed[2]:
            self.die3.roll()   
        self.fix_dice()
        self.calculate_score()
        self.expectation() 
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
        return self.fixed
    def calculate_score(self):
        if self.tupled_out:
            self.score = 0
        else:
            values = [self.die1.value, self.die2.value, self.die3.value]
            self.score = sum(values[i] for i in range(3))
        return self.score
    def play_turn(self):
        print("Starting a new turn!")
        self.roll_dice()
        while True:
            print(f'Dice values: {self.die1.value, self.die2.value, self.die3.value}')
            if self.check_tuple_out():
                print('Tupled out, Turn ends with 0')
                self.score = 0
                break
            self.fix_dice()
            print(f'Fixed dice:{self.fixed}')
            print(f'Your current score is: {self.score}')
            print(f'Expectation of rolling again: {self.exp}')
            decision = input('Do you want to re-roll unfixed dice?(y/n):').strip().lower()
            if decision != 'y':
                break
            self.roll_dice()

        self.calculate_score()
        print(f'Turn ends with a score of: {self.score}')
        self.history.append(self.score)  # Record the score for analysis
        return self.score
    def expectation(self):
        if self.fixed == [False, False, False]:
            self.exp = 10.5*(35/36) - self.score
        elif self.fixed == [True, True, True]:
            self.exp = 0
        else:
            values = [self.die1.value, self.die2.value, self.die3.value]
            for i in range(3):
                if not self.fixed[i]:
                    self.exp = (3.5 - values[i]) * 5/6 - self.score/6
        return self.exp

    def computer_roll(self):
        # Computer rolls until the expectation is negative or it reaches the max number of rolls
        rolls = 0
        while self.exp >= 0 and rolls < 10:  # You can set a limit for rolls here
            self.roll_dice()
            rolls += 1
            print(f'Computer rolled: {self.die1.value, self.die2.value, self.die3.value}')
            print(f'Expectation of rolling again: {self.exp}')
            print(f'Computer score after roll: {self.score}')
        self.history.append(self.score)  # Record the score after computer's turn
        return self.score

# Data Analysis and Visualization
def analyze_and_visualize_scores(scores):
    # Use Pandas to analyze the data
    df = pd.DataFrame(scores, columns=["Score"])
    
    # Calculate basic statistics
    print("Basic Statistics:")
    print(df.describe())

    # Visualize the scores distribution using Seaborn
    plt.figure(figsize=(8, 6))
    sns.histplot(df["Score"], kde=True, bins=10, color='blue')
    plt.title("Distribution of Scores from Computer Rolls")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()

def play_game():
    print("Welcome to the Dice Game!")
    game = Dice_Game()
    
    # Ask user if they want to play themselves or let the computer play
    mode = input("Do you want to play by yourself or let the computer play? (self/computer): ").strip().lower()
    
    if mode == "computer":
        computer_turns = int(input("How many turns should the computer play? "))
        
        for _ in range(computer_turns):
            game.reset_game()
            score = game.computer_roll()
            print(f'Computer ended with a score of {score}')
        
        # After the game, analyze and visualize the results
        analyze_and_visualize_scores(game.history)
    
    elif mode == "self":
        while True:
            score = game.play_turn()
            print(f'Your score of this turn is {score}')
            play_again = input("Do you want to play another turn?(y/n):").strip().lower()
            if play_again != 'y':
                print("Goodbye!")
                break
            game.reset_game()

if __name__ == "__main__":
    play_game()
