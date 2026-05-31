from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        with open ("scoreboard", "r") as file:
            self.high_score = int(file.read())
        self.update_scoreboard() # Call the helper to draw the initial screen

    def update_scoreboard(self):
        """Helper method: ONLY clears and redraws the current scores"""
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align="center", font=FONT)

    def increase_score(self):
        """Increments the score and refreshes the text"""
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        """Checks for a new high score, resets current score to 0, and refreshes text"""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("scoreboard", "w") as file:
            file.write(str(self.high_score))
        # This will now cleanly display 0 without adding 1