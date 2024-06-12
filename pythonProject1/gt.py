import tkinter as tk
import random

class DartGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Dart Game")

        self.target_score = 100
        self.total_score = 0
        self.throws_left = 7

        self.setup_ui()

    def setup_ui(self):
        self.target_label = tk.Label(self.master, text=f"Target Score: {self.target_score}")
        self.target_label.pack()

        self.score_label = tk.Label(self.master, text="Total Score: 0")
        self.score_label.pack()

        self.throws_label = tk.Label(self.master, text="Throws Left: 5")
        self.throws_label.pack()

        self.throw_button = tk.Button(self.master, text="Throw Dart", command=self.throw_dart)
        self.throw_button.pack()

    def throw_dart(self):
        if self.throws_left > 0:
            score = random.randint(1, 20)
            self.total_score += score
            self.throws_left -= 1

            self.update_labels()

            if self.total_score >= self.target_score:
                self.end_game("Congratulations! You reached or exceeded the target score.")
            elif self.throws_left == 0:
                self.end_game("Oops! You ran out of throws. Better luck next time.")
        else:
            self.end_game("Game over. Thanks for playing!")

    def update_labels(self):
        self.score_label.config(text=f"Total Score: {self.total_score}")
        self.throws_label.config(text=f"Throws Left: {self.throws_left}")

    def end_game(self, message):
        self.throw_button.config(state=tk.DISABLED)
        self.target_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    dart_game = DartGame(root)
    root.mainloop()
