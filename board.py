import random
import tkinter as tk

class Cell:
    def __init__(self, isMine=False, isCleared=False, neighborMines=0, row=None, col=None):
        self.isMine = isMine
        self.isCleared = isCleared
        self.neighborMines = neighborMines
        self.row = None
        self.col = None

class Board:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.width = 0
        self.height = 0
        self.numMines = 0
        self.cells = {}

        match self.difficulty:
            case 'easy':
                side = random.randint(8, 10)
                self.width = side
                self.height = side
                self.numMines = 10
                print(f"width: {self.width}, height: {self.height}, numMines: {self.numMines}")
            case 'medium':
                self.width = random.randint(15,16) 
                self.height = random.randint(13, 16)
                self.numMines = 40
                print(f"width: {self.width}, height: {self.height}, numMines: {self.numMines}")
            case 'hard':
                self.width = 30
                self.height = 16
                self.numMines = 99
                print(f"width: {self.width}, height: {self.height}, numMines: {self.numMines}")

        self.generate_mines()
    
    def generate_mines(self):
        for row in range(self.height):
            for col in range(self.width):
                self.cells[row, col] = Cell(row=row, col=col)
        mine_coords = set()
        while len(mine_coords) < self.numMines:
            row = random.randint(0, self.height - 1)
            col = random.randint(0, self.width - 1)
            mine_coords.add((row, col))
        
        for row, col in mine_coords:
            self.cells[row, col].isMine = True
        
        for row in range(self.height):
            for col in range(self.width):
                cell = self.cells[row, col]
                cell.neighborMines = self.count_neighbors(row, col)
        print(mine_coords)
    
    def count_neighbors(self, row, col):
        numMines = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                r = row + dr
                c = col + dc
                if not (0 <= r < self.height and 0 <= c < self.width):
                    continue
                if self.cells[r, c].isMine:
                    numMines += 1
        return numMines
    
    def get_cells(self):
        return self.cells