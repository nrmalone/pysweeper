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
                tk.Button(self.window,
                          width=4, height=2,
                          state="disabled", bd=2, relief="solid"
                          ).grid(row=i+1, column=j+1)
    
    def new_game(self, difficulty):
        pass

gui = Gui()