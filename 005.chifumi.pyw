from tkinter import Tk, Label, Button 
import random

root = Tk()
root.title("Shi-Fu-Mi")
root.iconbitmap("data/icons/shifumi.ico")

player_wins = {'rs', 'pr', 'sp'}
player_draws = {'rr', 'pp', 'ss'}
global plrscr, cpuscr
plrscr = 0
cpuscr = 0

def choose(choice):
	global plrscr
	global cpuscr
	computer = random.choice(['r', 'p', 's'])
	combo = choice + computer
	
	if combo in player_wins:
		text = 'You won!'
		plrscr += 1
	elif combo in player_draws:
		text = 'Draw!'
	else:
		text = 'Cpu won!'
		cpuscr += 1
	
	game_score.config(text="You: " + str(plrscr) + "    Cpu: " + str(cpuscr))
	game_state.config(text=text)

def gameReset():
	global plrscr
	global cpuscr
	plrscr = 0
	cpuscr = 0
	game_score.config(text="You: " + str(plrscr) + "    Cpu: " + str(cpuscr))
	game_state.config(text=" ")

# Main Label
title = Label(root, text="Rock, Paper or Scissors?", padx=0, pady=10, bg="#333333", fg="#ffffff")
title.grid(row=0, column=1)

# Buttons
rock_btn = Button(root, text="Rock!", padx=20, pady=10, bg="#333333", fg="#ffffff", command=lambda: choose('r'))
paper_btn = Button(root, text="Paper!", padx=18, pady=10, bg="#333333", fg="#ffffff", command=lambda: choose('p'))
scissors_btn = Button(root, text="Scissors!", padx=10, pady=10, bg="#333333", fg="#ffffff", command=lambda: choose('s'))
game_reset = Button(root, text="Reset", padx=5, pady=2, bg="#ff0000", fg="#ffffff", command=gameReset)

scissors_btn.grid(row=1, column=2)
paper_btn.grid(row=1, column=1)
rock_btn.grid(row=1, column=0)
game_reset.grid(row=2, column=2, padx=20, pady=10)

game_score = Label(root, text="You: 0    Cpu: 0", padx=8, pady=5, bg="#333333", fg="#ffffff")
game_score.grid(row=3, column=0, columnspan=3)
game_state = Label(root, padx=20, pady=10, bg="#333333", fg="#ffffff")
game_state.grid(row=2, column=1)

root.configure(bg="#333333")
root.geometry("286x170")
root.resizable(False,False)
root.mainloop()