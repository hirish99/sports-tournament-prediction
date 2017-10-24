import pandas as pd
import matplotlib.pyplot as plt

reg_season = pd.read_csv("./data/RegularSeasonDetailedResults.csv")
teams = pd.read_csv("./data/Teams.csv", index_col=0)

team_mappings = pd.DataFrame.to_dict(teams)
team_mappings = team_mappings['Team_Name']

reg_season_2003 = reg_season[(reg_season.Season == 2003)]
wins = reg_season_2003.groupby('Wteam')
losses = reg_season_2003.groupby('Lteam')
reg_season_2003 = reg_season_2003.sort_values('Wteam')
print(reg_season_2003)


#fg, 3pt
