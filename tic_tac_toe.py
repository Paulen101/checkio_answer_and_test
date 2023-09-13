import tkinter as tk
from tkinter import messagebox

# Initialize the board
board = [" " for _ in range(9)]

# Function to check if someone has won
def check_win(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i*3 + j] == player for j in range(3)]):  # Rows
            return True
        if all([board[i + j*3] == player for j in range(3)]):  # Columns
            return True
    if all([board[i] == player for i in [0, 4, 8]]) or all([board[i] == player for i in [2, 4, 6]]):  # Diagonals
        return True
    return False

# Function to handle a button click
def on_click(button, position):
    if board[position] == " " and not game_over:
        button.config(text=current_player)
        board[position] = current_player
        if check_win(current_player):
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_game()
        elif " " not in board:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_game()
        else:
            switch_player()

# Function to switch players
def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, current_player, game_over
    board = [" " for _ in range(9)]
    current_player = "X"
    game_over = False
    for button in buttons:
        button.config(text=" ", state="active")

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons for the game
buttons = []
for i in range(9):
    row, col = i // 3, i % 3
    button = tk.Button(root, text=" ", width=10, height=4, command=lambda i=i: on_click(buttons[i], i))
    button.grid(row=row, column=col)
    buttons.append(button)

# Initialize game variables
current_player = "X"
game_over = False

# Create a menu bar
menu = tk.Menu(root)
root.config(menu=menu)
game_menu = tk.Menu(menu)
menu.add_cascade(label="Game", menu=game_menu)
game_menu.add_command(label="New Game", command=reset_game)
game_menu.add_separator()
game_menu.add_command(label="Exit", command=root.quit)

# Start the game
root.mainloop()
