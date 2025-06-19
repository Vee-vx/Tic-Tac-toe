import os

# Function to draw the Tic-Tac-Toe board
def draw_board(place):
    # Create a string representation of the board
    board = (f"|{place[1]}|{place[2]}|{place[3]}|\n"
             f"|{place[4]}|{place[5]}|{place[6]}|\n"
             f"|{place[7]}|{place[8]}|{place[9]}|")
    # Print the board
    print(board)

# Function to determine whose turn it is
def check_turn(turn):
    # If the turn number is even, it's O's turn
    if turn % 2 == 0:
        return 'O'
    # Otherwise, it's X's turn
    else:
        return 'X'

# Function to check if there's a winner
def check_wins(place):
    # Check rows for a win
    if (place[1] == place[2] == place[3]) or (place[4] == place[5] == place[6]) or (place[7] == place[8] == place[9]):
        return True
    # Check columns for a win
    elif (place[1] == place[4] == place[7]) or (place[2] == place[5] == place[8]) or (place[3] == place[6] == place[9]):
        return True
    # Check diagonals for a win
    elif (place[1] == place[5] == place[9]) or (place[3] == place[5] == place[7]):
        return True
    # If no win, return False
    else:
        return False

# Function to view game stats
def view_game_stats(file_name):
    # Open the file and print its contents
    with open(file_name, 'r') as file:
        print(file.read())

# Function to save session stats
def save_session_stats(player1_wins, player2_wins, draws, session_number):
    # Open a file with the session number and write the stats
    with open(f'session_{session_number}_stats.txt', 'w') as file:
        file.write(f"Session {session_number} stats:\n")
        file.write(f"Player 1/X wins: {player1_wins}\n")
        file.write(f"Player 2/O wins: {player2_wins}\n")
        file.write(f"Draws: {draws}\n")

# Function to save game history
def save_game_history(history, session_number):
    # Open a file with the session number and write the history
    with open(f'session_{session_number}_history.txt', 'w') as file:
        for item in history:
            file.write(item + "\n")

# Function to update the HTML file with session stats
def update_html(session_number, player1_wins, player2_wins, draws):
    # Open the HTML file and write the stats
    with open('index.html', 'w') as file:
        file.write("<html><body>")
        file.write(f"<h1>Session {session_number} stats:</h1>")
        file.write(f"<p>Player 1/X wins: {player1_wins}</p>")
        file.write(f"<p>Player 2/O wins: {player2_wins}</p>")
        file.write(f"<p>Draws: {draws}</p>")
        file.write("</body></html>")

# Function to get the current session number
def get_current_session():
    # Check if the current session file exists
    session_file = "current_session.txt"
    session_number = 1
    if os.path.exists(session_file):
        # If it exists, read the session number from the file
        with open(session_file, 'r') as file:
            session_number = int(file.read())
    return session_number

# Function to update the current session number
def update_current_session(session_number):
    # Write the new session number to the file
    with open("current_session.txt", 'w') as file:
        file.write(str(session_number))

# Function to update game stats (not actually doing anything)
def update_game_stats(player1_wins, player2_wins, draws):
    return player1_wins, player2_wins, draws
