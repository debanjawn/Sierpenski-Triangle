from turtle import *
pen = Turtle()
pen.speed(0)
pen.ht()
def drawTriangle(r,x,y):
  pen.up()
  pen.goto(r+x,-r+y)
  pen.down()
  pen.goto(x,y+r)
  pen.goto(x-r,y-r)
  pen.goto(x+r,y-r)

def layerTwo(r,x,y,t):
  if t > 0:
    layerTwo(r/2,x,y+r,t-1)
    layerTwo(r/2,x-r,y-r,t-1)
    layerTwo(r/2,x+r,y-r,t-1)
  else:
    drawTriangle(r,x,y+r)#(r,x+r,y-r)(10,20,0)
    drawTriangle(r,x-r,y-r)#(x+r,y-r)
    drawTriangle(r,x+r,y-r)#(r,x,y+r)(10,10,20)

layerTwo(50,0,0,5)

'''
def layerThree(r,x,y):
  layerTwo(r/2,x,y+r)
  layerTwo(r/2,x-r,y-r)
  layerTwo(r/2,x+r,y-r)

layerThree(10,0,0)
'''