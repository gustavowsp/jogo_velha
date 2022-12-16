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
        def get_house():
            def house():
                house = input("\nWhat's house you will play?")

                if self.is_number(house):
                    house = int(house)
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
        
    def print_player(self):
        print(f'A bolinha é {self.boll} \no X é {self.ex}')
        
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

    
    
