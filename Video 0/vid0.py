from turtle import *

width(7)
speed(30)
color("darkblue")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(80)

begin_fill()
color("red")
left(90)
forward(75)
right(90)
forward(40)
right(90)
forward(75)
right(90)
forward(40)
end_fill()

penup()
goto(200, 200)
pendown()

color("purple")
begin_fill()
right(60)
forward(200)
left(120)
forward(200)
end_fill()


color("brown")
penup()
goto(80, 100)

begin_fill()
right(60)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
left(90)

penup()
goto(160, 100)
pendown()
right(180)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

exitonclick()