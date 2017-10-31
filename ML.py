import pandas as pd
reg_season = pd.read_csv("./data/RegularSeasonDetailedResults.csv", index_col = 0)
teams = pd.read_csv("./data/Teams.csv", index_col = 0)
team_mappings = pd.DataFrame.to_dict(teams)
team_mappings = team_mappings['Team_Name']

team_id = 1228
year = 2005

#Gives a table with 2 columns: Number of losses and Number of Wins
year_data = reg_season.loc[[year],:]

wins_year = year_data['Wteam'].value_counts(dropna = True).to_frame()
wins_year.rename(team_mappings, inplace=True)
wins_year = wins_year.sort_index()

loss_year = year_data['Lteam'].value_counts(dropna = True).to_frame()
loss_year.rename(team_mappings, inplace=True)
loss_year = loss_year.sort_index()

table = pd.concat([wins_year, loss_year], axis = 1)

#Adds extra columns to previous table about relevant stats
reg_season = pd.read_csv("./data/RegularSeasonDetailedResults.csv", index_col = 2)
reg_season.rename(team_mappings, inplace=True)
reg_season = reg_season.sort_index()

#Take the subset of our particular team
reg_season = reg_season.loc[team_mappings[team_id],:]
reg_season = reg_season[reg_season['Season'] == year]
avg = reg_season.mean()
