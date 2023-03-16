import turtle as t
from turtle import*


def shape(x,y,size):
    pensize(3)
    speed(100)
    for l in range(360):
        t.forward(l)
        t.right(10+l)
    penup()
    goto(0,0)
    pendown()
    
    for n in range (360):
        t.back(n)
        t.left(20) 

    for i in range(15):
        print(i)
        forward(10)
        left(10)
        penup()
        goto(0,0)
        pendown()
        for j in range(10):
            
            print(j)
            back(180)
            left(45)
        for k in range(15):
            
            print(k)
            forward(300)
            left(100)
           
    done()
author = "isaac"

def calculator (x: int, y: int = 5, subtract = True) -> int:
    return x - y if subtract else x + y
            
if __name__ == "__main__":
    shape(0,0,10)





    # def shape(x,y,size):
    # pensize(3)
    # speed(100)
    # for i in range(15):
    #     print(i)
    #     forward(10)
    #     left(10)
    #     for j in range(10):
    #         print(j)
    #         back(90)
    #         left(45)
    #     for k in range(15):
    #         print(k)
    #         forward(200)
    #         left(170)
            