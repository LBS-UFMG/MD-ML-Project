#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:31:04 2022

@author: gutembergue
"""

data_dir = "../../Files/"

# Importing necessary libraries for data manipulation and visualization
import pandas as pd
import numpy as np
from matplotlib import pyplot as pl
import seaborn as sns

# Loading data from a CSV file into a DataFrame
df = pd.read_csv(data_dir+'MD Analysis/rmsfrbm-+.csv')

# Displaying the first few rows of the DataFrame to check its structure
df.head()

# Extracting specific columns from the DataFrame for visualization
x = df['resnumber']    # Residue numbers
med1 = df['Med-+']     # Median values
stdev1 = df['Stdev-+'] # Standard deviation values

# Plotting the median values against residue numbers
pl.plot(x, med1, '#1E90FF', label='- +')

# Adding a shaded area around the median line to represent the standard deviation
pl.fill_between(x, med1-stdev1, med1+stdev1, color='#1E90FF', alpha=0.3)

# Setting labels and title for the plot with custom formatting
pl.ylabel('RMSF($\AA$)', fontsize=14, fontweight='bold')    # Y-axis label
pl.xlabel('Resíduos', fontsize=14, fontweight='bold')       # X-axis label
pl.title('RBM(-+)', fontsize=30, color='#C2C2C2', fontweight='bold')

# Setting the limits for Y and X axes for better visualization
pl.ylim(0, 5.0)    # Y-axis limits
pl.xlim(438, 508)  # X-axis limits

pl.tight_layout()

# Adding a legend for the plot to identify different lines or shaded areas
pl.legend(title='Mutações')

# Saving the plot to an SVG file with high resolution
pl.savefig('rmsfrbm-+.svg', dpi=600, bbox_inches='tight')

# Displaying the plot on screen
pl.show()
