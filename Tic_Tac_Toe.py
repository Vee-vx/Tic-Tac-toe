# Import the necessary modules and functions
import os

from helper import draw_board, check_turn, check_wins, view_game_stats, save_session_stats, save_game_history, update_html, get_current_session, update_current_session, update_game_stats

# Initialize the game board and player stats
place = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
         6: '6', 7: '7', 8: '8', 9: '9'}  
player1_wins = 0  # Player 1's win count
player2_wins = 0  # Player 2's win count
draws = 0  # draw count
session_number = get_current_session()  # track of game sessions!

while True:
    playing = True  # playing
    complete = False  # won or draw
    turn = 0  # Keep track of whose turn it is
    prev_turn = -1  # Remember the previous turn to avoid invalid moves
    history = []  # keep a record of game history
#main menu
    print("MAIN  MENU")
    print("1. Play Game")  
    print("2. View Game History") 
    print("3. Exit")  
    choice = input("Enter your choice: ")

    if choice == "1":
        while playing:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen for a fresh start
            draw_board(place)  # Shows us the board!
            if prev_turn == turn:
                print('Invalid position selected, please select another')  # invalid move
            prev_turn = turn
            print("Player " + str((turn % 2) + 1) + "'s turn: Pick your position or press q to quit")  # check whose turn is it?

            choice = input().upper()  # Get the player's move
            if choice == 'Q':
                playing = False
                 # Reset the game board for the next game
                place = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


            elif str.isdigit(choice) and int(choice) in place:
                if not place[int(choice)] in {"X", "O"}:
                    turn += 1
                    place[int(choice)] = check_turn(turn)  # Update the board with the new move

            if check_wins(place):
                playing, complete = False, True  # Got a winner
            if turn > 8:
                playing = False  # It's a draw!

        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen for the final result
        draw_board(place)  # Show us the final board
# winner decider
        if complete:
            if check_turn(turn) == 'X':
                print("Player 1/X wins!")
                history.append('Player 1/X wins!')
                player1_wins +=1
            else:
                print("Player 2/O wins!")  
                history.append('Player 2/O wins!')
                player2_wins +=1
            # Reset the game board for the next game
            place = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

        else:
            print("Game is Tied!")  # It's a draw!
            history.append('The game was draw')
            draws +=1
            # Reset the game board for the next game
            place = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

        save_game_history(history, session_number)  # Save game history

        update_html(session_number, player1_wins, player2_wins, draws)
  # Update  HTML file with the latest stats

        player1_wins, player2_wins, draws = update_game_stats(player1_wins, player2_wins, draws)  # Update  game stats
        save_session_stats(player1_wins, player2_wins, draws, session_number)  # Save  game stats
        print("Thanks for playing!")  
        session_number += 1  # Increment session number
         # Update current session number
    elif choice == "2":
        view_game_stats(f'session_{session_number - 1}_stats.txt')  # View game history
    elif choice == "3":
        update_current_session(session_number + 1)
        print("Thanks for playing!")  # Thanks for playing, goodbye!
        break
    else:
        print("Invalid choice, try again.")  # Oops
