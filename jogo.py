from collections import deque # LinkedList
import array as arr # Arrays
import random
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Players():
    
    def __init__(self, name) -> None:
        self.name = name
        self.points = 0
        self.victory = 0
        self.caracter = None

    def __repr__(self) -> str:
        return self.name or 'Player Off'

    def __str__(self) -> str:
        return 'Class of players at Jogo Da Velha'

    @staticmethod
    def is_number(number):
        try:
            x = int(number)
            return True
        except:
            return False

    def jogar(self):
        def welcome():
            print('=='*20)
            print(f"Now it's the round of {player.name}")
            print('=='*20)
        def get_house():

            def house():         
                welcome()
                house = input("\nWhat's house you will play?")

                if self.is_number(house):
                    house = int(house)
                elif house == 'x':
                    return False

                if house >= 1 and house <= 9:
                    return house
                    
                print('Choice an house in range of 1-9')
                return None
        
            # Create a var for house
            number = None

            # Getting the house
            while number == None:
                number = house()
            
            # Return the house 
            return number
        def house_to_array(number):
            
            house_bi = number

            if house_bi <= 3:
                house_bi = [0,number-1]

            elif house_bi <= 6:
                house_bi = [1,number-4]

            elif house_bi <= 9:
                house_bi = [2,number-7]

            return house_bi

        # Get...
        number = get_house()
        if number == False:
            return number

        # Create the house addres
        casa = arr.array('I',[])

        # Append the house
        casa.extend(house_to_array(number))

        return casa
class Board(bcolors):

    def __init__(self) -> None:
        # Lines
        l1= [1,2,3]
        l2= [4,5,6]
        l3= [7,8,9]

        # Collums
        self.board = [l1,l2,l3]

    def __str__(self) -> str:
        return 'Board'

    def play(self, local,caracter):

        # Get the line and collumns
        line = local[0]
        collum = local[1]
        
        # Check if the house is full
        players = ('X','O')
        if self.board[line][collum] in players:
            print('\nEsta casa está preenchida, por favor escolha outra.')
            return True

        # Play
        self.board[line][collum] = caracter
        
    def print_board(self,playedhouse=None):

        boar_temp = arr.array('i',[0,0])

        # Pass the line items to the statment FOR below
        for line in self.board:
            time.sleep(0.3)

            # Get the itens in each collum and print.
            for item_collum in line:
                
                # Print the played house colored
                if boar_temp == playedhouse:
                    print(f'{self.BOLD}{self.OKCYAN}{item_collum}',end=' ')
                           
                # Print full houses with color
                elif item_collum in ('X','O'):
                     print(f'{self.FAIL}{item_collum}',end=' ')
                
                # Print free houses.
                else:
                    print(f"{self.OKGREEN}{item_collum}",end=' ')

                print(self.ENDC,end='')
                boar_temp[1] +=  1
                
                
            

            boar_temp[1] = 0
            boar_temp[0] += 1

            # Space
            print('')

    def check_winner(self,play_position,caract):
        def last_house(firts_house,second_house):
            
            # Pegando a linha e a coluna da PRIMEIRA CASA
            first_house_line = firts_house[0]
            first_house_collum = firts_house[1]

            # Pegando a linha e a coluna da SEGUNDA CASA
            second_house_line = second_house[0]
            second_house_collum = second_house[1]

            # Pegando a diferença entre a PRIMEIRA CASA e a SEGUNDA       
            diferenca = (first_house_line - second_house_line, first_house_collum - second_house_collum)

            # Descobrindo qual é a próxima casa
            """Aqui estou somando a diferença entre a primeira e a segunda casa
            com a segunda casa
            Assim descubro para onde ir

            Imagine: 
            1 casa = (2,2)
            2 casa = (1,2)
            Diferença entre a 1 casa e a 2 casa = (1,0)

            a soma:
            Linha -- 1 + 1
            Coluna -- 0 + 2
            Resultado: (-1,2) 
            """
            last_house = (diferenca[0] + second_house_line, diferenca[1] + second_house_collum)

            # Passando para um array, para poder modificar
            last_house =  arr.array('b',[last_house[0],last_house[1]])
            
            # Caso a última casa for igual a primeira vou repetir o passo anterior, mas subtraindo
            if last_house[0] == first_house_line and last_house[1] == first_house_collum:
                last_house[0] = second_house_line - diferenca[0]
                last_house[1] = second_house_collum - diferenca[1]
            
                # Deixando positivo
                if last_house[0] != -1 and last_house[0] < 0 :
                    last_house[0] = last_house[0] * -1

                if last_house[1] != -1 and last_house[1] < 0:
                    last_house[1] = last_house[1] * -1
                
                
            if last_house[0] == -1:
                last_house[0] = 2

            elif last_house[0] == 3:
                last_house[0] = 0

            if last_house[1] == -1:
                last_house[1] = 2
                
            elif last_house[1] == 3:
                last_house[1] = 0
            
            if self.board[last_house[0]][last_house[1]] == caract:
                return True

        def exists_one_house(checks):
            for check in checks:

                if self.board[check[0]][check[1]] == caract:

                    winer = last_house(play_position,check)
                    if winer == True:
                        return True
                            
        winner = False
        # Discover the position
        canto = (
            (0,0),  (0,2),
            (2,0),  (2,2)
        )
        canto_borda =(
                (0,1),
            (1,0),  (1,2),
                (2,1)
            )
        centro =  (
            (1,1),
            )

        line = play_position[0]
        collum = play_position[1]

        for local in canto:
            if local[0] == line and local[1] == collum:

                # Esquerda superior
                if (line,collum) == (0,0):
                    checks = (
                            (0,1),
                        (1,0),(1,1)
                        )
                    winner = exists_one_house(checks)
                    

                # Direita superior
                elif  (line,collum) == (0,2):
                        checks = (
                            (0,1),
                            (1,1), (1,2)
                        )
                        winner = exists_one_house(checks)

                # Esquerda inferior 
                elif  (line,collum) == (2,0):
                        checks = (

                            (1,0),(1,1)
                                ,(2,1)
                        )
                        winner =  exists_one_house(checks)

                # Direita inferior
                elif  (line,collum) == (2,2):
                        checks = ( 
                            (1,1), (1,2),
                            (2,1),
                        )
                        winner =exists_one_house(checks)

        for local in canto_borda:
            if local[0] == line and local[1] == collum:
                    # Centro Cima
                    if (line,collum) == (0,1):
                        checks = (
                            (0,0),  (0,2),
                                (1,1)
                        )
                        winner = exists_one_house(checks)
                    
                    # Centro Esqueda
                    elif (line,collum) == (1,0):
                        checks = (
                            (0,0),
                                (1,1),
                            (2,0)
                        )
                        winner = exists_one_house(checks)

                    # Centro Direita
                    elif (line,collum) == (1,2):
                        checks = (
                                (0,2),
                            (1,1),
                                (2,2)
                        )
                        winner = exists_one_house(checks)

                    # Centro baixo
                    elif (line,collum) == (2,1):
                        checks = (
                                (1,1),
                            (2,0),   (2,2)
                        )
                        winner = exists_one_house(checks)
                    
        for local in centro:
            if local[0] == line and local[1] == collum:
                checks = (
                (0,0),(0,1),(0,2),
                (1,0),      (1,2),
                (2,0),(2,1),(2,2)
                        )
            
                winner = exists_one_house(checks)
        
        return winner

def random_players(p1,p2):

    number = random.randint(0,1)
    
    if number == 0:
        players = (p1, p2)
    else:
        players = (p2, p1)

    players[0].caracter = 'O'
    players[1].caracter = 'X'

    return players

def get_players_name():
        p1 = input("Hello new player what's your name? ")
        p2 = input("Hello new player what's your name? ")
        print('\n\n\n')
        return p1,p2

def welcome_game(text1):
    def tracos():
        time.sleep(0.4)
        print('--'*20)
        time.sleep(0.4)
    
    tracos()

    print(text1)
    time.sleep(0.8)
    print('Lets start...') 

    tracos()
    print('\n')      

def space():
    print('\n\n')

def won(player):

                    print(f'\nThe player {player.name} WON the round.')
                    time.sleep(0.5)
                    print(f'The player {player.name} WON the round.')
                    time.sleep(0.3)
                    print(f'The player {player.name} WON the round.\nCongratulions')
                    time.sleep(0.2)
                    player.victory += 1 
                    print(f'\nThe {player.name} have {player.victory} win NOW.')

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
    welcome_game("Are you ready???")
    on = True
    while on:

        for i in range(0,2):

            # Get the player
            player = x_or_o[i]

            # Get the house
            house_played = player.jogar()
            if house_played == False:
                on = False
                break

            # Play
            full = board.play(house_played,player.caracter)
            
            # If the house is full, restart.
            if full == True:
                continue
            
            ###TRABALHANDO
            #--------------------------------------------------------------------------------------
            # Print the board
            board.print_board(playedhouse=house_played)

            winner = board.check_winner(house_played,player.caracter)

            if winner == True:
                won(player)
                on = False
                break 
            space()

    print('\nObrigado por jogar comigo!!\n\n')
    
    

