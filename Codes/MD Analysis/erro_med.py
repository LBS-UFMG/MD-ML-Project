#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:31:04 2022

@author: gutembergue
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as pl
import seaborn as sns

df = pd.read_csv('rmsfrbm-+.csv')
df.head()
x = df['resnumber']
med1 = df['Med-+']
stdev1 = df['Stdev-+']
pl.plot(x, med1, '#1E90FF', label='- +')
pl.fill_between(x, med1-stdev1, med1+stdev1, color='#1E90FF', alpha=0.3)
#plt.plot(x, mean_2, 'r--', label='mean_2')
#plt.fill_between(x, mean_2 - std_2, mean_2 + std_2, color='r', alpha=0.2)
pl.ylabel('RMSF($\AA$)', fontsize=14, fontweight='bold')
pl.xlabel('Resíduos', fontsize=14, fontweight='bold')
pl.title('RBM(-+)', fontsize=30, color='#C2C2C2', fontweight='bold')
pl.ylim(0,5.0)
pl.xlim(438,508)
pl.tight_layout()
#display plot 
pl.legend(title='Mutações')
pl.savefig('rmsfrbm-+.svg', dpi= 600,  bbox_inches='tight')

pl.show()