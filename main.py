#main file for the Tournament App.
"""
Basketball Tournament Scoring App
Unit: Programming - Design Document
Learning Aim: A and B
Name: Yigit Tan
"""

# Points awarded based on rank in each game
POINTS_SYSTEM = {1: 10, 2: 7, 3: 5, 4: 3, 5: 1}
MAX_GAMES = 5       # up to 5 games in the tournament
MAX_TEAMS = 4       # 4 basketball teams
TEAM_SIZE = 5       # 5 players per team
MAX_INDIVIDUALS = 20  # up to 20 individual players (e.g. free throw contest)

def main():
    print("Welcome to the Basketball Tournament Scoring App!")
    print("This app will help you manage and score a basketball tournament.")
    print("You can enter team names, player names, and game results to calculate scores.")
    print("Let's get started!")