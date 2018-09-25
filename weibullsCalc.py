# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 15:52:00 2018

@author: Hassan
"""
import numpy as np
import scipy
from scipy import stats
from scipy.stats import weibull_min
from scipy.integrate import simps

def weib_calc(n=25,shape=2,scale=7.5):
    pdfs=np.zeros(n)
    x=np.linspace(1,n,n)
    for elem in range(0,n):
        pdfs[elem]=(shape/scale)*((x[elem]/scale)**(shape-1))*np.exp(-(x[elem]/scale)**shape)
    return pdfs

xs=np.arange(1,25,0.01)
pdfss=np.zeros(len(xs))
for cnt in range(0,2400):
        pdfss[cnt]=(2/7.5)*((xs[cnt]/7.5)**(2-1))*np.exp(-(xs[cnt]/7.5)**2)
areas=np.zeros(12)
addv=0
for cnt in range(0,11):
    areas[cnt] = simps(pdfss[(cnt+addv+1)*100:(cnt+3+addv)*100], dx=.01)
    addv=addv+1
areas[11] = simps(pdfss[2300:2400], dx=.01)*2
     
     
     
     
     
     
     
     
     
     
# 3 - 13 step of 1 and 13 - 25 step of 2 

wbs=np.zeros(17)
for x in range(3, 13):
    wbs[x-3]=weibull_min.pdf(x, 2, scale=7.5)
for cnt in range(10, 17):
    wbs[cnt]=areas[cnt-5]

probs=[wbs[0]]*9
for cnt in range(1,17):
    temp=[wbs[cnt]]*9
    for cnt1 in range(0,9):
        probs.append(temp[cnt1])
        
temp=[0.5,0.25,0.25]
pwdir=temp
for cnt in range(0,50):
    for cnt1 in range(0,3):
        pwdir.append(temp[cnt1])
        
Nr_speed=[0.3333333]*207
 
P=[0.975]*207

hours=np.zeros(153)

for cnt in range(0,153):
    hours[cnt]=probs[cnt]*pwdir[cnt]*Nr_speed[cnt]*P[cnt]*24*365*20*6

#for cnt in range(0,207):
#    print(hours[cnt])         
         