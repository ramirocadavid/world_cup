#! /usr/bin/python

import time
from subprocess import call
from images import *
from team_setup import *
from match_setup import *
from kick_dynamics import *

def main():
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
    
    # Create default teams

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
    p22 = Player('Kylian Mbappé', 5, 1, t2)
    p23 = Player('Olivier Giroud', 5, 1, t2)
    p24 = Player('Paul Pogba', 5, 1, t2)
    p25 = Player('Antoine Griezmann', 5, 1, t2)
    p26 = Player('N\'Golo Kanté', 5, 1, t2)
    p27 = Player('Lucas Hernández', 5, 1, t2)
    t2_players = [p21, p22, p23, p24, p25]

    teams = [t1, t2]
    players = t1_players + t2_players

    while True:
        call(["clear"])
        print(title_text, "\n\n")
        print(title_image)
        for option in options_1.values():
            print(option, end='\n')
        print()
        option_entered = input("Enter option: ")
        print()

        try:
            option_1 = int(option_entered)
            # Create team
            if option_1 == 1:
                while True:
                    try:
                        call(["clear"])
                        print("CREATE TEAM")
                        print(team_image)
                        team_name = input("Enter team name: ")
                        Team(team_name)
                        print()
                        print("Team created!")
                        print()
                        if input("Create another team? (Yes / No) ").lower() == 'no':
                            break
                        call(["clear"])
                    except Exception as e:
                        print("\n", e)
            
            # List teams
            elif option_1 == 2:
                call(["clear"])
                Team.list_teams()
            
            # Create player
            elif option_1 == 3:
                call(["clear"])
                while True:
                    try:
                        # Enter player information
                        print(player_image)
                        print("CREATE PLAYER!")
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
                call(["clear"])
                Player.list_players()
            
            # match
            elif option_1 == 5:
                call(["clear"])
                teams = Team.teams
                players = Player.players
                match = Match.match_setup(teams, players)
                Kick.start_kicks(match)
            
            # Start quick match
            elif option_1 == 6:
                call(["clear"])
                t1 = Team.teams[0]
                t1_players = [p for p in Player.players if p.team == t1]
                t2 = Team.teams[1]
                t2_players = [p for p in Player.players if p.team == t2]
                match = Match.quick_match(t1, t1_players, t2, t2_players)
                Kick.start_kicks(match)
            
            # Credits
            elif option_1 == 7:
                call(["clear"])
                print("'ASCII' images taken from http://www.chris.com/ascii")
                print("'ASCII' text taken from http://patorjk.com/software/taag/")
                print()
                input("Press Enter to Main menu")
                
            
            # Quit game
            elif option_1 == 8:
                call(["clear"])
                print()
                print("Finishing game")
                for i in range(1, 4):
                    time.sleep(0.5)
                    print('.')
                print()
                print("Game finished")
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

if __name__ == "__main__":
    call(["clear"])
    main()