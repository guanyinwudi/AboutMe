#!/usr/bin/python
import turtle
from random import choice
x,y=0,0
d=10
pts=[(x,y)]
L=20
dirs=[(0,1),(1,0),(0,-1),(-1,0)]
route=turtle.Turtle()
route.setposition(0,0)
x=1
route.goto(x*d,y*d)
pts.append((x,y))
while True:
    dr=list(dirs)
    for (dx,dy) in dirs:
        if x+dx<-L or x+dx>L or y+dy<-L or y+dy>L or (x+dx,y+dy) in pts:
            dr.remove((dx,dy))
    cnt=len(dr)
    if cnt==0:
        break
    (dx,dy)=choice(dr)
    x+=dx
    y+=dy
    pts.append((x,y))
    route.goto(x*d,y*d)
turtle.done()
