import pandas as pd
import numpy as np
from winlossratio import wlr
from badstats import returnlYear
from stats import returnYear
import sklearn
from sklearn.linear_model import LinearRegression
import time

start = time.time()


year = 2003

Y = wlr(year)

X1 = returnYear(year)
X1.drop(['Lteam', 'Lscore', 'Daynum', 'Season', 'Lftm', 'Lfta', 'Lor', 'Ldr', 'Last', 'Lto', 'Lstl', 'Lblk', 'Lpf', 'Lfgm', 'Lfga', 'Lfgm3', 'Lfga3'], axis = 1, inplace = True)
X2 = returnlYear(year)
l = ['Lscore', 'Numot', 'Lfga3', 'Lftm', 'Lfta', 'Lor', 'Ldr', 'Last', 'Lto', 'Lstl', 'Lblk', 'Lpf']
X2 = X2[l]
X = pd.concat([X1, X2], 1)
l = list(Y.index)
X = X.loc[l]

X.fillna(value = 0, inplace = True)
Y.fillna(value = 0, inplace = True)
table = pd.concat([X, Y], 1)

for year in range(2004, 2015):

    Y = wlr(year)

    X1 = returnYear(year)
    X1.drop(['Lteam', 'Lscore', 'Daynum', 'Season', 'Lftm', 'Lfta', 'Lor', 'Ldr', 'Last', 'Lto', 'Lstl', 'Lblk', 'Lpf', 'Lfgm', 'Lfga', 'Lfgm3', 'Lfga3'], axis = 1, inplace = True)
    X2 = returnlYear(year)
    l = ['Lscore', 'Numot', 'Lfga3', 'Lftm', 'Lfta', 'Lor', 'Ldr', 'Last', 'Lto', 'Lstl', 'Lblk', 'Lpf']
    X2 = X2[l]
    X = pd.concat([X1, X2], 1)
    l = list(Y.index)
    X = X.loc[l]

    X.fillna(value = 0, inplace = True)
    Y.fillna(value = 0, inplace = True)
    temp = pd.concat([X, Y], 1)
    table = pd.concat([table, temp])
    end = time.time()
    print(end - start)

lm = LinearRegression()
lm.fit(X, Y)


#Test
year = 2015

Y = wlr(year)

X1 = returnYear(year)
X1.drop(['Lteam', 'Lscore', 'Daynum', 'Season', 'Lftm', 'Lfta', 'Lor', 'Ldr', 'Last', 'Lto', 'Lstl', 'Lblk', 'Lpf', 'Lfgm', 'Lfga', 'Lfgm3', 'Lfga3'], axis = 1, inplace = True)
X2 = returnlYear(year)
l = ['Lscore', 'Numot', 'Lfga3', 'Lftm', 'Lfta', 'Lor', 'Ldr', 'Last', 'Lto', 'Lstl', 'Lblk', 'Lpf']
X2 = X2[l]
X = pd.concat([X1, X2], 1)
l = list(Y.index)
X = X.loc[l]

X.fillna(value = 0, inplace = True)
Y.fillna(value = 0, inplace = True)



prediction = lm.predict(X)
Output = Y
Output['Prediction'] = prediction
Output.to_csv("output.csv")
Output.sort_values('Prediction', ascending = False, inplace = True)
Output['Error'] = (Output['Wins'] - Output['Prediction'])**2

end = time.time()
print(end - start)
