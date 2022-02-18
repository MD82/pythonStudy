import turtle as t

color_status = ["white", "blue", "red"]
alert_status = ["정상", "주의", "화재"]
tempc = 50

def check_fire():
    if tempc < 80:
        status = 0
    elif tempc < 120:
        status = 1
    else:
        status = 2

    t.clear()
    t.home()
    t.pendown()
    t.fillcolor(color_status[status])
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(-22, 50)
    t.write("%s : %d"%(alert_status[status],tempc))

def keyUp():
    global tempc
    if tempc < 80:
        tempc = tempc + 5
    else:
        tempc = tempc + 10
    check_fire()

def keyDown():
    global tempc
    if tempc <= 0:
        tempc = 0
    elif tempc <= 80:
        tempc = tempc - 5
    else:
        tempc = tempc - 10
    check_fire()

t.setup(300, 300)
s = t.Screen()
t.hideturtle()
t.speed(0)
check_fire()
s.onkey(keyUp, "Up")
s.onkey(keyDown, "Down")
s.onkey(s.bye, "q")
s.listen()
t.mainloop() # IDE에서 실행하자마자 터틀 스크린이 꺼짐