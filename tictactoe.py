"""

WELCOME TO MY TIC TAC TOE GAME VERSUS A COMPUTER-GENERATED USER! I USED COLORS TO DEPICT
POSITIONS AND TUPLES FOR WINNING/LOSING COMBINATIONS!

"I WOULD PREPARE TO FAIL WITH HONOR THAN WIN BY CHEATING." - SOPHOCLES

"""

import tkinter
import random

class Game(object):
    """
    class to support a tic tac toe app

    Argument:
    parent: (tkinter.Tk) the root window object

    Attributes:
    canvas:  (tkinter.Canvas) - our tic tac toe canvas
    parent:  (tkinter.Tk) - the root window object
    restart: (tkinter.Button) - restart button for canvas
    win_lose_message: (tkinter.Label) - label object displayed when win or lose

    """
    # class variables
    tile_size = 100
    position = []
    combo1 = [(1,), (2,), (3,)] # hortizontal
    combo2 = [(4,), (5,), (6,)] # hortizontal
    combo3 = [(7,), (8,), (9,)] # hortizontal
    combo4 = [(1,), (4,), (7,)] # vertical
    combo5 = [(2,), (5,), (8,)] # vertical
    combo6 = [(3,), (6,), (9,)] # vertical
    combo7 = [(1,), (5,), (9,)] # diagonal
    combo8 = [(3,), (5,), (7,)] # diagonal

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent
        restart_button = tkinter.Button(self.parent, text='RESTART', width=10,\
                                      command=self.restart)
        restart_button.grid()
        self.canvas = tkinter.Canvas(self.parent, width=self.tile_size * 3,\
                                     height=self.tile_size * 3)
        self.canvas.grid()
        for row in range(3):
            for column in range(3):
                color = 'white'
                self.canvas.create_rectangle(self.tile_size * column,
                                             self.tile_size * row,
                                             self.tile_size * (column + 1),
                                             self.tile_size * (row + 1),
                                             fill=color)

        self.canvas.bind("<Button-1>", self.play)
        self.win_lose_message = tkinter.Label(parent, text=" ")
        self.win_lose_message.grid()
        self.players_choice = [] # counts player's occupied tiles
        self.computers_choice = [] # counts computers's occupied tiles
        self.flag = True # for play functions
        self.color = 'maroon1' # color for player's tiles

        self.restart()

    def restart(self):
        """
        executes when player clicks on restart button
        parameter: none
        returns: none

        """
        for shape in self.canvas.find_all():
            self.canvas.itemconfigure(shape, fill='white')
        self.position = []
        self.players_choice = []
        self.computers_choice = []
        self.win_lose_message.configure(text='')
        self.flag = True

    def play(self, event):
        """
        function that allows player to move on tic tac toe board
        parameter: event (coordinates x and y)
        returns: none

        """
        while self.flag:
            self.player = self.canvas.find_closest(event.x, event.y)
            if self.player in self.position:
                return
            self.canvas.itemconfigure(self.player,fill=self.color)
            self.position.append(self.player)
            self.players_choice.append(self.player)
            remaining_computer = [(x,) for x in range(1,10) if (x,) not in \
                                  self.position]
            print(len(self.position))
            if len(remaining_computer) != 0: # check if available spots left
                self.computer = random.choice(remaining_computer)
                self.canvas.itemconfigure(self.computer, fill='cyan')
                self.position.append(self.computer)
                self.computers_choice.append(self.computer)
            self.flag = not self.check_win()

    def check_win(self):
        """
        checks if player wins or loses
        parameters: none
        returns: true (boolean) - stops while loop in play function so player
        stops clicking after win, lose, or tie

        """
        if set(self.players_choice).issuperset(self.combo1):
            self.win_lose_message.configure(text='You won!')
            return True

        if set(self.players_choice).issuperset(self.combo2):
            self.win_lose_message.configure(text='You won!')
            return True

        if set(self.players_choice).issuperset(self.combo3):
            self.win_lose_message.configure(text='You won!')
            return True

        if set(self.players_choice).issuperset(self.combo4):
            self.win_lose_message.configure(text='You won!')
            return True

        if set(self.players_choice).issuperset(self.combo5):
            self.win_lose_message.configure(text='You won!')
            return True

        if set(self.players_choice).issuperset(self.combo6):
            self.win_lose_message.configure(text='You won!')
            return True

        if set(self.players_choice).issuperset(self.combo7):
            self.win_lose_message.configure(text='You won!')
            return True

        if set(self.players_choice).issuperset(self.combo8):
            self.win_lose_message.configure(text='You won!')
            return True

        if set(self.computers_choice).issuperset(self.combo1):
            self.win_lose_message.configure(text='You lost!')
            return True

        if set(self.computers_choice).issuperset(self.combo2):
            self.win_lose_message.configure(text='You lost!')
            return True

        if set(self.computers_choice).issuperset(self.combo3):
            self.win_lose_message.configure(text='You lost!')
            return True

        if set(self.computers_choice).issuperset(self.combo4):
            self.win_lose_message.configure(text='You lost!')
            return True

        if set(self.computers_choice).issuperset(self.combo5):
            self.win_lose_message.configure(text='You lost!')
            return True

        if set(self.computers_choice).issuperset(self.combo6):
            self.win_lose_message.configure(text='You lost!')
            return True

        if set(self.computers_choice).issuperset(self.combo7):
            self.win_lose_message.configure(text='You lost!')
            return True

        if set(self.computers_choice).issuperset(self.combo8):
            self.win_lose_message.configure(text='You lost!')
            return True

        else:
            if len(self.position) == 9:
                self.win_lose_message.configure(text="It's a tie!")
                return True


def main():
    root = tkinter.Tk()
    tic_tac = Game(root)
    root.mainloop()


if __name__ == '__main__':
    main()
