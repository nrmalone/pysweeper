import tkinter as tk
import board

WINDOW_BG = '#848888'
BG = '#C1CDCD'
FG = '#000000'
FONT = ("Arial", 12)

class Gui():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Minesweeper")
        self.window.configure(bg=WINDOW_BG, padx=10, pady=10)

        self.difficulty = tk.StringVar()
        self.difficulty.set('medium')
        self.create_difficulty_buttons()
        self.placeholder = tk.Frame(self.window)
        self.placeholder.grid(row=1, column=1, rowspan=8, columnspan=8)
        self.placeholder_grid()

        self.newGameButton = tk.Button(self.window, command=lambda: self.new_game(self.difficulty.get()),
                                       text="New Game", bg=BG, fg=FG, font=FONT, bd=5, relief="raised"
                                       ).grid(column=0, row=4, pady=(5,0), padx=(0,5))
        
        self.window.mainloop()
    
    def create_difficulty_buttons(self):
        difficultyLabel = tk.Label(self.window, text="Difficulty:",
                                   font=FONT, bg=BG, fg=FG, bd=5, relief="raised", pady=2
                                   ).grid(row=0, column=0, pady=(0,5))
        difficulties = ['easy', 'medium', 'hard']
        for i, difficulty in enumerate(difficulties):
            tk.Radiobutton(self.window, 
                           text=difficulty.capitalize(), variable=self.difficulty, value=difficulty,
                           font=FONT, bg=BG, fg=FG, bd=5, relief="groove"
                           ).grid(row=(i+1), column=0, pady=(5,0), padx=(0,5))
    
    def placeholder_grid(self):
        for i in range(0, 8):
            for j in range(0, 8):
                tk.Button(self.placeholder,
                          width=4, height=2,
                          state="disabled", bd=2, relief="solid"
                          ).grid(row=i, column=j)
    
    def new_game(self, difficulty):
        for child in self.placeholder.winfo_children():
            child.destroy()
        self.placeholder.destroy()
        
        self.board = board.Board(self.difficulty.get())
        self.create_cell_buttons()

    def create_cell_buttons(self):
        self.cellButton = {}
        boardFrame = tk.Frame(self.window)
        boardFrame.grid(row=1, column=1, rowspan=self.board.width, columnspan=self.board.height)
        for (row, col), cell in self.board.get_cells().items():
            self.cellButton[row, col] = tk.Button(boardFrame, width=4, height=2, relief="raised", command=lambda r=row, c=col: self.clicked(r, c))
            self.cellButton[row, col].grid(row=row, column=col)

    def clicked(self, row, col):
        cell = self.board.get_cells()[(row, col)]
        if cell.isMine:
            self.cellButton[row, col].config(text="X", bg="red")
            for (r, c), button in self.cellButton.items():
                button.config(state="disabled")
            tk.messagebox.showinfo("Game Over", "You lost!")
        else:
            self.clear_cell(row, col)

    def clear_cell(self, row, col):
        cell = self.board.get_cells()[(row, col)]
        if cell.isCleared:
            return
        cell.isCleared = True
        self.cellButton[row, col].config(text=str(cell.neighborMines), relief="sunken", state="disabled")
        if cell.neighborMines == 0:
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    r = row + dr
                    c = col + dc
                    if (0 <= r < self.board.height and 0 <= c < self.board.width and not self.board.get_cells()[(r, c)].isMine):
                        self.clear_cell(r, c)
                        
gui = Gui()