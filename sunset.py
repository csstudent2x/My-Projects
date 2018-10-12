#GWC PROJECT
from turtle import *
#sun
penup()
pensize(10)
colormode(255)
pencolor(255,255,0)
speed(0)
goto(-200,200)
pendown()
fillcolor("yellow")
begin_fill()
for i in range(1):
	circle(80,360,1000)
end_fill()

#roof
penup()
colormode(255)
goto(-50,10)
right(45)
pendown()
fillcolor("rosy brown")
begin_fill()
for i in range(1):
	pencolor(188,143,143)
	forward(100)
	left(225) 
	forward(140)
	left(230)
	forward(95)
end_fill()

#square
penup() 
goto(-120,-60)
colormode(255)
fillcolor("salmon")
begin_fill()
pendown()
right(50)
for i in range(4):
	pencolor(250,128,114)
	forward(140)
	right(90)
end_fill()

#roof
penup()	
goto(100,10)
right(45)
pendown()
fillcolor("peach puff")
begin_fill()
for i in range(1):
	pencolor(255,218,185)
	forward(100)
	left(225) 
	forward(140)
	left(230)
	forward(95)
end_fill()

#square
penup() 
goto(30,-60)
colormode(255)
fillcolor("slate gray")
begin_fill()
pendown()
right(50)
for i in range(4):
	pencolor(112,128,144)
	forward(140)
	right(90)
end_fill()

#roof
penup()	
goto(250,10)
right(45)
pendown()
fillcolor("sea green")
begin_fill()
for i in range(1):
	pencolor(46,139,87)
	forward(100)
	left(225) 
	forward(140)
	left(230)
	forward(95)
end_fill()

#square
penup() 
goto(180,-60)
colormode(255)
fillcolor("orchid")
begin_fill()
pendown()
right(50)
for i in range(4):
	pencolor(218,112,214)
	forward(140)
	right(90)
end_fill()




	
	
mainloop()
