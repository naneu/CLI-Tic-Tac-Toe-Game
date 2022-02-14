
board ={1:' ', 2:' ', 3:' ', 
        4:' ', 5:' ', 6:' ',
        7:' ', 8:' ', 9:' '}

class Game:
    def __init__(self):
        self.count = 0
        self.player_turn = 0
        self.turn = None
        self.draws = 0
        self.x_wins = 0
        self.o_wins = 0

    def print_board(self,board):
        print('\n')
        print('\t    |     |   ')
        print(f"\t {board[1]}  |  {board[2]}  | {board[3]}")
        print('\t----|-----|----')

        print('\t    |     |   ')
        print(f"\t {board[4]}  |  {board[5]}  | {board[6]}")
        print('\t----|-----|----')

        print('\t    |     |   ')
        print(f"\t {board[7]}  |  {board[8]}  | {board[9]}")

    def check_state(self,board):
        #check whether a player has won or its a draw
        if self.count >= 5:
            if board[1] == board[2] == board[3] != ' ':
                print(f' {self.turn} won!!')
                self.print_board(board)
                self.add_results(self.player_turn)
                self.scoreboard()
                return True
            
            elif board[4] == board[5] == board[6] != ' ':
                print(f' {self.turn} won!!')
                self.print_board(board)
                self.add_results(self.player_turn)
                self.scoreboard()
                return True

            elif board[7] == board[8] == board[9] != ' ':
                print(f' {self.turn} won!!')
                self.print_board(board)
                self.add_results(self.player_turn)
                self.scoreboard()
                return True

            elif board[1] == board[4] == board[7] != ' ':
                print(f' {self.turn} won!!')
                self.print_board(board)
                self.add_results(self.player_turn)
                self.scoreboard()
                return True

            elif board[2] == board[5] == board[8] != ' ':
                print(f' {self.turn} won!!')
                self.print_board(board)
                self.add_results(self.player_turn)
                self.scoreboard()
                return True

            elif board[3] == board[6] == board[9] != ' ':
                print(f' {self.turn} won!!')
                self.print_board(board)
                self.add_results(self.player_turn)
                self.scoreboard()
                return True
            
            elif board[1] == board[5] == board[9] != ' ':
                print(f' {self.turn} won!!')
                self.print_board(board)
                self.add_results(self.player_turn)
                self.scoreboard()
                return True

            elif board[3] == board[5] == board[7] != ' ':
                print(f' {self.turn} won!!')
                self.print_board(board)
                self.add_results(self.player_turn)
                self.scoreboard()
                return True
        
        if self.count == 9:
            print('Its a draw!!!')
            self.print_board(board)
            self.draws += 1
            self.scoreboard()
            return True

    def scoreboard(self):
        print('\n')
        print('\t   -------------------------------------')
        print('\t       SCOREBOARD')
        print('\t   -------------------------------------')
        print('\t   Player X \t  Tie \t  Player O')
        print(f'\t      {self.x_wins}   \t   {self.draws}   \t     {self.o_wins}')

    def add_results(self, turn):
        if turn % 2 == 0:
                    self.o_wins += 1
        else:
            self.x_wins += 1

    def start_game(self):
        print("\n")
        print(" Let's Play Tic Tac Toe")
        self.print_board(board)
        self.scoreboard()

    def play(self):
        self.start_game()

        game_on = True
        cells_played = []

        while game_on:
            print('\n')
            self.count += 1

            if self.count % 2 == 0:
                cell =int( input('Player O enter cell number: '))
                if  cell <= 0 or cell > 9 or cell in cells_played:
                    print('Cannot play there!!')
                    cell =int( input('Player O enter cell number: '))
                
                board[cell] = 'O'
                cells_played.append(cell)
            else:
                cell = int(input('Player X enter cell number: '))
                if cell <= 0 or cell > 9 or cell in cells_played:
                    print('Cannot play there!!')
                    cell = int(input('Player X enter cell number: '))
                
                board[cell] = 'X'
                cells_played.append(cell)
            
            self.player_turn += 1
            if self.player_turn % 2 != 0 :
                self.turn = 'Player X'
            else:
                self.turn = 'Player O'

            self.print_board(board)
            print('\n')

            if self.check_state(board):
                game_on = False


my_game = Game()
my_game.play()

