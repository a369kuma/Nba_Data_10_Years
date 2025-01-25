import numpy as np
import pandas as pd
import random
import time


teams = [
    'atl', 'bos', 'brk', 'cho', 'chi', 'cle', 'dal', 
    'den', 'det', 'gsw', 'hou', 'ind', 'lac', 'lal', 
    'mem', 'mia', 'mil', 'min', 'nop', 'nyk', 'okc', 
    'orl', 'phi', 'pho', 'por', 'sac', 'sas', 'tor', 
    'uta', 'was'
]

seasons = [
    '2014', '2015', '2016', '2017', '2018',
    '2019', '2020', '2021', '2022', '2023', '2024'
]

stats = [
    'FG', 'FGA', 'fg%', 
    '3P', '3PA', '3P%',
    'FT', 'FTA', 'FT%',
    'ORB', 'TRB', 'AST',
    'STL', 'BLK', 'TOV',
    'PF'
]

tm_stats_dictionary = {stat: 'Tm_' + str(stat) for stat in stats}
opp_stats_dictionary = {stat + '.1': 'Opp_' + str(stat) for stat in stats}

# Data frame to append into
nba_Data_Frame = pd.DataFrame()

for season in seasons:
    for team in teams:
        url = f'https://www.basketball-reference.com/teams/{team}/{season}/gamelog/'
        print(url)

        try:
            team_df = pd.read_html(url, header=1, attrs={'id': 'tgl_basic'})[0]
            team_df = team_df[(team_df['Rk'].str != '') & (team_df['Rk'].str.isnumeric())]
            team_df = team_df.drop(columns=['Rk', 'unnamed: 24'])

            team_df = team_df.rename(columns={'unnamed: 3': 'Home', 'Tm': 'tm_pts', 'opp.1': 'Opp_pts'})
            team_df = team_df.rename(columns=tm_stats_dictionary)
            team_df = team_df.rename(columns=opp_stats_dictionary)

            team_df['Home'] = team_df['Home'].apply(lambda x: 0 if x == '@' else 1)

            team_df.insert(loc=0, column='Season', value=season)
            team_df.insert(loc=1, column='Team', value=team.upper())

            nba_Data_Frame = pd.concat([nba_Data_Frame, team_df], ignore_index=True)

            # Pause to respect scraping limits
            time.sleep(random.randint(4, 6))
        except Exception as e:
            print(f"Error fetching data for {team} in {season}: {e}")
            continue

print(nba_Data_Frame)
nba_Data_Frame.to_csv('nba-gamelogs-2014-2024.csv', index=False)