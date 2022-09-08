# Team setup and configuration classes 

from images import * 

class Team:
    """
    Represents a team that can be chosen to play in a match. Contains data of 
    the team name, the players available and the times the team has won.
    """
    teams = []

    def __init__(self, name):
        if name in [team.name for team in Team.teams]:
            raise Exception("Team name already exist. Enter a different name")
        self.name = name
        self.players = [] 
        self.wins = 0
        Team.teams.append(self)

    def __repr__(self):
        """Returns the name of the team capitalized"""
        return self.name.capitalize()
    
    @classmethod
    def list_teams(cls):
        """List the teams available, formatted"""
        print("TEAMS")
        print(team_image)
        for team in cls.teams:
            print("  ", team.name, end='\n')
        print()
        input("Press Enter to Main menu")


class Player:
    """ 
    Represents a player that can be included in a team. Contains name, ability,
    type and team.
    """
    players = []

    def __init__(self, name=None,  ability=None, type=None, team=None):
        if name in [player.name for player in Player.players]:
            raise Exception("Player name already exists")
        if ability < 0 or ability > 10:
            raise Exception("Ability must be between 0 and 10")
        if type not in [1, 2]:
            raise Exception("Type must be 1 or 2")
        else:
            self.name = name
            self.team = team
            self.ability = ability
            self.type = type
        Player.players.append(self)
    
    def __str__(self):
        """Returns formatted information of player"""
        type = None
        if self.type == 1:
            type = 'Shooter'
        elif self.type == 2:
            type = 'Goalie'
        return "    {0:<25s} {1:<10s} {2:<35s}".format(self.name, str(type), self.team.name)

    @classmethod
    def list_players(cls):
        """Lists all the players created in this class, formatted"""
        print("PLAYERS")
        print(player_image)
        print("    {0:<25s} {1:<10s} {2:<35s}".format("NAME", "TYPE", "TEAM"))
        for player in cls.players:
            print(player)
        # print("-" * 73)
        print()
        input("Press Enter to Main menu")