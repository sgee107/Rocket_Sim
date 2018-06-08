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
    
    #Initialize the class with all of its thrust properties and immediately develop trajectory of rocket
    def __init__(self,isp,final_mass,initial_mass,rock_diameter,CD):
        self.isp = isp
        self.massf = final_mass
        self.massi = initial_mass
        self.rocket_diam = rock_diameter
        self.Cd = CD
        self.traj_solve(self.isp,self.massf,self.massi,self.rocket_diam,self.Cd)
        
    def traj_solve(self,isp,massf,massi,rocket_diam,Cd):
        traj_df = simulator.traj_solve(self.isp,self.massf,self.massi,self.rocket_diam,self.Cd)
        self.Dy = traj_df["Distance"]
        self.Velo = traj_df["Velocity"]
        self.Accel = traj_df['Acceleration']
        self.Time = traj_df['Time']
        self.traj_df = traj_df

        
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
    
    def vary_attribute():
        input1 = input("What variable would you like to alter?: isp,Cd,Initial Mass, Final Mass, Rocket Diameter: ")
        input1 = input1.lower()
        
        window = tkinter.Tk()
        window.mainloop()
        
    def get_features(self):
        max_height = 0
        max_velo = 0
        pitchover_time = 0
        total_flight_time = 0
        length = self.traj_df.shape[0]
        
        for i in range(length):
            if (i > 0):
                if (self.Dy[i]>self.Dy[i-1]):
                    max_height = self.Dy[i]
                if (self.Velo[i] < 0 and self.Velo[i-1] > 0):
                    pitchover_time = self.Time[i]
                if (self.Velo[i]>self.Velo[i-1]):
                    max_velo = self.Velo[i]
                if ( i > 500 and self.Dy[i] <= 0):
                    total_flight_time = self.Time[i]
                    break
        feature_dict  = {"max_height":max_height,"max_velo":max_velo,"pitchover_time":pitchover_time,"total_flight_time":total_flight_time}
        return feature_dict
    
    @staticmethod
    def compare_rocket(self,*args):
        for one_object in args:
            self.plotter(one_object.Dy,one_object.Velo,one_object.Accel)
        



###################### test program #########################        
Model = Rocket(50,35,50,.1,.06)
#Model.trajectory_solve()
Model.plotter(Model.Dy,Model.Velo,Model.Accel)
feature_print = Model.get_features()
Model2 = Rocket(50,40,50,.05,.15)
Model3 = Rocket(50,40,50,.15,.4)
#Model2.trajectory_solve()
Rocket.compare_rocket(Model,Model2,Model3)
#Model.term_velo()
#Rocket.vary_attribute()