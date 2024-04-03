#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:31:04 2022

@author: gutembergue
"""

data_dir = "../../Files/"

# Importing necessary libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading data from a CSV file into a DataFrame
df = pd.read_csv(data_dir+'MD Analysis/rmsfrbd.csv') 

# Displaying the first few rows of the DataFrame to check its structure
df.head()

# Extracting data from the DataFrame for plotting
x = df['resnumber']  # The residue numbers

# Data for the first mutation type '+ +'
med1 = df['Med++']      # Median RMSF values
stdev1 = df['Stdev++']  # Standard deviation of RMSF values

# Data for the second mutation type '+ -'
med2 = df['Med+-']      # Median RMSF values
stdev2 = df['Stdev+-']  # Standard deviation of RMSF values

# Data for the third mutation type '- +'
med3 = df['Med-+']      # Median RMSF values
stdev3 = df['Stdev-+']  # Standard deviation of RMSF values

# Data for the fourth mutation type '- -'
med4 = df['Med--']      # Median RMSF values
stdev4 = df['Stdev--']  # Standard deviation of RMSF values

# Plotting the RMSF data for each mutation type
plt.plot(x, med1, '#FF8000', label='+ +')  # Orange line for '+ +' mutation
plt.fill_between(x, med1-stdev1, med1+stdev1, color='#FF8000', alpha=0.3)  # Filling the area for standard deviation

plt.plot(x, med4, '#0000CD', label='- -')  # Blue line for '- -' mutation
plt.fill_between(x, med4-stdev4, med4+stdev4, color='#0000CD', alpha=0.3)  # Filling the area for standard deviation

plt.plot(x, med2, '#008000', label='+ -')  # Green line for '+ -' mutation
plt.fill_between(x, med2-stdev2, med2+stdev2, color='#008000', alpha=0.3)  # Filling the area for standard deviation

# The data for '- +' mutation type is commented out and thus not plotted

# Setting labels, title, and formatting for the plot
plt.ylabel('RMSF($\AA$)', fontsize=14, fontweight='bold')  # Y-axis label
plt.xlabel('Residues', fontsize=14, fontweight='bold')  # X-axis label
plt.title('RBD', fontsize=32, color='#C2C2C2', fontweight='bold')  # Title of the plot

# Configuring the Y-axis and X-axis limits for better visualization
plt.ylim(0.0, 5.0)  # Y-axis limits
plt.xlim(438, 508)  # X-axis limits

# Adjusting the layout for better spacing and appearance
plt.tight_layout()

# Adding a legend for the plot to identify different mutation types
plt.legend(title='Mutations')

# Saving the plot to an SVG file with high resolution
plt.savefig('rmsfartigo.svg', dpi=600, bbox_inches='tight')

# Displaying the plot on screen
plt.show()