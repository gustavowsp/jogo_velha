if __name__ == '__main__':

    welcome_game('Welcome to the **JOGO DA VELHA**')

    # Get the players name
    players = get_players_name()

    # Create the players
    p1 = Players(players[0])
    p2 = Players(players[1])

    # Sort players
    x_or_o = random_players(p1,p2)

    player_o = x_or_o[0]
    player_x = x_or_o[1]

    # Create the board
    board = Board()

    # Start of play
    welcome_game("Yourue:'re READY??????")
    while True:

        for i in range(0,2):

            # Get the player
            player = x_or_o[i]

            print('=='*20)
            print(f"Now it's the round of {player.name}")
            print('=='*20)

            # Get the house
            house_played = player.jogar()

            # Play
            full = board.play(house_played,player.caracter)
            
            # If the house is full, restart.
            if full == True:
                continue
            
            # Print the board
            board.print_board(playedhouse=house_played)
            space()

    
   