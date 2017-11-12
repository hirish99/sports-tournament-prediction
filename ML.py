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

#The point of ML.py is to input a year, and give back relevant stats for each
#team during that year. This creates our label (input) dataframes.

team_id = 1102
year = 2005
'''
stat = 'Wscore'
'''

#Gives a table with 2 columns: Number of losses and Number of Wins
'''
year_data = reg_season.loc[[year],:]

wins_year = year_data['Wteam'].value_counts(dropna = True).to_frame()
wins_year.rename(team_mappings, inplace=True)
wins_year = wins_year.sort_index()

loss_year = year_data['Lteam'].value_counts(dropna = True).to_frame()
loss_year.rename(team_mappings, inplace=True)
loss_year = loss_year.sort_index()
'''

table = returnYear(year)


table['Y'] = wlr(year)

table = table[table['Y'] >= 0]
table.sort_values('Y', ascending = False, inplace = True)

'''

table.fillna(0, inplace = True);

X = table.drop('W', axis = 1)

lm = LinearRegression()

lm.fit(X, table.W)

prediction = lm.predict(X)
#realval = ((table.W).to_frame()).as_matrix()

#Adds extra columns to previous table about relevant stats
reg_season = pd.read_csv("./data/RegularSeasonDetailedResults.csv", index_col = 2)
reg_season.rename(team_mappings, inplace=True)
reg_season = reg_season.sort_index()

#Take the subset of our particular team
reg_season = reg_season.loc[team_mappings[team_id],:]
reg_season = reg_season[reg_season['Season'] == year]

#Average of the team we want:
avg = (reg_season.mean()).to_frame()
avg = avg.rename(columns = {0:team_mappings[team_id]})

#Particular Stat
#table[stat] = np.nan
#table.set_value(team_mappings[team_id], stat ,avg[team_mappings[team_id]][stat])


'''

