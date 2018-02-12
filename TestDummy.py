#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:00:59 2018

@author: austinmcdonnell
"""

import matplotlib.pyplot as plt
import os
import numpy


def pressure(V,n,R,T):
    return n*R*T/V

def Force(P,A):
    return P * A

def acceleration(F,m):
    return F / m

def velocity(u,a,dt):
    return u + a * dt

def position(x,u,dt):
    return x + u * dt

def moles(n,flow,dt):
    return n + flow * dt

def Volume(x,A):
    return x * A

def propogate(step_size,num_steps):
#Globals
    P = 101300 # Initial pressure Pascals
    P_STP = 101300 #Standard room temp pressure
    radius = 0.050 # radius of piston meters
    A = 3.14 * (radius )**2# Area of piston face
    x = 0.010 # intial length meters
    V = x * A #inital length times area
    R = 8.314#J/ mol K
    T = 273#Kelvin
    n = P * V / ( R * T ) # moles
    m = 0.5 #mass of piston
    u = 0.0 # velocity
    a = 0.0 # acceleration
    F = 0.0 # force
    friction = 1#pseduo frictional force
    flow = 1 * 0.0224 # Liters per second times moles in a liter
    
    P_list = [] # for plotting
    pos_list = []
    times = []
    vel_list = []
    moles_list = []
    a_list = []
    
 
    #Algorithm Engine
    for dt in range(1,num_steps):
        n = moles(n,flow,step_size)
        P = pressure(V,n,R,T)
        F = Force(P,A) - (P_STP * A) - friction # subtract air pressure and estimate friction
        a = acceleration(F,m)
        u = velocity(u,a,step_size )
        x = position(x,u,step_size )
        V = Volume(A,x)
       
        numpy.savetxt("PistonData.txt",moles_list,fmt='%1.4e',header='Moles List')
        numpy.savetxt("PistonData1.txt",times,fmt='%1.4e',header='Times')
        numpy.savetxt("PistonData2.txt",P_list,fmt='%1.4e',header='Pressure')
        numpy.savetxt("PistonData3.txt",a_list,fmt='%1.4e',header='Acceleration')
        numpy.savetxt("PistonData4.txt",vel_list,fmt='%1.4e',header='Velocity')
        numpy.savetxt("PistonData5.txt",pos_list,fmt='%1.4e',header='Position')
     
    #End Engine
    
        #Gather for plotting
        moles_list.append(n)
        times.append(dt)
        P_list.append(P)
        a_list.append(a)
        vel_list.append(u)
        pos_list.append(x)
        
       
    #Plots
    plt.figure(1)
    plt.plot(times, P_list, 'ko-')
    plt.title('Time evolution of piston')
    plt.ylabel('Pressure in Pascals')
    os.chdir('/Users/austinmcdonnell/Desktop')
    plt.savefig('Piston1.png')
        
    plt.figure(2)
    plt.plot(times, moles_list, 'y.-')
    plt.ylabel('gas in moles')
    os.chdir('/Users/austinmcdonnell/Desktop')
    plt.savefig('Piston2.png')
        
    plt.figure(3)
    plt.plot(times, a_list, 'ko-')
    plt.ylabel('acceleration m/ss')
    os.chdir('/Users/austinmcdonnell/Desktop')
    plt.savefig('Piston3.png')
    
    plt.figure(4)
    plt.plot(times, vel_list, 'b.-')
    plt.ylabel('Velocity m/s')
    os.chdir('/Users/austinmcdonnell/Desktop')
    plt.savefig('Piston4.png')

    plt.figure(5)
    plt.plot(times, pos_list, 'r.-')
    plt.xlabel('time (millisecond)')
    plt.ylabel('position m')
    os.chdir('/Users/austinmcdonnell/Desktop')
    plt.savefig('Piston5.png')
    plt.show()
#main loop
propogate(0.001,10) #STtep size and num_steps

         
#The next thing that you need to do is check how all things end up changing from when you
#start it at the 101300 initial pressure for 10 runs then using that ending pressure for the inital for the next 10;
#compared to a run of 20.>> The results of changing the inital pressures and doing a set of two 8 point runs and one 
#16 point run show that the are slight differences when there is a pause but the do come to a very similar point
