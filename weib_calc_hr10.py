# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:16:47 2018

@author: Hassan
"""

import numpy as np
import scipy
from scipy import stats
from scipy.stats import weibull_min
from scipy.integrate import simps

def weib_calc_uni(st=1,beg=3,end=25,shape=2,scal=7.5,nwang=3,rep=3,wdirprob=[0.5,0.25,0.25],pdlc=0.975,nyears=20):
    n=int((end-beg)/st+1)

    areas=[0.154280014,0.206081225,0.20700702,0.170956289,0.120150479,0.073096804,0.038868449,0.018173172,0.007501222,0.002741008,0.000888469,0.000255849]     
     
    wbs=np.zeros(n)
    if st==1:
        for x in range(0, n):
            wbs[x]=weibull_min.pdf(x+beg, shape, scale=scal)           
    if st==2:
        ## sub is value to subtract from begin speed to find index of first area
        sub=int(0.5*beg+1.5)
        sub=beg-sub
        for cnt in range(0, n):
            wbs[cnt]=areas[sub] 
            sub=sub+1     
           
    probs=[wbs[0]]*rep*nwang
    for cnt in range(1,n):
        temp=[wbs[cnt]]*rep*nwang
        for cnt1 in range(0,rep*nwang):
            probs.append(temp[cnt1])
    
  
    
    temp=wdirprob
    pwdir=temp
    for cnt in range(0,rep*n-1):
        for cnt1 in range(0,nwang):
            pwdir.append(temp[cnt1])
    

    for x in range(0, len(probs)):
        print(pwdir[x])
     
    Nr_speed=[1.0/rep]*len(probs)
     
    P=[pdlc]*len(probs)
    
    hours=np.zeros(len(probs))
    
    for cnt in range(0,len(probs)):
        hours[cnt]=probs[cnt]*pwdir[cnt]*Nr_speed[cnt]*P[cnt]*24*365*nyears*6
             
    return hours



def weib_calc_mixd(stfst=1,strang=[3,12,13,25],shape=2,scal=7.5,nwang=3,rep=3,wdirprob=[0.5,0.25,0.25],pdlc=0.975,nyears=20):
    if stfst==1:
        n=int(strang[1]-strang[0]+(strang[3]-strang[2])/2+2)
    if stfst==2:
        n=int(strang[3]-strang[2]+(strang[1]-strang[0])/2+2)        

    
    areas=[0.154280014,0.206081225,0.20700702,0.170956289,0.120150479,0.073096804,0.038868449,0.018173172,0.007501222,0.002741008,0.000888469,0.000255849]     

    wbs=np.zeros(n)
    if stfst==1:
        for x in range(0,strang[1]-strang[0]+1 ):
            wbs[x]=weibull_min.pdf(x+strang[0], shape, scale=scal)
        sub=int(0.5*strang[2]+1.5)
        sub=strang[2]-sub
        for cnt in range(strang[1]-strang[0]+1, n):
            wbs[cnt]=areas[sub]
            sub=sub+1
            
    if stfst==2:
        sub=int(0.5*strang[0]+1.5)
        sub=strang[0]-sub
        for cnt in range(0,strang[1]-strang[0]+1 ):
            wbs[cnt]=areas[sub]
            sub=sub+1
        dumcnt=0
        for x in range(strang[1]-strang[0]+2, n):
            wbs[x]=weibull_min.pdf(strang[2]+dumcnt, shape, scale=scal)
            dumcnt=dumcnt+1

    probs=[wbs[0]]*rep*nwang
    for cnt in range(1,n):
        temp=[wbs[cnt]]*rep*nwang
        for cnt1 in range(0,rep*nwang):
            probs.append(temp[cnt1])
            
    temp=wdirprob
    pwdir=temp
    for cnt in range(0,rep*n-1):
        for cnt1 in range(0,nwang):
            pwdir.append(temp[cnt1])
            
    Nr_speed=[1.0/rep]*len(probs)
     
    P=[pdlc]*len(probs)
    
    hours=np.zeros(len(probs))
    
    for cnt in range(0,len(probs)):
        hours[cnt]=probs[cnt]*pwdir[cnt]*Nr_speed[cnt]*P[cnt]*24*365*nyears*6
             
    return hours

txts=weib_calc_mixd()
