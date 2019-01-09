from turtle import Turtle 
import turtle
import random 

class ball():
	def__init__(self,x,y,dx,dy,r,color):
	Turtle.__init__(self)
	self.x = x
	self.y = y
	self.dx = dx
	self.dy = dy
	self.r = rself.color = color

	turtle.penup()
	self.goto(x,y)
	self.shape('circle')
	self.shapesize(r/10)
	self.color(color)

	def move(self,screen_width,screen_height):
		current_x = self.xcor()
		new_x=( current_x +self.dx )

		current_y = self.ycor()
		new_y=( current_y +self.dy )

		right_side_ball = ( new_x + self.r)
		left_side_ball = (new_x -self.r)
		upper_side_ball = (new_x -self.r)
		

