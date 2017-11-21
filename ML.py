import pandas as pd
import numpy as np
from winlossratio import wlr
from badstats import returnlYear
from stats import returnYear
import sklearn
from sklearn.linear_model import LinearRegression

year = 2003
table = returnYear(year)
#table['Y'] = wlr(year)


#table.fillna(value = -1, inplace = True)
#table = table[table['Y'] != -1]

#Y = table.Y

X = table
X.drop(['Lteam', 'Lscore', 'Daynum', 'Season', 'Lftm', 'Lfta', 'Lor', 'Ldr', 'Last', 'Lto', 'Lstl', 'Lblk', 'Lpf', 'Lfgm', 'Lfga', 'Lfgm3', 'Lfga3'], axis = 1, inplace = True)
X1 = returnlYear(year)
l = ['Lscore', 'Numot', 'Lfga3', 'Lftm', 'Lfta', 'Lor', 'Ldr', 'Last', 'Lto', 'Lstl', 'Lblk', 'Lpf']
X1 = X1[l]
X2 = pd.concat([X, X1])

'''

lm = LinearRegression()

lm.fit(X, Y)

prediction = lm.predict(X)

Output = Y.to_frame()
Output['Prediction'] = prediction
Output['Percent Error'] = (Output['Prediction'] - Output['Y']) * 100/Output['Y']
Output.sort_values('Prediction', ascending = False, inplace = True)

'''
