# This is the mail file to be run
# for our project.

# importing some libraries from tkinter module
# will be sueful to add graphical user interface
# in our game.
from tkinter import Frame, Label, CENTER

# importing the other two code files
# to use their functionalies we have
# already defined.
import LogicsFinal
import constants as c

# Creating the frame of our game
class Game2048(Frame):

    # function to define the GUI of the grid
    # at the time of start of game.
    def init_grid(self):

        # adding the background color.
        background = Frame(self, bg = c.BACKGROUND_COLOR_GAME,
                           width = c.SIZE, height = c.SIZE)
        background.grid()

        
        for i in range(c.GRID_LEN):

            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)

                cell.grid(row = i, column = j, padx = c.GRID_PADDING,
                          pady = c.GRID_PADDING)
                
                t=Label(master = cell, text = "",
                        bg = c.BACKGROUND_COLOR_CELL_EMPTY,
                        justify = CENTER, font = c.FONT,
                        width = 5, height = 2)
                
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    # Initialising the matrix 
    def init_matrix(self):
        
        self.matrix = LogicsFinal.start_game()
        LogicsFinal.add_new_2(self.matrix)
        LogicsFinal.add_new_2(self.matrix)

    # updating the interface of cells
    # of the grid.
    def update_grid_cells(self):
        
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):

                # Adding a new number to the matrix
                # after every slide or step
                new_number = self.matrix[i][j]
                
                if(new_number == 0):
                    self.grid_cells[i][j].configure(
                        text = "", bg = c.BACKGROUND_COLOR_CELL_EMPTY)
                    
                else:
                    self.grid_cells[i][j].configure(
                        text = str(new_number),
                        bg = c.BACKGROUND_COLOR_DICT[new_number],
                        fg = c.CELL_COLOR_DICT[new_number])

        self.update_idletasks()

    def key_down(self,event):
        
        key = repr(event.char)
        
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            
            if changed:
                
                LogicsFinal.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False

                # we will get the current status of the game, if it
                # is 'WON' then we will update the interface accordingly.
                # and in case of 'LOST' we will show the message "You Lose !"
                # to the user.
                if(LogicsFinal.get_current_state(self.matrix) == 'WON'):
                    
                    self.grid_cells[1][1].configure(
                        text = "You", bg = c.BACKGROUND_COLOR_CELL_EMPTY)

                    self.grid_cells[1][2].configure(
                        text = "Win!", bg = c.BACKGROUND_COLOR_CELL_EMPTY)

                if(LogicsFinal.get_current_state(self.matrix) == 'LOST'):
                    
                    self.grid_cells[1][1].configure(
                        text = "You",bg = c.BACKGROUND_COLOR_CELL_EMPTY)

                    self.grid_cells[1][2].configure(
                        text = "Lose!",bg = c.BACKGROUND_COLOR_CELL_EMPTY)

    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>",self.key_down)
        
        self.commands = {c.KEY_UP: LogicsFinal.move_up,
                         c.KEY_DOWN: LogicsFinal.move_down,
                         c.KEY_LEFT: LogicsFinal.move_left,
                         c.KEY_RIGHT: LogicsFinal.move_right}

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

# Calling out function which will launch our game
gamegrid = Game2048()

                    

                    
                    

