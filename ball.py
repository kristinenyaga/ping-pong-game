from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.up()
        self.y_move =10
        self.x_move = 6
        self.move_speed =0.04
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)
    
    def change_direction(self):
        self.y_move*=-1
    
    def bounce(self):
        self.x_move*=-1