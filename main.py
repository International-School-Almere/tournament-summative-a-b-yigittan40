"""
Basketball Tournament Scoring App
Unit: Programming - Design Document
Learning Aim: A and B
Name: Yigit Tan
"""

import tkinter as tk
from tkinter import messagebox

team_names   = []   
team_players = []  
team_scores  = []   

player_names  = []  
player_scores = [] 

def get_points(rank):
    if rank == 1:
        return 10
    if rank == 2:
        return 7
    if rank == 3:
        return 5
    if rank == 4:
        return 3
    if rank == 5:
        return 1
    return 0

def add_team():
    name = team_name_entry.get()
    name = name.strip()

    if name == "":
        messagebox.showerror("Error", "Team name cannot be empty.")
        return

    if len(team_names) >= 4:
        messagebox.showerror("Error", "Maximum 4 teams already added.")
        return

    if name in team_names:
        messagebox.showerror("Error", "Team name already exists.")
        return

    players_text = players_entry.get()
    players_text = players_text.strip()

    if players_text == "":
        messagebox.showerror("Error", "Players cannot be empty.")
        return

    players = players_text.split(",")

    if len(players) != 5:
        messagebox.showerror("Error", "Please enter exactly 5 players, separated by commas.")
        return

    team_names.append(name)
    team_players.append(players)
    team_scores.append([0, 0, 0, 0, 0])

    status_label.config(text="Team " + name + " added!")
    team_name_entry.delete(0, tk.END)
    players_entry.delete(0, tk.END)

def add_player():
    name = player_name_entry.get()
    name = name.strip()

    if name == "":
        messagebox.showerror("Error", "Player name cannot be empty.")
        return

    if len(player_names) >= 20:
        messagebox.showerror("Error", "Maximum 20 players already added.")
        return

    if name in player_names:
        messagebox.showerror("Error", "Player already exists.")
        return

    player_names.append(name)
    player_scores.append([0, 0, 0, 0, 0])

    status_label.config(text="Player " + name + " added!")
    player_name_entry.delete(0, tk.END)

def save_score():
    game_text  = game_entry.get().strip()
    name       = score_name_entry.get().strip()
    score_text = score_entry.get().strip()

    if game_text == "" or name == "" or score_text == "":
        messagebox.showerror("Error", "Please fill in all three score fields.")
        return

    if not game_text.isdigit():
        messagebox.showerror("Error", "Game number must be a number, not letters.")
        return

    if not score_text.isdigit():
        messagebox.showerror("Error", "Score must be a number, not letters.")
        return

    game_num = int(game_text)
    score    = int(score_text)

    if game_num < 1 or game_num > 5:
        messagebox.showerror("Error", "Game number must be between 1 and 5.")
        return
    
    found = False

    for i in range(len(team_names)):
        if team_names[i] == name:
            team_scores[i][game_num - 1] = score
            found = True

    for i in range(len(player_names)):
        if player_names[i] == name:
            player_scores[i][game_num - 1] = score
            found = True

    if not found:
        messagebox.showerror("Error", name + " was not found. Add them first.")
        return

    status_label.config(text="Score saved! " + name + " scored " + score_text + " in Game " + game_text)
    score_entry.delete(0, tk.END)

def show_leaderboard():
    all_names  = []
    all_totals = []
    all_types  = []

    for i in range(len(team_names)):
        total = 0
        for s in team_scores[i]:
            total = total + s
        all_names.append(team_names[i])
        all_totals.append(total)
        all_types.append("Team")

    for i in range(len(player_names)):
        total = 0
        for s in player_scores[i]:
            total = total + s
        all_names.append(player_names[i])
        all_totals.append(total)
        all_types.append("Player")
 
    if len(all_names) == 0:
        messagebox.showinfo("Leaderboard", "No teams or players added yet.")
        return
    
    for i in range(len(all_totals)):
        for j in range(i + 1, len(all_totals)):
            if all_totals[j] > all_totals[i]:
                temp = all_totals[i]
                all_totals[i] = all_totals[j]
                all_totals[j] = temp
                temp = all_names[i]
                all_names[i] = all_names[j]
                all_names[j] = temp
                temp = all_types[i]
                all_types[i] = all_types[j]
                all_types[j] = temp
 
    message = "BASKETBALL TOURNAMENT LEADERBOARD\n\n"
 
    for i in range(len(all_names)):
        rank = i + 1
        if rank == 1:
            place = "1st"
        elif rank == 2:
            place = "2nd"
        elif rank == 3:
            place = "3rd"
        else:
            place = str(rank) + "th"
 
        message = message + place + "  " + all_names[i] + " (" + all_types[i] + ")  -  " + str(all_totals[i]) + " pts\n"
 
    messagebox.showinfo("Leaderboard", message)
    import tkinter as tk

window = tk.Tk()
window.title("Basketball Tournament Scorer")
 
tk.Label(window, text="Team name").grid(row=0, column=0, sticky="e", padx=6, pady=4)
tk.Label(window, text="Players (comma separated)").grid(row=1, column=0, sticky="e", padx=6, pady=4)
 
team_name_entry = tk.Entry(window, width=30)
team_name_entry.grid(row=0, column=1, pady=4)
 
players_entry = tk.Entry(window, width=30)
players_entry.grid(row=1, column=1, pady=4)
players_entry.insert(0, "Alice, Bob, Carl, Dana, Eve")
 
tk.Button(window, text="Add Team", command=add_team).grid(row=0, column=2, padx=6)
 
tk.Label(window, text="Player name").grid(row=2, column=0, sticky="e", padx=6, pady=4)
 
player_name_entry = tk.Entry(window, width=30)
player_name_entry.grid(row=2, column=1, pady=4)
 
tk.Button(window, text="Add Player", command=add_player).grid(row=2, column=2, padx=6)
 
tk.Label(window, text="─" * 44).grid(row=3, column=0, columnspan=3, pady=2)
 
tk.Label(window, text="Game number (1-5)").grid(row=4, column=0, sticky="e", padx=6, pady=4)
tk.Label(window, text="Team or Player name").grid(row=5, column=0, sticky="e", padx=6, pady=4)
tk.Label(window, text="Points scored").grid(row=6, column=0, sticky="e", padx=6, pady=4)
 
game_entry = tk.Entry(window, width=30)
game_entry.grid(row=4, column=1, pady=4)
 
score_name_entry = tk.Entry(window, width=30)
score_name_entry.grid(row=5, column=1, pady=4)
 
score_entry = tk.Entry(window, width=30)
score_entry.grid(row=6, column=1, pady=4)
 
tk.Button(window, text="Save Score", command=save_score).grid(row=6, column=2, padx=6)
 
tk.Label(window, text="─" * 44).grid(row=7, column=0, columnspan=3, pady=2)
 
tk.Button(window, text="Show Leaderboard", command=show_leaderboard).grid(row=8, column=1, pady=6)
 
status_label = tk.Label(window, text="", fg="green")
status_label.grid(row=9, column=0, columnspan=3, pady=4)
 
window.mainloop()