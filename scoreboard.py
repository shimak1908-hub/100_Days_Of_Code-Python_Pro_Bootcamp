from turtle import Turtle




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score = {self.score}" , align="center" , font=("Arial" , 24 , "normal"))
        self.hideturtle()
        self.update_scoreboard()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt" , mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0 , 0)
    #     self.write("Game Over" , align="center" , font=("Arial" , 24 , "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()



class Snake:
    def __init__(self):
        self.snakes = []

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snakes.append(new_segment)