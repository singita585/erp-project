# import module we need in order to display the csv file into chart form

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')

#The program will read the csv file that we have stored in pd.read_csv in order for us to display it in chart form
df = pd.read_csv('data.csv')

#Here we label the Income and Expenses as x any y in order to display them in bar chart form
x = df['Income']
y = df['Expenses']

#Bar chart
plt.xlabel('Income', fontsize=18)
plt.ylabel('Expenses', fontsize=16)
plt.bar(x, y)