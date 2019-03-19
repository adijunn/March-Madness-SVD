import csv
import numpy as np

class Team:
    def __init__(self, name):
        self.name = name
        self.stats = []

def get_stats():
    """Returns team stats in dictionary form and matrix form"""
    team_dict = {}
    # parse team names
    with open('../data/teams.txt') as teams:
        team_name_list = teams.readlines()
        for team in team_name_list:
            team_dict[team.rstrip()] = Team(team)

    # parse rankings
    with open('../data/rankings.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            for team_name in team_dict.keys():
                if team_name == "Northeastern" and "REB MAR" in row: # bad patch
                     team_dict[team_name].stats.append(0)
                elif team_name in row:
                    team_dict[team_name].stats.append(row[-1])
    matrix = np.array([t.stats for t in team_dict.values()])
    return team_dict, matrix 
