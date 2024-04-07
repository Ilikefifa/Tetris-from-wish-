
import tkinter as tk
from random import choice, randrange


class TetrisApp:
    board_width = 20
    board_height = 30
    title_size = 30
    shapes = [
        [[1, 1, 1, 1]],  # I
    ]
    colors = ["white"]

    def __init__(self, master):
        self.master = master
        master.title("Tetris Game")
        self.board = [[0] * TetrisApp.board_width for _ in range(TetrisApp.board_height)]
        self.current_block = None
        self.current_block_color = ""
        self.current_block_x = 0
        self.current_block_y = 0
        self.game_over = False

        self.canvas = tk.Canvas(self.master, width=TetrisApp.board_width * TetrisApp.title_size,
                                height=TetrisApp.board_height * TetrisApp.title_size)
        self.canvas.pack()
        self.new_block()
        self.update()

        self.master.bind("<Left>", lambda event: self.move_block(-1, 0))
        self.master.bind("<Right>", lambda event: self.move_block(1, 0))
        self.master.bind("<Down>", lambda event: self.move_block(0, 1))

    def new_block(self):
        self.current_block = choice(TetrisApp.shapes)
        self.current_block_color = choice(TetrisApp.colors)
        self.current_block_x = TetrisApp.board_width // 2 - len(self.current_block[0]) // 2
        self.current_block_y = 0

    def update(self):
        if not self.game_over:
            self.current_block_y += 1
        self.draw()
        self.master.after(400, self.update)

    def move_block(self, x, y):
        new_x = self.current_block_x + x
        new_y = self.current_block_y + y
        self.current_block_x = new_x
        self.current_block_y = new_y
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_tile(x, y, TetrisApp.colors[cell - 1])
            for y, row in enumerate(self.current_block):
                for x, cell in enumerate(row):
                    if cell:
                        self.draw_tile(self.current_block_x + x, self.current_block_y + y, self.current_block_color)

    def draw_tile(self, x, y, color):
        self.canvas.create_rectangle(x * TetrisApp.title_size, y * TetrisApp.title_size,
                                     (x+1) * TetrisApp.title_size, (y+1) * TetrisApp.title_size,
                                     fill=color, outline="black")


def main():
    root = tk.Tk()
    app = TetrisApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
