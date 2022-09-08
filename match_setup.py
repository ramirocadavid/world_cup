# Match setup and configuration classes

from subprocess import call
from images import *

class Match:
    """
    Represents the match in which the shootout will be played. Contains data on 
    the setup of the game and keeps track of its status and results.
    """

    def __init__(self, team1, team2, players1, players2):
        # Teams and players
        self.teams = [team1, team2]
        self.team_1 = team1
        self.team_2 = team2
        self.players_1 = players1
        self.players_2 = players2
        # Shooters
        self.shooters_1 = []
        for player in self.players_1:
            if player.type == 1:
                self.shooters_1.append(player)
        self.shooters_2 = []
        for player in self.players_2:
            if player.type == 1:
                self.shooters_2.append(player)
        self.shooters = [self.shooters_1, self.shooters_2]
        # Goalies
        self.goalies = []
        for player in self.players_1:
            if player.type == 2:
                self.goalies.append(player)
                break
        for player in players2:
            if player.type is 2:
                self.goalies.append(player)
                break
        # Status
        self.kicks_num = 0
        self.kicking_team = 1
        self.score = [0, 0]
        self.winner = None
    
    @staticmethod
    def match_setup(teams, players):
        """
        Method to setup a match, including the participating teams and players
        within each team
        """
        # Select teams
        print(team_image)
        print("SELECT TEAMS!")
        print()
        while True:
            for t in range(len(teams)):
                print('[', t, ']: ', teams[t].name, sep='', end='\n')
            print()
            team_1_index = input("Select team 1: ")
            team_2_index = input("Select team 2: ")
            if team_1_index == team_2_index:
                print()
                print("Team 1 has to be different than Team 2")
                print()
                continue
            valid = [str(i) for i in range(len(teams))]
            if team_1_index not in valid or team_2_index not in valid:
                print()
                print("Select a valid team!")
                print()
                continue
            team_1 = teams[int(team_1_index)]
            team_2 = teams[int(team_2_index)]
            call(["clear"])
            break
        
        # Select Team 1 players
        print("CHOOSE TEAM 1 PLAYERS (", team_1.name.capitalize(), ")", sep='')
        print(player_image)
        print()
        while True:
            # Request input
            print()
            players_available_1 = []
            count = 0 
            for player in players:
                if player.team.name == team_1.name:
                    players_available_1.append(player)
                    print('[', count, '] ', player, sep='', end='\n')
                    count += 1
            print()
            players_1_index = input(
                "Select players (enter consecutive numbers): "
                )
            # Validate input
            valid = range(len(players_available_1))
            if not set([int(p) for p in list(players_1_index)]).issubset(set(valid)):
                print()
                print("Select only players available!")
                continue
            players_1 = [players_available_1[int(i)] for i in list(players_1_index)]
            if len(players_1) < 6:
                print()
                print("Choose at least 6 players (one goalie and 5 shooters)")
                continue
            elif 2 not in [p.type for p in players_1]:
                print()
                print("Include a golie in your selection!")
                continue
            print()
            print("Players added to", team_1.name, ":")
            for player in players_1:
                print(player)
            print()
            input("Press enter to continue")
            call(["clear"])
            break
        
        # Select Team 2 players
        print("CHOOSE TEAM 2 PLAYERS (", team_2.name.capitalize(), ")", sep='')
        print(player_image)
        print()
        while True:
            # Request input
            print()
            print(team_2.name.capitalize())
            players_available_2 = []
            count = 0 
            for player in players:
                if player.team.name == team_2.name:
                    players_available_2.append(player)
                    print('[', count, '] ', player, sep='', end='\n')
                    count += 1
            print()
            players_2_index = input(
                "Select players (enter consecutive numbers): "
                )
            # Validate input
            valid = range(len(players_available_2))
            if not set([int(p) for p in list(players_2_index)]).issubset(set(valid)):
                print()
                print("Select only players available!")
                continue
            players_2 = [players_available_2[int(i)] for i in list(players_2_index)]
            if len(players_2) < 6:
                print()
                print("Choose at least 6 players (one goalie and 5 shooters)")
                continue
            elif 2 not in [p.type for p in players_2]:
                print()
                print("Include a golie in your selection!")
                continue
            print()
            print("Players added to", team_2.name, ":")
            for player in players_2:
                print(player)
            print()
            input("Press Enter to continue")
            call(["clear"])
            break
        
        # Create match
        match = Match(team_1, team_2, players_1, players_2)
        return match
    
    @staticmethod
    def quick_match(t1, t1_players, t2, t2_players):
        """Sets up a quick match, where the teams and players are automatically selected"""
        print()
        match = Match(t1, t2, t1_players, t2_players)
        return match
