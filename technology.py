import turtle as t

s7seg_base = "7s10.gif"
s7seg_led = ["7s-a.gif","7s-b.gif","7s-c.gif","7s-d.gif","7s-e.gif","7s-f.gif","7s-g.gif"]
s7seg_num = [[1,1,1,1,1,1,0], #0
             [0,1,1,0,0,0,0], #1
             [1,1,0,1,1,0,1], #2
             [1,1,1,1,0,0,1], #3
             [0,1,1,0,0,1,1], #4
             [1,0,1,1,0,1,1], #5
             [1,0,1,1,1,1,1], #6
             [1,1,1,0,0,0,0], #7
             [1,1,1,1,1,1,1], #8
             [1,1,1,1,0,1,1]  #9
            ]
old_key = 0

def disp_num(k):
    global old_key
    t.shape(s7seg_base)
    t.stamp()
    if k != old_key:
        if k < 10:
            for i in range(7):
                if s7seg_num[k][i] == 1:
                    t.shape(s7seg_led[i])
                    t.stamp()
    old_key = k

def key_0():
    disp_num(0)
def key_1():
    disp_num(1)
def key_2():
    disp_num(2)
def key_3():
    disp_num(3)
def key_4():
    disp_num(4)
def key_5():
    disp_num(5)
def key_6():
    disp_num(6)
def key_7():
    disp_num(7)
def key_8():
    disp_num(8)
def key_9():
    disp_num(9)
def key_10():
    t.clearstamps()
    disp_num(10)

t.setup(400, 400)
s = t.Screen()
t.hideturtle()
t.speed(0)

s.addshape(s7seg_base)
for i in range(7):
    s.addshape(s7seg_led[i])

disp_num(10)

s.onkeypress(key_0, "0")
s.onkeypress(key_1, "1")
s.onkeypress(key_2, "2")
s.onkeypress(key_3, "3")
s.onkeypress(key_4, "4")
s.onkeypress(key_5, "5")
s.onkeypress(key_6, "6")
s.onkeypress(key_7, "7")
s.onkeypress(key_8, "8")
s.onkeypress(key_9, "9")

s.onkeyrelease(key_10, "0")
s.onkeyrelease(key_10, "1")
s.onkeyrelease(key_10, "2")
s.onkeyrelease(key_10, "3")
s.onkeyrelease(key_10, "4")
s.onkeyrelease(key_10, "5")
s.onkeyrelease(key_10, "6")
s.onkeyrelease(key_10, "7")
s.onkeyrelease(key_10, "8")
s.onkeyrelease(key_10, "9")
s.listen()
t.mainloop() # IDE에서 실행하자마자 터틀 스크린이 꺼짐