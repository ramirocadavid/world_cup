# Kick dynamics classes 

from images import *
from subprocess import call
import getpass

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
        # Update winner (if there is one)
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
            print("Round ", (match.kicks_num // 2) + 1, "!", sep='')
            print()
            print("Turn to kick: ", match.teams[match.kicking_team - 1].name, sep='')
            print("Kicker:", match.shooters[match.kicking_team - 1][0].name)
            print()

            # Shooter strategy
            while True:
                print()
                vertical_s = getpass.getpass("Kick height (0 1 2): ")
                if vertical_s not in [str(i) for i in range(3)]:
                    print("Enter a height between 0 and 2")
                    continue
                horizontal_s = getpass.getpass("Kick direction (L C R): ").capitalize()
                if horizontal_s not in ['L', 'C', 'R']:
                    print("Enter a valid direction (L, C or R)")
                    continue
                player_s = match.shooters[match.kicking_team - 1][0]
                strategy_s = Strategy(player_s, horizontal_s, int(vertical_s))
                break
            # Goalie strategy
            while True:
                print()
                vertical_g = getpass.getpass("Goalie height (0 1 2): ")
                if vertical_g not in [str(i) for i in range(3)]:
                    print("Enter a height between 0 and 2")
                    continue
                horizontal_g = getpass.getpass("Goalie direction (L C R): ").capitalize()
                if horizontal_g not in ['L', 'C', 'R']:
                    print("Enter a valid direction (L, C or R)")
                    continue
                if match.kicking_team == 1:
                    player_g = match.goalies[1]
                elif match.kicking_team == 2:
                    player_g = match.goalies[0]
                
                strategy_g = Strategy(player_g, horizontal_g, int(vertical_g))
                call(["clear"])
                break
        
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
            print("{0:s}: \t{1:.0f}".format(kick.match.team_1.name, kick.match.score[0]))
            print("{0:s}: \t{1:.0f}".format(kick.match.team_2.name, kick.match.score[1]))
            print()
            # print("-" * 73)
            if match.kicks_num % 2 != 0:
                input("Press Enter for next kick!")
            else:
                input("Press Enter for next round!")
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
                input("Press Enter for Main menu")
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