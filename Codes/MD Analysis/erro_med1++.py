#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:31:04 2022

@author: gutembergue
"""

import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns

df = pd.read_csv('rmsfrbd.csv')
df.head()
x = df['resnumber']
med1 = df['Med++']
stdev1 = df['Stdev++']
med2 = df['Med+-']
stdev2 = df['Stdev+-']
med3 = df['Med-+']
stdev3 = df['Stdev-+']
med4 = df['Med--']
stdev4 = df['Stdev--']

plt.plot(x, med1, '#FF8000', label='+ +')
plt.fill_between(x, med1-stdev1, med1+stdev1, color='#FF8000', alpha=0.3)
                 
plt.plot(x, med4, '#0000CD', label='- -')
plt.fill_between(x, med4-stdev4, med4+stdev4, color='#0000CD', alpha=0.3)                 
                
plt.plot(x, med2, '#008000', label='+ -')
plt.fill_between(x, med2-stdev2, med2+stdev2, color='#008000', alpha=0.3)
                 
# plt.fill_between(x, med3-stdev3, med3+stdev3, color='#FF0000', alpha=0.3)
                 
plt.ylabel('RMSF($\AA$)', fontsize=14, fontweight='bold')
plt.xlabel('Residues', fontsize=14, fontweight='bold')
plt.title('RBD', fontsize=32, color='#C2C2C2', fontweight='bold')
plt.ylim(0.0,5.0)
plt.xlim(438,508)
plt.tight_layout()

#display plot 
plt.legend(title='Mutations')
plt.savefig('rmsfartigo.svg', dpi= 600,  bbox_inches='tight')

plt.show()