import tkinter

class BoardGUI():
    def __init__(self, game):
        # Initialize parameters
        self.game = game
        self.ROWS = 8
        self.COLS = 8
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 800
        self.col_width = self.WINDOW_WIDTH / self.COLS
        self.row_height = self.WINDOW_HEIGHT / self.ROWS

        # Initialize GUI
        self.initBoard()

    def initBoard(self):
        self.root = tkinter.Tk()
        self.c = tkinter.Canvas(self.root, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT,
                                borderwidth=5, background='white')
        self.c.pack()
        self.board = [[0]*self.COLS for _ in range(self.ROWS)]
        self.tiles = [[None for _ in range(self.COLS)] for _ in range(self.ROWS)]

        # Print dark square
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    self.c.create_rectangle(i * self.row_height, j * self.col_width,
                                        (i+1) * self.row_height, (j+1) * self.col_width, fill="gray", outline="gray")

        # Print grid lines
        for i in range(8):
            self.c.create_line(0, self.row_height * i, self.WINDOW_WIDTH, self.row_height * i, width=2)
            self.c.create_line(self.col_width * i, 0, self.col_width * i, self.WINDOW_HEIGHT, width=2)