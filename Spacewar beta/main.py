import turtle
import os
import random


win = turtle.Screen()
win.title("Spacewar (beta) by Rami Mikha")
win.bgcolor("black")
win.tracer(1) #sets drawing speed
win.setup(width=650, height=650)

#turtle.setundobuffer(1) #saves memory
turtle.speed(0)
turtle.ht() #hide the defualt turtle

#creating class which will be called when sprites are made
class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0) #speed of animation, 0 is max
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1 #speed of movement    

        #creates a move method for all sprites when created
    def move(self):
        self.fd(self.speed)

        #border check
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

#creating a player class which is a child of the sprite class (takes code from sprite class and adds to it only for player sprite)
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 3
        self.lives = 3
    def turn_left(self):
        self.lt(45)
    def turn_right(self):
        self.rt(45)
    def accelerate(self):
        self.speed +=1
    def decelerate(self):
        self.speed -=1

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing" #tell program what state the game is in, if its done or if it is running
        self.pen = turtle.Turtle()
        self.lives = 3
    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300,300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()

#create game object
game = Game()

#drawing the border
game.draw_border()

#Create the sprites
player = Player("triangle", "white", 0, 0 )


#keyboard bindings
turtle.listen()
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")

#main game loop
while True:
    win.update()
    player.move()
    

