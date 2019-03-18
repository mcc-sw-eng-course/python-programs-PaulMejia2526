from tkinter import *
from tkinter import Tk
import Tic_Tac_Toe_Controller

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', textvariable=None):
        super().__init__(master, textvariable=textvariable)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class Tic_Tac_Toe_UI(Tk):
    WINDOW_SIZE = 600
    WINDOW_COLOR = 'beige'
    CELL_SIZE = (WINDOW_SIZE - WINDOW_SIZE / 5)/3
    WINDOW_SIZE = 600  # pixels
    GRID_LINE_WIDTH = 2  # pixels
    SYMBOL_WIDTH = WINDOW_SIZE / 12  # pixels - adjust ratio

    SYMBOL_SIZE = 0.5
    X_COLOR = 'dodger blue'
    O_COLOR = 'tomato'
    DRAW_SCREEN_COLOR = 'light sea green'
    GRID_COLOR = 'light grey'
    BG_COLOR = 'white'
    FIRST_PLAYER = 2  # 1 - X, 2 = O
    STATE_TITLE_SCREEN = 0
    STATE_X_TURN = 1
    STATE_O_TURN = 2
    STATE_GAME_OVER = 3

    EMPTY = 0
    X = 1
    O = 2

    def __init__(self):
        Tk.__init__(self)
        self.gameController = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller()

        self.init_start_window()


    def init_start_window(self):
        # placeholder title screen

        row = Frame(self, width = Tic_Tac_Toe_UI.WINDOW_SIZE, height = Tic_Tac_Toe_UI.WINDOW_SIZE)
        self.playerName = StringVar()
        self.gamePlayer = EntryWithPlaceholder(row, "Player 1", textvariable=self.playerName)
        self.gamePlayer.pack()

        startGameButton = Button(row, height=2, width=30, text="Start Game", command=self.init_start_game)
        startGameButton.pack()
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        self.row = row

    def init_start_game(self):
        self.clear()
        self.playerCounter = 0
        self.init_game_data()
        self.init_board_window()

    def init_game_data(self):
        player1 = self.playerName.get()
        self.gameController = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller()
        self.gameController.init_players_data(player1)
        self.gameController.gameData.gameState = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller.STATE_GAME_IN_COURSE

    def init_board_window(self):

        self.canvasTop = Canvas(
            height=Tic_Tac_Toe_UI.WINDOW_SIZE/5, width=Tic_Tac_Toe_UI.WINDOW_SIZE,
            bg=Tic_Tac_Toe_UI.WINDOW_COLOR)

        self.canvasTop.create_text(
            100,
            20,
            text='Player 1: ' + self.gameController.getPlayer1(), fill='black',
            font=('Franklin Gothic', int(-Tic_Tac_Toe_UI.WINDOW_SIZE / 36), 'bold'))

        self.canvasBoard = Canvas(
            height=(Tic_Tac_Toe_UI.WINDOW_SIZE - Tic_Tac_Toe_UI.WINDOW_SIZE / 5), width=(Tic_Tac_Toe_UI.WINDOW_SIZE - Tic_Tac_Toe_UI.WINDOW_SIZE / 5),
            bg=Tic_Tac_Toe_UI.WINDOW_COLOR)

        for n in range(1, 3):
            # vertical
            self.canvasBoard.create_line(
                Tic_Tac_Toe_UI.CELL_SIZE * n, 0,
                Tic_Tac_Toe_UI.CELL_SIZE * n, Tic_Tac_Toe_UI.WINDOW_SIZE,
                width=Tic_Tac_Toe_UI.GRID_LINE_WIDTH, fill=Tic_Tac_Toe_UI.GRID_COLOR)
            # horizontal
            self.canvasBoard.create_line(
                0, Tic_Tac_Toe_UI.CELL_SIZE * n,
                Tic_Tac_Toe_UI.WINDOW_SIZE, Tic_Tac_Toe_UI.CELL_SIZE * n,
                width=Tic_Tac_Toe_UI.GRID_LINE_WIDTH, fill=Tic_Tac_Toe_UI.GRID_COLOR)

        self.canvasBottom= Canvas(
            height=Tic_Tac_Toe_UI.WINDOW_SIZE / 5, width=Tic_Tac_Toe_UI.WINDOW_SIZE,
            bg=Tic_Tac_Toe_UI.WINDOW_COLOR)

        self.canvasBottom.create_text(
            100,
            20,
            text='Player 2: '+ self.gameController.getPlayer2(), fill='black',
            font=('Franklin Gothic', int(-Tic_Tac_Toe_UI.WINDOW_SIZE / 36), 'bold'))

        self.canvasBoard.bind("<Button-1>", self.do_move_click)
        self.canvasTop.pack()
        self.canvasBoard.pack()
        self.canvasBottom.pack()

    def do_move_click(self, event):
        if (self.gameController.gameData.gameState == Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller.STATE_GAME_IN_COURSE):
            x = self.ptgrid(event.x)
            y = self.ptgrid(event.y)
            playerMove = self.gameController.newMove(event.x, event.y, Tic_Tac_Toe_UI.CELL_SIZE)
            if (playerMove != None):
                self.draw_X(x, y)
                if self.gameController.gameData.gameState == Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller.STATE_GAME_IN_COURSE:
                    resultMove = self.gameController.newMoveVsComputer(Tic_Tac_Toe_UI.CELL_SIZE)
                    if(resultMove != None):
                        x = self.ptgrid(resultMove["x"])
                        y = self.ptgrid(resultMove["y"])
                        self.draw_O(x, y)

            if self.gameController.gameData.gameState == Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller.STATE_GAME_OVER:
                self.gameover_screen(self.gameController.gameData.winner_player)



    def gameover_screen(self, winnerPlayer):
        # placeholder gameover screen

        self.canvasBoard.delete('all')
        self.canvasTop.delete('all')
        self.canvasBottom.delete('all')

        if winnerPlayer == None:
            wintext = 'Draw'
            wincolor = Tic_Tac_Toe_UI.DRAW_SCREEN_COLOR

        else:
            wintext = winnerPlayer.playerName + ' wins'
            if(winnerPlayer.playerShape == "X"):
                wincolor = Tic_Tac_Toe_UI.X_COLOR

            elif (winnerPlayer.playerShape == "O"):
                wincolor = Tic_Tac_Toe_UI.O_COLOR

        self.canvasBoard.create_rectangle(
            0, 0,
            Tic_Tac_Toe_UI.WINDOW_SIZE, Tic_Tac_Toe_UI.WINDOW_SIZE,
            fill=wincolor, outline='')

        self.canvasBoard.create_text(
            int(Tic_Tac_Toe_UI.WINDOW_SIZE / 2), int(Tic_Tac_Toe_UI.WINDOW_SIZE / 2),
            text=wintext, fill='white',
            font=('Franklin Gothic', int(-Tic_Tac_Toe_UI.WINDOW_SIZE / 20), 'bold'))


    def draw_X(self, grid_x, grid_y):
        """
        draw the X symbol at x, y in the grid
        """

        x = self.gtpix(grid_x)
        y = self.gtpix(grid_y)
        delta = Tic_Tac_Toe_UI.CELL_SIZE / 2 * Tic_Tac_Toe_UI.SYMBOL_SIZE

        self.canvasBoard.create_line(
            x - delta, y - delta,
            x + delta, y + delta,
            width=Tic_Tac_Toe_UI.SYMBOL_WIDTH, fill=Tic_Tac_Toe_UI.X_COLOR)

        self.canvasBoard.create_line(
            x + delta, y - delta,
            x - delta, y + delta,
            width=Tic_Tac_Toe_UI.SYMBOL_WIDTH, fill=Tic_Tac_Toe_UI.X_COLOR)

    def draw_O(self, grid_x, grid_y):
        """
        draw an O symbol at x, y in the grid

        note : a big outline value appears to cause a visual glitch in tkinter
        """

        x = self.gtpix(grid_x)
        y = self.gtpix(grid_y)
        delta = Tic_Tac_Toe_UI.CELL_SIZE / 2 * Tic_Tac_Toe_UI.SYMBOL_SIZE

        self.canvasBoard.create_oval(
            x - delta, y - delta,
            x + delta, y + delta,
            width=Tic_Tac_Toe_UI.SYMBOL_WIDTH, outline=Tic_Tac_Toe_UI.O_COLOR)


    def gtpix(self, grid_coord):
        # gtpix = grid_to_pixels
        # for a grid coordinate, returns the pixel coordinate of the center
        # of the corresponding cell

        pixel_coord = grid_coord * Tic_Tac_Toe_UI.CELL_SIZE + Tic_Tac_Toe_UI.CELL_SIZE / 2
        return pixel_coord

    def ptgrid(self, pixel_coord):
        # ptgrid = pixels_to_grid
        # the opposit of gtpix()

        # somehow the canvas has a few extra pixels on the right and bottom side
        if pixel_coord >= Tic_Tac_Toe_UI.WINDOW_SIZE:
            pixel_coord = Tic_Tac_Toe_UI.WINDOW_SIZE - 1

        grid_coord = int(pixel_coord / Tic_Tac_Toe_UI.CELL_SIZE)
        return grid_coord




    def exit(self, event):
        self.destroy()

    def clear(self):
        self.row.destroy()



def main():
    root = Tic_Tac_Toe_UI()
    root.mainloop()

main()