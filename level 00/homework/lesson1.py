from turtle import *

speed(30)
#we womt to paint a house

#step 1:  draw a square
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
# end of square

#drawing a door

left(90)
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)

right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,  200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)

end_fill()

penup()
goto(0,  150)
goto(170, 150)
pendown()
color("green")

right(60)
forward(30)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(10)

penup()
goto(40, 150)
pendown()
forward(20)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)



exitonclick()