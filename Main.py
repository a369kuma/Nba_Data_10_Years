import numpy as np
import pandas as pd
import random
import time
from unidecode import unidecode

teams = [
    'atl', 'bos', 'brk', 'cho', 'chi', 'cle', 'dal', 
    'den', 'det', 'gsw', 'hou', 'ind', 'lac', 'lal', 
    'mem', 'mia', 'mil', 'min', 'nop', 'nyk', 'okc', 
    'orl', 'phi', 'pho', 'por', 'sac', 'sas', 'tor', 
    'uta', 'was'
]
len(teams)

seasons = [
    '2014', '2015', '2016', '2017', '2018'
    '2019', '2020', '2021', '2022', '2023' , '2024'
]
len(seasons)


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

# Going through seasons

for season in seasons:

    # Going through teams

    for team in teams:

        url = 'https://www.basketball-reference.com/teams' + team + '/' + season + 
