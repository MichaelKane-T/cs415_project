#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb 2, 2020

@author: Michael Kane

"""
import pandas as pd
import requests
import json

# Import your Django models
from models import Player, Team

def fpl_to_database():
    # Navigate to FPL website
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

    # Get raw data dump from FPL website
    response = requests.get(url)
    json_blob = json.loads(response.text)

    # Get only a subset of the Player Info json blob imbedded in the response
    player_json_blob = json_blob['elements']

    # Create a map of positions using their id and shortname
    position_json_blob = json_blob['element_types']
    pos_map = {pos['id']: pos['singular_name_short'] for pos in position_json_blob}

    # Create a map of teams using their id and shortname
    team_json_blob = json_blob['teams']
    team_map = {team['id']: team['short_name'] for team in team_json_blob}

    # Get just the columns that we care about
    df = pd.DataFrame(player_json_blob)
    player_df = df[['id', 'first_name', 'second_name', 'team', 'points_per_game', 'total_points', 'goals_scored', 'assists', 'clean_sheets', 'form', 'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'chance_of_playing_next_round']]

    # Replace all team and position numerical values in player dataframe with their corresponding values per pos_map and team_map
    player_df = player_df.replace({'team': team_map})
    player_df.sort_values('id', axis=0, ascending=True, inplace=True, na_position='last')
    player_df['Cost'] = player_df['now_cost'] / 10
    player_df.drop(['now_cost'], axis=1, inplace=True)
    player_df = player_df.rename(columns={'element_type': 'position'})

    # Iterate over the players and save them to the Player model
    for index, row in player_df.iterrows():
        team_name = row['team']
        team_obj, created = Team.objects.get_or_create(team_name=team_name)
        player_data = {
            'first_name': row['first_name'],
            'second_name': row['second_name'],
            'points_per_game': row['points_per_game'],
            'total_points': row['total_points'],
            'goals_scored': row['goals_scored'],
            'team': team_obj,
            'assists': row['assists'],
            'form': row['form'],
            'clean_sheets': row['clean_sheets'],
            'chance_of_playing_next_round': row['chance_of_playing_next_round'],
            'yellow_cards': row['yellow_cards'],
            'red_cards': row['red_cards'],
            'saves': row['saves'],
            'penalties_missed': row['penalties_missed'],
        }
        Player.objects.create(**player_data)

   

# Allows users to just run this file as a script vs importing the function into a separate python script
fpl_to_database()
