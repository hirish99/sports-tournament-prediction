import pandas as pd

def wlr(year):
    tourney = pd.read_csv("./data/TourneyCompactResults.csv", index_col = 0)

    teams = pd.read_csv("./data/Teams.csv", index_col = 0)

    tourney_2015 = tourney.loc[[year],:]

    wins_2015 = tourney_2015['Wteam'].value_counts().to_frame()

    losses_2015 = tourney_2015['Lteam'].value_counts(dropna = True).to_frame()

    team_mappings = pd.DataFrame.to_dict(teams)
    team_mappings = team_mappings['Team_Name']

    wins_2015.rename(team_mappings, inplace=True)
    losses_2015.rename(team_mappings, inplace=True)

    wins_2015.columns = ['Wins']

    losses_2015.columns = ['Losses']

    Z = pd.concat([wins_2015,losses_2015], 1)
    Z.fillna(value = 0, inplace = True)
    Z1 = Z['Wins'].to_frame()
    return Z1;
