# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:54:24 2018

@author: scott.gee
"""
import simulator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import math
import tkinter
###creating rocket objects so functions will be made for it

class Rocket:
    def __init__(self,isp,final_mass,initial_mass,rock_diameter,CD):
        self.isp = isp
        self.massf = final_mass
        self.massi = initial_mass
        self.rocket_diam = rock_diameter
        self.Cd = CD
    
    #@staticmethod 
    def trajectory_solve(self):
        traj_df = simulator.traj_solve(self.isp,self.massf,self.massi,self.rocket_diam,self.Cd)
        self.Dy = traj_df["Distance"]
        self.Velo = traj_df["Velocity"]
        self.Accel = traj_df['Acceleration']
        self.Time = traj_df['Time']
        
    def plotter(self, *args):
        index = 0
        for parameter in args:
            plt.figure(index)
            plt.plot(self.Time,parameter)
            plt.xlabel("Time (s)")
            plt.ylabel(parameter.name)
            title_string = str(parameter.name) + " Vs Time"
            plt.title(title_string)
            index = index + 1
            
    def term_velo(self):
        cross_area = (self.rocket_diam**2)*math.pi/4
        term_velo = ((2*self.massf*9.81)/(self.Cd*1.225*cross_area))**(1/2)
        print(term_velo)
        return term_velo
    @staticmethod
    def vary_attribute():
        window = tkinter.Tk()
        window.mainloop()
            
#Model = Rocket(50,35,50,.1,.06)
#Model.trajectory_solve()
#Model.plotter(Model.Velo,Model.Accel)
#Model.term_velo()
#Rocket.vary_attribute()