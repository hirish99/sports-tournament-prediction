import pandas as pd

year = 2005
reg_season = pd.read_csv("./data/RegularSeasonDetailedResults.csv", index_col = 2)
teams = pd.read_csv("./data/Teams.csv", index_col = 0)
team_mappings = pd.DataFrame.to_dict(teams)
team_mappings = team_mappings['Team_Name']
reg_season.rename(team_mappings, inplace = True)
reg_season = reg_season.sort_index()


table = None


reg_season = reg_season[reg_season['Season'] == year]

def returnRow(team_name, reg_season):
    team_data = reg_season.loc[team_name,:]
    avg = (team_data.mean()).to_frame()
    avg = avg.rename(columns = {0:team_name})
    avg = avg.transpose()
    return avg


j = ""
k = 0
for i in reg_season.index:
    if k == 0:
        k = 1
        print(i)
        table = returnRow(i, reg_season)
        j = i
    if k == 1 and j!=i:
        print(i)
        table = pd.concat([table, returnRow(i, reg_season)])
        j = i



