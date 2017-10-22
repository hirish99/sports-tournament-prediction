import pandas as pd

reg_season_compact_pd = pd.read_csv('C:/Users/Danyuhl/Desktop/Data Sets/sports-tournament-prediction-master/RegularSeasonCompactResults.csv')
reg_season_compact_pd.head()

teams_pd = pd.read_csv('C:/Users/Danyuhl/Desktop/Data Sets/sports-tournament-prediction-master/Teams.csv')
teamList = teams_pd['Team_Name'].tolist()

                    
