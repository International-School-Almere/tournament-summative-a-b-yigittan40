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