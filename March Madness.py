import pandas as pd

reg_season_compact_pd = pd.read_csv('C:/Users/Danyuhl/Desktop/Data Sets/sports-tournament-prediction-master/RegularSeasonCompactResults.csv')
reg_season_compact_pd.head()

teams_pd = pd.read_csv('C:/Users/Danyuhl/Desktop/Data Sets/sports-tournament-prediction-master/Teams.csv')
teamList = teams_pd['Team_Name'].tolist()

reg_season_detailed_pd = pd.read_csv('C:/Users/Danyuhl/Desktop/Data Sets/sports-tournament-prediction-master/RegularSeasonDetailedResults.csv')

seed_pd = pd.read_csv('C:/Users/Danyuhl/Desktop/Data Sets/sports-tournament-prediction-master/TourneySeeds.csv')
tourney_compact_pd = pd.read_csv('C:/Users/Danyuhl/Desktop/Data Sets/sports-tournament-prediction-master/TourneyCompactResults.csv')

def seed_convert(seed):
    s_int = int(seed[1:3])
    return s_int
seed_pd['n_seed'] = seed_pd.Seed.apply(seed_convert)
seed_pd.drop(labels = ['Seed'], inplace = True, axis = 1)

winseeds_pd = seed_pd.rename(columns = {'Team':'Wteam', 'n_seed':'WinSeed'})
lossseeds_pd = seed_pd.rename(columns = {'Team':'Lteam', 'n_seed':'LossSeed'})

dummy_pd = pd.merge(left = tourney_compact_pd, right = winseeds_pd, how = 'left', on = ['Season', 'Wteam'])
concat_pd = pd.merge(left = dummy_pd, right = lossseeds_pd, on = ['Season', 'Lteam'])
concat_pd['seed_diff'] = concat_pd.WinSeed - concat_pd.LossSeed

tourneywins_pd = pd.DataFrame()
tourneywins_pd['seed_diff'] = concat_pd['seed_diff']
tourneywins_pd['result'] = 1
