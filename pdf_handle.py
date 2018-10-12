import matplotlib
matplotlib.use('Agg')
import glob, os
import fpdf
import subprocess

LDEL=[1.667958427430881629e+00,1.522900114878828148e+00,1.151546309924921196e+01,1.532992615830861105e+00,4.175239836186649178e+00,2.483874343841527832e+00,1.667958427430881629e+00,5.296180005789425493e+00,5.292735468565884283e+00,5.887607147947949038e+00,3.094010222699058943e+01,5.887607147947949038e+00,3.094010222699058943e+01,2.111153692880986255e-01,1.527426622719958438e+00,2.424594082041503784e-01,2.137148680748577334e+00,1.687655387647762462e+00,2.628922435304935856e+00,7.862629802022850223e-01,1.656005059586740380e+00,3.082841286410143225e-02,2.358007396013581669e-01,1.670856696292321031e-01,3.314948970917179082e-05,1.731463658319559002e-04,1.370786550827642059e-01]

cons_cases=['11','22','31','52'] 
cases_ends=['NTM','NTM','NTM','NTM']

strsfigs = ["" for x in range(len(cons_cases))] 
for case in range(0,len(cons_cases)):
    strsfigs[case]='DLC'+cons_cases[case]+'_'+cases_ends[case]+'/FiguresDLC'+cons_cases[case]
    
my_path = os.getcwd() 

# Create the pdf
from fpdf import FPDF
title = 'ti'
author='N'
turbineModel='VA'

pdf = FPDF()
pdf.set_title(title)
pdf.set_author(author)

#Cover Page
pdf.add_page()
pdf.set_font('Arial','B',20.0) 
epw = pdf.w - 2*pdf.l_margin #effective page width
pdf.ln(20)
pdf.cell(epw,0.0, title, align='C')
pdf.ln(80)
pdf.set_font('Arial','B',50.0)
pdf.cell(epw,0.0, turbineModel, align='C')
pdf.ln(150)
pdf.set_font('Arial','',15.0) 
pdf.cell(epw,0.0, author, align='R')
print('Generating the pdf')

# LDEL table
pdf.add_page()
col_width = epw/4 
pdf.set_font('Arial','',15.0)  
pdf.ln(15)
pdf.cell(epw,0.0, 'Lifetim', align='C')
pdf.ln(10)
th = pdf.font_size
pdf.set_font('Arial','',10.0) 
channels_names=['RotTorq','LSShftFxa','RotPwr','RootFzc1','RootMxb1','RootMyb1','LSShftMxa','LSSGagMya','LSSGagMza','TwrBsMxt','TwrBsMyt','TwrBsMxt','TwrBsMyt','YawBrFzn','YawBrFxp','YawBrFyp','YawBrMzn','YawBrMxp','YawBrMyp','RootFxb1','RootFyb1','RootMzc1','LSShftFys','LSShftFzs','Q_DrTr','QD_DrTr','LSSTipVxa']
channels_units= ['(kN-m)','(kN)','(kW)','(kN)','(kN-m)','(kN-m)','(kN-m)','(kN-m)','(kN-m)','(kN-m)','(kN-m)','(kN-m)','(kN-m)','(kN)','(kN)','(kN)','(kN-m)','(kN-m)','(kN-m)','(kN)','(kN)','(kN-m)','(kN)','(kN)','(rad)','(rad/s)','(rpm)']
chnindx=0
for row in LDEL:
    pdf.cell(col_width/2, th, str(channels_names[chnindx]), border=1)
    pdf.cell(col_width/2, th, str(channels_units[chnindx]), border=1)
    pdf.cell(col_width, th, str(row), border=1) 
    chnindx=chnindx+1
    pdf.ln(th)
pdf.ln(4*th)
print('Generated cover page and LDEL table')
eno=0
print(pdf.w,pdf.h)
#for DLCcase in range(0,len(strsfigs)):
for DLCcase in range(0,1):        
    # Change directory to current considered load case and go to figures directory
    os.chdir(strsfigs[DLCcase])
    print('Generating graphs for:')
    print(strsfigs[DLCcase])
    for fig_name in glob.glob('*.png'):
        if eno==1:
            break
        pdf.add_page()
        pdf.image(fig_name,w=25*25*0.3, h=15*25*0.3) 
        print(fig_name)
        eno=eno+1
    os.chdir(my_path)

pdf.output('fatigueProto1.pdf','F')

subprocess.call(["pdftk", "fat1.pdf" ,"fat2.pdf", "cat", "output", "fat.pdf"])
