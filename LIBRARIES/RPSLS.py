import random
import PySimpleGUI as sg

# List of options for computer to randomly select from
options = ["rock", "paper", "scissors", "lizard", "spock"]

# Global Variables
userwins = 0
computerwins = 0
winsneeded = 0
computerchoice = ""
playerchoice = ""

# Calculate result based on user input and randomised computer input
def GameLogic():
    global userwins, computerwins, computerchoice, playerchoice
    
    computerchoice = random.choice(options)
    print(f"Player: {playerchoice}, Computer: {computerchoice}")
    
    if playerchoice == "rock":
        if computerchoice == "scissors" or computerchoice == "lizard":
            userwins += 1
        elif computerchoice == "paper" or computerchoice == "spock":
            computerwins += 1
        else:
            DrawBox()
            
    elif playerchoice == "paper":
        if computerchoice == "rock" or computerchoice == "spock":
            userwins += 1
        elif computerchoice == "scissors" or computerchoice == "lizard":
            computerwins += 1
        else:
            DrawBox()
    
    elif playerchoice == "scissors":
        if computerchoice == "paper" or computerchoice == "lizard":
            userwins += 1
        elif computerchoice == "rock" or computerchoice == "spock":
            computerwins += 1
        else:
            DrawBox()
    
    elif playerchoice == "lizard":
        if computerchoice == "spock" or computerchoice == "paper":
            userwins += 1
        elif computerchoice == "rock" or computerchoice == "scissors":
            computerwins += 1
        else:
            DrawBox()
    
    elif playerchoice == "spock":
        if computerchoice == "scissors" or computerchoice == "rock":
            userwins += 1
        elif computerchoice == "paper" or computerchoice == "lizard":
            computerwins += 1
        else:
            DrawBox()
    print(f"Player wins: {userwins}, Computer wins: {computerwins}")

# Set up for the win window
def WinBox():
    layout = [[sg.Text("You win! Congratulations!")]]
    window = sg.Window("Winner!", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
    window.close()

# Set up for the lose window
def LoseBox():
    layout = [[sg.Text("You Lost! Try again!")]]
    window = sg.Window("Loser!", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
    window.close()

# Set up for the draw window
def DrawBox():
    layout = [[sg.Text("It was a draw! Try again!")]]
    window = sg.Window("Draw!", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
    window.close()

# Main Function to play the game by selecting options
def PlayGame():
    global userwins, computerwins, winsneeded, playerchoice
    layout = [
        [sg.Text("Please pick an option to play against the computer!")],
        [sg.Button("Rock", expand_x=True)],
        [sg.Button("Paper", expand_x=True)],
        [sg.Button("Scissors", expand_x=True)],
        [sg.Button("Lizard", expand_x=True)],
        [sg.Button("Spock", expand_x=True)]
    ]
    window = sg.Window("Rock, Paper, Scissors, Lizard, Spock", layout)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        
        # Player Choice Logic
        if event == "Rock":
            playerchoice = "rock"
        elif event == "Paper":
            playerchoice = "paper"
        elif event == "Scissors":
            playerchoice = "scissors"
        elif event == "Lizard":
            playerchoice = "lizard"
        elif event == "Spock":
            playerchoice = "spock"
        
        # Run Game Logic
        GameLogic()
        
        # Check Win/Loss Conditions
        if userwins == winsneeded:
            WinBox()
            break
        elif computerwins == winsneeded:
            LoseBox()
            break

    window.close()

# Best Of Game Setup
def BestOf():
    global userwins, computerwins, winsneeded
    layout = [
        [sg.Text("Welcome to Rock, Paper, Scissors, Lizard, Spock!")],
        [sg.Text("Please select the number of games")],
        [sg.Button("Best of 1", expand_x=True)],
        [sg.Button("Best of 3", expand_x=True)],
        [sg.Button("Best of 5", expand_x=True)]
    ]
    
    window = sg.Window("Rock, Paper, Scissors, Lizard, Spock", layout)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        
        if event == "Best of 1":
            winsneeded = 1
        elif event == "Best of 3":
            winsneeded = 2
        elif event == "Best of 5":
            winsneeded = 3
        
        # Reset scores and start the game
        userwins = 0
        computerwins = 0
        PlayGame()
        break

    window.close()

# Run the Best of Selection screen
BestOf()

#
#
# Test commit
#
#