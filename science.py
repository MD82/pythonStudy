import turtle as t
import math

tm = 0.3
ux = 0
uy = 0
dx = 0
dy = 0
g = 9.8
velo = 0
ang = 0

def draw_pos(x,y):
    velo = t.numinput("입력", "속도 : ", 50, 50, 100)
    ang = math.radians(t.numinput("입력", "각도 : ", 45, 0, 360))

    t.clearstamps()
    t.hideturtle()
    t.setpos(x,y)
    t.showturtle()
    t.stamp()

    hl = -(t.window_height() / 2)

    ux = velo * math.cos(ang)
    uy = velo * math.sin(ang)

    while True:
        uy = uy + (-1 * g) * tm
        dy = t.ycor() + (uy*tm) - (g * tm**2)/2
        dx = t.xcor() + (ux*tm)
        if dy > hl:
            t.goto(dx, dy)
            t.stamp()
        else:
            break

t.setup(600, 600)
t.shapesize(0.3, 0.3, 0)
t.penup()
s = t.Screen()
s.onscreenclick(draw_pos)
s.listen()
t.mainloop() # IDE에서 실행하자마자 터틀 스크린이 꺼짐