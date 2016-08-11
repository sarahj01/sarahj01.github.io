
from turtle import *

red = 0
blue = 0
green = 0

def hexagon(hex_color):
	#pencolor(hex_color)
	speed(0)
	for i in range(6):
		right(60)
		forward(100)
		
def draw_circle(color2):
	penup()
	pendown()
	pencolor(color2)
	circle(100)
	
#color2 = input("Pick: ")
your_color = input("Pick again: ")

for i in range(20):
	#pencolor((red+i*5, green+i*5, blue+i*5))
	#speed(0)
	#hexagon((red+i*5, green+i*5, blue+i*5))
	forward(10)
	'''
for i in range(15):
	fillcolor(your_color)
	begin_fill()
	speed(0)
	draw_circle(color2)
	forward(5)
	'''
end_fill()

done()



