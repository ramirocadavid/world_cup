import time
from subprocess import call
import getpass

# CONFIGURATION CLASSES

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
        self.players = None
        self.wins = 0
        Team.teams.append(self)
    
    def __repr__(self):
        """Returns the name of the team capitalized"""
        return self.name.capitalize()
    
    @classmethod
    def list_teams(cls):
        """List the teams available, formatted"""
        for team in cls.teams:
            print("  ", team.name, end='\n')
        print("-" * 73)
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
            raise Exception("Player name already exist")
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
        print("-" * 73)
        print("PLAYERS")
        print("-" * 73)
        print(player_image)
        print("    {0:<25s} {1:<10s} {2:<35s}".format("NAME", "TYPE", "TEAM"))
        for player in cls.players:
            print(player)
        print("-" * 73)
        print()
        input("Press Enter to Main menu")


# GAME SETUP CLASSES
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
    def match_setup():
        """
        Method to setup a match, including the participating teams and players
        within each team
        """
        # Select teams
        print("-" * 73)
        print("CHOOSE TEAMS")
        print("-" * 73)
        while True:
            for t in range(len(Team.teams)):
                print('[', t, ']: ', Team.teams[t].name, sep='', end='\n')
            print()
            team_1_index = input("Select team 1: ")
            team_2_index = input("Select team 2: ")
            if team_1_index == team_2_index:
                print()
                print("Team 1 has to be different than Team 2")
                print()
                continue
            valid = [str(i) for i in range(len(Team.teams))]
            if team_1_index not in valid or team_2_index not in valid:
                print()
                print("Select a valid team!")
                print()
                continue
            team_1 = Team.teams[int(team_1_index)]
            team_2 = Team.teams[int(team_2_index)]
            call(["clear"])
            break
        
        # Select Team 1 players
        print()
        print("-" * 73)
        print("CHOOSE TEAM 1 PLAYERS (", team_1.name.capitalize(), ")", sep='')
        print("-" * 73)
        while True:
            # Request input
            print()
            players_available_1 = []
            count = 0 
            for player in Player.players:
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
        print()
        print("-" * 73)
        print("CHOOSE TEAM 2 PLAYERS (", team_2.name.capitalize(), ")", sep='')
        print("-" * 73)
        while True:
            # Request input
            print()
            print(team_2.name.capitalize())
            players_available_2 = []
            count = 0 
            for player in Player.players:
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
    def quick_match():
        """Sets up a quick match, where the teams and players are automatically selected"""
        print()
        match = Match(t1, t2, t1_players, t2_players)
        return match


# GAME CLASSES

class Kick:
    """
    Represents an individual kick, with information on each participating 
    player's strategy and the result of the combination of both strategies.
    """
    horizontal_num = {'L': -1, 'C': 0, 'R': +1}

    def __init__(self, match, strategy_shooter, strategy_goalie):
        self.strategies = [strategy_shooter, strategy_goalie]
        self.result = None
        self.match = match
    
    def set_result(self):
        """
        Determines the result of the kick based on the combination of the
        player's strategies
        """
        self.match.kicks_num += 1
        # Shooter is always 0
        if (
            self.strategies[0].horizontal != self.strategies[1].horizontal or
            self.strategies[1].vertical != self.strategies[0].vertical
            ) and (
                self.strategies[0].horizontal in ['L', 'C', 'R']
                or self.strategies[0].vertical <= 3
                ):
            self.result = 'Goal'
        else:
            self.result = 'Miss'
    
    def update_score(self):
        """Updates the match score based on the kicks result (goal or miss)"""
        # Update score
        if self.result == 'Goal':
            self.match.score[self.match.kicking_team - 1] += 1
        # Update kicking team
        if self.match.kicking_team == 1:
            self.match.kicking_team = 2
        else:
            self.match.kicking_team = 1
        # Update winner (if there is)
        if self.match.kicks_num >= 10 and self.match.kicks_num % 2 == 0:
            if self.match.score[0] > self.match.score[1]:
                self.match.winner = self.match.team_1
            if self.match.score[1] > self.match.score[0]:
                self.match.winner = self.match.team_2

    @staticmethod
    def start_kicks(match):
        """
        Starts a kicks session, that is repeated until one of the players wins
        """
        print()
        print("-" * 73)
        print(ball_image)
        print("-" * 73)
        input("Press Enter to start!")
        call(["clear"])
        print()
        # Match goes on until one of the teams win
        while True:
            # Round info
            # if match.kicks_num % 2 == 0:
            print("-" * 73)
            print("Round ", (match.kicks_num // 2) + 1, "!", sep='')
            print("-" * 73)
            print("Turn to kick: ", match.teams[match.kicking_team - 1].name, sep='')
            print("Kicker:", match.shooters[match.kicking_team - 1][0].name)
            print("-" * 73)

            # Shooter strategy
            while True:
                print()
                vertical_s = getpass.getpass("Kicker vertical direction (0 / 1 / 2): ")
                if vertical_s not in [str(i) for i in range(3)]:
                    print("Enter a vertical direction between 0 and 2")
                    continue
                horizontal_s = getpass.getpass("Kicker horizontal direction (L / C / R): ").capitalize()
                if horizontal_s not in ['L', 'C', 'R']:
                    print("Enter a valid horizontal direction (L, C or R)")
                    continue
                player_s = match.shooters[match.kicking_team - 1][0]
                strategy_s = Strategy(player_s, horizontal_s, int(vertical_s))
                break
            # Goalie strategy
            while True:
                print()
                vertical_g = getpass.getpass("Goalie vertical direction (0 / 1 / 2): ")
                if vertical_g not in [str(i) for i in range(3)]:
                    print("Enter a vertical direction between 0 and 2")
                    continue
                horizontal_g = getpass.getpass("Goalie horizontal direction (L / C / R): ").capitalize()
                if horizontal_g not in ['L', 'C', 'R']:
                    print("Enter a valid horizontal direction (L, C or R)")
                    continue
                if match.kicking_team == 1:
                    player_g = match.goalies[1]
                elif match.kicking_team == 2:
                    player_g = match.goalies[0]
                
                strategy_g = Strategy(player_g, horizontal_g, int(vertical_g))
                break
            print("-" * 73)
        
            # Kick
            first_player = match.shooters[match.kicking_team - 1].pop(0)
            match.shooters[match.kicking_team - 1].append(first_player)
            kick = Kick(match, strategy_s, strategy_g)
            kick.set_result()
            kick.update_score()
            print("Kicker:", kick.strategies[0])
            print("Goalie:", kick.strategies[1])
            if kick.result == "Goal":
                print(goal_image)
            else:
                print(miss_image)
            print()
            print("   {0:<15s}: {1:.0f}".format(kick.match.team_1.name, kick.match.score[0]))
            print("   {0:<15s}: {1:.0f}".format(kick.match.team_2.name, kick.match.score[1]))
            print()
            print("-" * 73)
            print()
            if match.kicks_num % 2 != 0:
                input("Press Enter to next kick ")
            else:
                input("Press Enter to next round ")
            print()
            call(["clear"])
            # Match winner
            if kick.match.winner is not None:
                print("-" * 73)
                print("   ", kick.match.team_1.name, ": ", kick.match.score[0])
                print("   ", kick.match.team_2.name, ": ", kick.match.score[1])
                print("-" * 73)
                if kick.match.winner is kick.match.team_1:
                    print(p1wins_image, "\n", kick.match.team_1)
                elif kick.match.winner is kick.match.team_2:
                    print(p2wins_image, "\n", kick.match.team_2)
                print("-" * 73)
                print()
                input("Press Enter to Main menu")
                call(["clear"])
                break
   

class Strategy:
    """
    Represents a player's strategy, i.e. the direction selected in each kick
    """
    def __init__(self, player, horizontal, vertical):
        self.player = player
        self.horizontal = horizontal
        self.vertical = vertical
        self.error = 8 / self.player.ability

    def __repr__(self):
        """Formatted representation of the player's strategy"""
        return "(" + str(self.horizontal) + ", " + str(self.vertical) + ")"


# User interface
def start():
    """
    Controls the flow of the game by displaying the main menu options and
    graphical elements.
    """
    print()
    options_1 = {
        1: '[1] Create team', 2: '[2] List teams', 3: '[3] Create player',
        4: '[4] List players', 5: '[5] Start match', 6: '[6] Quick match',
        7: '[7] Image and text credits', 8: '[8] Quit game'
        }

    while True:
        print("-" * 87)
        print(title_text)
        print(title_image)
        print()
        print("-" * 87)
        print("MAIN MENU")
        print('-' * 87)
        for option in options_1.values():
            print(option, end='\n')
        print()
        print('-' * 87)
        option_entered = input("Choose option: ")
        call(["clear"])
        print()

        try:
            option_1 = int(option_entered)
            # Create team
            if option_1 == 1:
                print("-" * 73)
                print("CREATE TEAM")
                print("-" * 73)
                while True:
                    try:
                        print()
                        team_name = input("     Team name: ")
                        Team(team_name)
                        print()
                        print("Team created!")
                        print()
                        if input("Create another team? (Yes / No) ").lower() == 'no':
                            break
                    except Exception as e:
                        print("\n", e)
                print("-" * 73)
                call(["clear"])
            
            # List teams
            elif option_1 == 2:
                print("-" * 73)
                print("TEAMS")
                print("-" * 73)
                print(team_image)
                Team.list_teams()
                call(["clear"])
            
            # Create player
            elif option_1 == 3:
                while True:
                    try:
                        # Enter player information
                        print("-" * 73)
                        print("CREATE PLAYER")
                        print("-" * 73)
                        print()
                        name = input("Player name: ")
                        ability = int(input("Ability (1 to 10): "))
                        type = int(input("Player type ([1] Shooter / [2] Goalie): "))
                        print("Teams")
                        for t in range(len(Team.teams)):
                            print('   [', t, ']: ', Team.teams[t].name, sep='', end='\n')
                        team_i = int(input("Select team: "))
                        team = Team.teams[team_i]
                        # Create player
                        Player(name=name, ability=ability, type=type, team=team)
                        print()
                        print("Player created!")
                        print()
                        if input("Create another player (Yes / No)? ").lower() == 'no':                            
                            break 
                        call(["clear"])
                    except Exception as e:
                        print()
                        print("Try again:", e)
            
            # List players
            elif option_1 == 4:
                Player.list_players()
                call(["clear"])
            
            # match
            elif option_1 == 5:
                match = Match.match_setup()
                Kick.start_kicks(match)
            
            # Start quick match
            elif option_1 == 6:
                match = Match.quick_match()
                Kick.start_kicks(match)
            
            # Credits
            elif option_1 == 7:
                print("'ASCII' images taken from http://www.chris.com/ascii")
                print("'ASCII' text taken from http://patorjk.com/software/taag/")
                print()
                input("Press Enter to Main menu")
                
            
            # Quit game
            elif option_1 == 8:
                print()
                print("Closing game")
                for i in range(1, 4):
                    time.sleep(0.5)
                    print('.')
                print()
                print("Game closed")
                time.sleep(1)
                call(["clear"])
                exit()
                break
        except ValueError:
            print()
            print('-' * 24)
            print("Select a valid option!")
            print('-' * 24)
        print()


# Quick match setup
t1 = Team('Croatia')
p11 = Player('Danijel Subašić', 5, 2, t1)
p12 = Player('Luka Modrić', 5, 1, t1)
p13 = Player('Ivan Rakitić', 5, 1, t1)
p14 = Player('Mario Mandžukić', 5, 1, t1)
p15 = Player('Marcelo Brozović', 5, 1, t1)
p16 = Player('Ivan Perišić', 5, 1, t1)
p17 = Player('Ante Rebić', 5, 1, t1)
t1_players = [p11, p12, p13, p14, p15]

t2 = Team('France')
p21 = Player('Hugo Lloris', 5, 2, t2)
p22 = Player('Kylian Mabppé', 5, 1, t2)
p23 = Player('Olivier Giroud', 5, 1, t2)
p24 = Player('Paul Pogba', 5, 1, t2)
p25 = Player('Antoine Griezmann', 5, 1, t2)
p26 = Player('N\'Golo Kanté', 5, 1, t2)
p27 = Player('Lucas Hernández', 5, 1, t2)
t2_players = [p21, p22, p23, p24, p25]


# Game images
title_text = """ 
 ____ ____ __ _  __  __  ____ _  _    ____ _  _  __   __ ____     __  _  _ _________
(  _ (  __(  ( \/ _\(  )(_  _( \/ )  / ___/ )( \/  \ /  (_  _)__ /  \/ )( (_  _/ ___)
 ) __/) _)/    /    / (_/\)(  )  /   \___ ) __ (  O (  O ))((___(  O ) \/ ( )( \___ \\
(__) (____\_)__\_/\_\____(__)(__/    (____\_)(_/\__/ \__/(__)    \__/\____/(__)(____/
"""
title_image = """
     -   \O                                     ,  .-.___\     
   -     /\                                   O/  /xx\XXX\     
  -   __/\ `                                  /\  |xx|XXX|       
     `    \, ()                              ` << |xx|XXX|      
 jgs^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

team_image = """
                                                    ,/)
                                                    |_|
        _        _        _        _        _       ].[       ,~,
       |.|      |.|      |.|      |.|      |.|    /~`-'~\     |_|
       ]^[      ]^[      ]^[      ]^[      ]^[   (<|   |>)    ]0[
     /~/^\~\  /~`-'~\  /~`-'~\  /~`-'~\  /~`-'~\  \|___|/   ,-`^'~\\
    {<| $ |>}{<| 8 |>}{<| 9 |>}{<| , |>}{<| 2 |>} {/   \}  {<|   |>}
     \|___|/  \|___|/  \|___|/  \|___|/  \|___|/  /__1__\   \|,__|/
    /\    \    /   \    /   \    /   \    /   \   | / \ |   {/ \  /
    |/>/|__\  /__|__\  /__|__\  /__|__\  /__|__\  |/   \|   /__|\/\\
    |)   \ |  | / \ |  | / \ |  | / \ |  | / \ |  {}   {}   | / \ |
   (_|    \)  (/   \)  (/   \)  (/   \)  (/   \)  |)   (|   (/   \)
   / \    (|  |)   (|  |)   (|  |)   (|  |)   (|  ||   ||  _|)   (|_
.,.\_/,..,|,)(.|,.,|,)(,|,.,|.)(.|,.,|,)(,|,.,|.)(.|.,.|,)(.,|.,.|,.),.,.
"""

player_image = """
           /_`\\
           /-\ )
         __7_/_(_______ _
        /        _____|<_\\
       /        /
      / /|__ __/   
    _/_/ /  X  |      
   <_/  /_     |
       /  \-___|
      ( )'  |  /      ___
       \ |  ( )      /\_/\\
        >\  | /     (-<_>-)
       (_/  |/       \/_\/   
           (_)
"""

ball_image =         """
           _...----.._
        ,:':::::.      `>.
      ,' |:::::;'       |:::.
     /    `'::'         :::::\\
    /           _____     `::;\\
   :           /:::::\      `  :
   | ,.       /::SSt::\        |         MATCH START!
   |;:::.     `::::::;'        |
   ::::::       `::;'      ,.  ;
    \:::'                ,::::/
     \                   \:::/
      `.     ,:.         :;'
        `-.::::::..   _.''
            ```---- '''
        """

goal_image = """
                         _________
                        |   _     |
            \o/         |_o=--    |    GOOOAL!
            ()    o
            |\,
            """

miss_image = """
            _______________
           |':.____________|Z:.
           |  |    \o/     |  |   MISS!
           |  |_____|______|__|
           |,'     / \      |,'
            """

p1wins_image = """                
______ _       _____   _____________   __    _    _ _____ _   _  _____ _ 
| ___ \ |     / _ \ \ / /  ___| ___ \ /  |  | |  | |_   _| \ | |/  ___| |
| |_/ / |    / /_\ \ V /| |__ | |_/ / `| |  | |  | | | | |  \| |\ `--.| |
|  __/| |    |  _  |\ / |  __||    /   | |  | |/\| | | | | . ` | `--. \ |
| |   | |____| | | || | | |___| |\ \  _| |_ \  /\  /_| |_| |\  |/\__/ /_|
\_|   \_____/\_| |_/\_/ \____/\_| \_| \___/  \/  \/ \___/\_| \_/\____/(_)                                                                         
                """

p2wins_image = """
______ _       _____   _____________   _____   _    _ _____ _   _  _____ _ 
| ___ \ |     / _ \ \ / /  ___| ___ \ / __  \ | |  | |_   _| \ | |/  ___| |
| |_/ / |    / /_\ \ V /| |__ | |_/ / `' / /' | |  | | | | |  \| |\ `--.| |
|  __/| |    |  _  |\ / |  __||    /    / /   | |/\| | | | | . ` | `--. \ |
| |   | |____| | | || | | |___| |\ \  ./ /___ \  /\  /_| |_| |\  |/\__/ /_|
\_|   \_____/\_| |_/\_/ \____/\_| \_| \_____/  \/  \/ \___/\_| \_/\____/(_)
                """

# Start game
call(["clear"])
start()