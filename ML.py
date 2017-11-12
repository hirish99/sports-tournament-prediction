import pandas as pd
import numpy as np
from winlossratio import wlr
from stats import returnYear
import sklearn
from sklearn.linear_model import LinearRegression

reg_season = pd.read_csv("./data/RegularSeasonDetailedResults.csv", index_col = 0)
teams = pd.read_csv("./data/Teams.csv", index_col = 0)
team_mappings = pd.DataFrame.to_dict(teams)
team_mappings = team_mappings['Team_Name']

year = 2003
table = returnYear(year)
table['Y'] = wlr(year)
table.fillna(value = -1, inplace = True)
table = table[table['Y'] != -1]

#Add loss data and
#Add more years

Y = table.Y
X = table
X.drop('Y', axis = 1, inplace = True)
X.drop('Lteam', axis = 1, inplace = True)
X.drop('Lscore', axis = 1, inplace = True)
X.drop('Daynum', axis = 1, inplace = True)
X.drop('Season', axis = 1, inplace = True)
X.drop('Lftm', axis = 1, inplace = True)
X.drop('Lfta', axis = 1, inplace = True)
X.drop('Lor', axis = 1, inplace = True)
X.drop('Ldr', axis = 1, inplace = True)
X.drop('Last', axis = 1, inplace = True)
X.drop('Lto', axis =1, inplace = True)
X.drop('Lstl', axis = 1, inplace = True)
X.drop('Lblk', axis = 1, inplace = True)
X.drop('Lpf', axis = 1, inplace = True)
#Initially did not drop:
X.drop('Lfgm', axis = 1, inplace = True)
X.drop('Lfga', axis = 1, inplace = True)
X.drop('Lfgm3', axis = 1, inplace = True)
X.drop('Lfga3', axis = 1, inplace = True)

lm = LinearRegression()

lm.fit(X, Y)

prediction = lm.predict(X)

X['Prediction'] = prediction
#X['Y'] = Y
winners = X.sort_values('Prediction', ascending = False)
