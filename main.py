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

teams = []        
individuals = [] 

def get_valid_int(prompt, min_val=None, max_val=None):
    """Keep asking until a valid integer is entered."""
    while True:
        raw = input(prompt).strip()
        if not raw.lstrip("-").isdigit():
            print("  Error: enter a whole number, not letters.")
            continue
        value = int(raw)
        if min_val is not None and value < min_val:
            print(f"  Error: must be at least {min_val}.")
            continue
        if max_val is not None and value > max_val:
            print(f"  Error: must be at most {max_val}.")
            continue
        return value

def print_separator(char="─", width=52):
    print(char * width)


def total_points(obj):
    return sum(obj["points"])

def add_team():
    if len(teams) >= MAX_TEAMS:
        print(f"  Max {MAX_TEAMS} teams already added.")
        return

    print("\n── Add a Basketball Team ──")
    name = input("  Team name: ").strip()
    if not name:
        print("  Error: name cannot be empty.")
        return
    if any(t["name"].lower() == name.lower() for t in teams):
        print("  Error: team name already exists.")
        return
