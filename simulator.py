# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 16:27:24 2018

@author: scott.gee
"""

#new rocket simulator

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import math

def traj_solve(isp,massf,massi,rocket_diam,Cd):
#variables used for everything, could dictate different ISPs later
    isp = isp   #s
    g = 9.81    #m/s^2
    mdot = 2  #kg/s
    mcrafti = massi  #kg
    mcraftf = massf  #kg
    Cd = Cd
    ro = 1.225   #kg/m^3  but should vary this as a function of altitude
    rock_diameter = rocket_diam #m
    rock_cross_area = rock_diameter**2 * math.pi /4
    #variables you can vary
            #ISP, Cd
    sim_time = 25
    num_steps = 1500
    delta_t = sim_time/num_steps
    #Distributed velocities and accelerations
    Time = np.linspace(0,sim_time,num_steps)
    A = np.zeros(num_steps)
    Thrust = isp*g*mdot
    V = np.zeros(num_steps,dtype = 'int64')
    Dy = np.zeros(num_steps,dtype = 'int64')
    Drag = np.zeros(num_steps,dtype = 'int64')
    mass = np.zeros(num_steps)
    pitchover_time = 0
    term_velo_time = 0
    total_flight_time = 0
    imp_times = [pitchover_time,term_velo_time,total_flight_time]
    switch = True
    for i in range(Time.size):
    
        if (i == 0):
            V[i] = 0
            Drag[i] = 0
            Dy[i] = 0
            mass[i] = mcrafti
            A[i] = Thrust - Drag[i] - mass[i]*g
        elif(Time[i] < ((mcrafti-mcraftf)/mdot)):
            mass[i] = mcrafti - Time[i]*mdot
            Drag[i] = .5*ro*(V[i-1]**2)*Cd*rock_cross_area
            A[i] = Thrust - Drag[i] - mass[i]*g
            V[i] = V[i-1] + A[i-1]*(delta_t)
            Dy[i] = Dy[i-1] + V[i-1]*delta_t + .5*A[i-1]*delta_t**2
        elif (Time[i] > ((mcrafti-mcraftf)/mdot)):
            Thrust = 0
            mass[i] = mcraftf
            Drag[i] = .5*ro*(V[i-1]**2)*Cd*rock_cross_area
            
            V[i] = V[i-1] + A[i-1]*(delta_t)
            if (V[i-5] > 0 and V[i] < 0):
                pitchover_time = Time[i]
            if (Time[i] > 10 and V[i-1]== V[i] and switch == True):
                term_velo_time = Time[i]
                print(V[i])
                switch = False
            if (V[i] >= 0):
                A[i] = -Drag[i] - mass[i]*g
            else:
                A[i] = Drag[i] - mass[i]*g 
            Dy[i] = Dy[i-1] + V[i-1]*delta_t + .5*A[i-1]*delta_t**2
            if (Dy[i] <= 0):
                total_flight_time = Time[i]
                break
            
    
    
    
    d_to_use = {'Acceleration': A, 'Velocity':V,'Distance':Dy,'Time':Time}
    checker = pd.DataFrame(data = d_to_use)
    return checker
#forces to include
#Thrust = isp*g*mdot
#Drag = Cd * (ro * V**2)/2
#print(checker)

#plotting
#plt.figure(1)
#plt.plot(Time,A,'b')
#plt.figure(2)
#plt.plot(Time,Dy,'r')
#plt.figure(3)
#plt.plot(Time,V,'c')
#
#for i in imp_times: print(i)