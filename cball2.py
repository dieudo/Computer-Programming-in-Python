# cball2.py
from math import pi, sin, cos, radians

def main():
    angle, vel, time = getInputs()
    xpos, ypos = 0, 0
    xvel, yvel = getXYComponents(vel, angle)
    while ypos >= 0:     # update position and velocity
        xpos,ypos,yvel= updateCannonBall(time,xpos,ypos,xvel,yvel)
        print("(xpos,ypos): ({},{})".format(xpos, ypos))

def getInputs():
    a = eval(input("Enter the launch angle (in degrees):"))
    v = eval(input("Enter the initial velocity (in meters/sec):"))
    t = eval(input("Enter time interval between calculations:"))
    return a,v,t

def getXYComponents(vel, angle):
    theta = radians(angle)
    x = vel * cos(theta)
    y = vel * sin(theta)
    return x, y

def updateCannonBall(time, xpos, ypos, xvel, yvel):
        xpos = xpos + time * xvel
        yvel1 = yvel - 9.8 * time
        ypos = ypos + time * (yvel + yvel1)/2.0
        return xpos, ypos, yvel1
     
main()
