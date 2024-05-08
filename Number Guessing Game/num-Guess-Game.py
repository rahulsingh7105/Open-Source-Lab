#GUI

import tkinter as tk
import random

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Number Guessing Game")
        self.geometry("300x200")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(self, text="Welcome to the Number Guessing Game!")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(self, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.feedback_label = tk.Label(self, text="")
        self.feedback_label.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.feedback_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.feedback_label.config(text="Too high! Try again.")
            else:
                self.feedback_label.config(text=f"Congratulations! You've guessed the number {self.secret_number} in {self.attempts} attempts!")
                self.guess_button.config(state="disabled")
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.")

if __name__ == "__main__":
    app = NumberGuessingGame()
    app.mainloop()





# Console
import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_number()
