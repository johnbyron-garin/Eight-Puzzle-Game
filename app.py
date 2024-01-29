import copy
import tkinter.messagebox as messagebox
from tkinter import filedialog
from tkinter import *
from functools import partial

def read_puzzle():
    global gridBoard
    try:
        with open("puzzle.in", "r") as file: # assigns the opened file object to the file variable and ensures that the file is properly closed when the block of code is exited
            gridBoard = [] # will store the puzzle data read from the file
            for line in file: # iterate each line
                row = [int(x) for x in line.strip().split()] # splits each element from each line with whitespaces
                gridBoard.append(row)
    except FileNotFoundError:
        # handle file not found error
        print("File 'puzzle.in' not found!")

def button_click(row, col):
    
     # Check if the puzzle is solved
    check_solved()

    if playable == False:
        messagebox.showinfo("Invalid Move", "Solution already clicked, the board is now unplayable")
        return

    if solved:  # check if the puzzle is already solved, if it is solved, clicking buttons will no longer change the position of the buttons
        solved_label.config(text="Solved!")
        return

    i = gridBoard[row][col]
    if i != 0:  # if non-zero value is clicked
        if row == 0 and col == 0:  # if the button in the [0][0] is clicked
            if gridBoard[row][col+1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col+1]  # move the right neighbor's value to the current button
                gridBoard[row][col+1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col+1].config(text=gridBoard[row][col+1])  

            elif gridBoard[row+1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row+1][col]  # move the neighbor's value to the current button
                gridBoard[row+1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row+1][col].config(text=gridBoard[row+1][col])  

        elif row == 0 and col == 1:  # if the button in the [0][1] is clicked
            if gridBoard[row][col-1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col-1]  # move the neighbor's value to the current button
                gridBoard[row][col-1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col-1].config(text=gridBoard[row][col-1])  

            elif gridBoard[row][col+1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col+1]  # move the neighbor's value to the current button
                gridBoard[row][col+1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col+1].config(text=gridBoard[row][col+1])  

            elif gridBoard[row+1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row+1][col]  # move the neighbor's value to the current button
                gridBoard[row+1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row+1][col].config(text=gridBoard[row+1][col])  

        elif row == 0 and col == 2:  # if the button in the [0][2] is clicked
            if gridBoard[row][col-1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col-1]  # move the neighbor's value to the current button
                gridBoard[row][col-1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col-1].config(text=gridBoard[row][col-1])  
            
            elif gridBoard[row+1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row+1][col]  # move the neighbor's value to the current button
                gridBoard[row+1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row+1][col].config(text=gridBoard[row+1][col])  

        elif row == 1 and col == 0: # if the button in the [1][0] is clicked
            if gridBoard[row][col+1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col+1]  # move the neighbor's value to the current button
                gridBoard[row][col+1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col+1].config(text=gridBoard[row][col+1])  

            elif gridBoard[row-1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row-1][col]  # move the neighbor's value to the current button
                gridBoard[row-1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row-1][col].config(text=gridBoard[row-1][col])  

            elif gridBoard[row+1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row+1][col]  # move the neighbor's value to the current button
                gridBoard[row+1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row+1][col].config(text=gridBoard[row+1][col])  
        
        elif row == 1 and col == 1: # if the button in the [1][1] is clicked
            if gridBoard[row][col-1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col-1]  # move the neighbor's value to the current button
                gridBoard[row][col-1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col-1].config(text=gridBoard[row][col-1])  

            elif gridBoard[row][col+1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col+1]  # move the neighbor's value to the current button
                gridBoard[row][col+1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col+1].config(text=gridBoard[row][col+1])  

            elif gridBoard[row-1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row-1][col]  # move the neighbor's value to the current button
                gridBoard[row-1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row-1][col].config(text=gridBoard[row-1][col])  

            elif gridBoard[row+1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row+1][col]  # move the neighbor's value to the current button
                gridBoard[row+1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row+1][col].config(text=gridBoard[row+1][col])  

        elif row == 1 and col == 2: # if the button in the [1][2] is clicked
            if gridBoard[row][col-1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col-1]  # move the neighbor's value to the current button
                gridBoard[row][col-1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col-1].config(text=gridBoard[row][col-1])  

            elif gridBoard[row-1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row-1][col]  # move the neighbor's value to the current button
                gridBoard[row-1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row-1][col].config(text=gridBoard[row-1][col])  

            elif gridBoard[row+1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row+1][col]  # move the neighbor's value to the current button
                gridBoard[row+1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row+1][col].config(text=gridBoard[row+1][col])  

        elif row == 2 and col == 0:  # if the button in the [2][0] is clicked
            if gridBoard[row][col+1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col+1]  # move the neighbor's value to the current button
                gridBoard[row][col+1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col+1].config(text=gridBoard[row][col+1])  
            
            elif gridBoard[row-1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row-1][col]  # move the neighbor's value to the current button
                gridBoard[row-1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row-1][col].config(text=gridBoard[row-1][col])  

        elif row == 2 and col == 1:  # if the button in the [2][1] is clicked
            if gridBoard[row][col-1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col-1]  # move the neighbor's value to the current button
                gridBoard[row][col-1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col-1].config(text=gridBoard[row][col-1])  

            elif gridBoard[row][col+1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col+1]  # move the neighbor's value to the current button
                gridBoard[row][col+1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col+1].config(text=gridBoard[row][col+1])  

            elif gridBoard[row-1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row-1][col]  # move the neighbor's value to the current button
                gridBoard[row-1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row-1][col].config(text=gridBoard[row-1][col])  

        if row == 2 and col == 2:  # if the button in the [0][0] is clicked
            if gridBoard[row][col-1] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row][col-1]  # move the neighbor's value to the current button
                gridBoard[row][col-1] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row][col-1].config(text=gridBoard[row][col-1])  

            elif gridBoard[row-1][col] == 0:
                temp = gridBoard[row][col]  # store the original value
                gridBoard[row][col] = gridBoard[row-1][col]  # move the neighbor's value to the current button
                gridBoard[row-1][col] = temp  # set the neighbor's value to the original value

                # Update button text to reflect the changes for both buttons
                buttons[row][col].config(text=gridBoard[row][col])
                buttons[row-1][col].config(text=gridBoard[row-1][col]) 

        # Update the i value after swapping
        i = gridBoard[row][col]
        
    check_solved()

    if solved:  # check if the puzzle is already solved, if it is solved, clicking buttons will no longer change the position of the buttons
        solved_label.config(text="Solved!")
        return
    
def check_solved():
    global solved
    if gridBoard == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
        solved = True
        print("Puzzle solved!")
        messagebox.showinfo("Solved", "Puzzle is solved!")

def check_solvable():
    global solvable
    # transfering the numbers from 2D array to 1D array for easy access
    alternative_arr = []
    for row in range(len(gridBoard)):
        for col in range(len(gridBoard[row])):
            alternative_arr.append(gridBoard[row][col])

    # comparing each number to each number to its right handside and then incrementing the value of the counter by 1 whenever the number on its right is less than the number being compared to
    # storing it to sum_array
    sum_array = []
    x = 0
    while x < len(alternative_arr):
        y = x + 1
        counter = 0
        if (alternative_arr[x] != 0):
            while y < len(alternative_arr):
                if (alternative_arr[x] > alternative_arr[y]) and (alternative_arr[y] != 0):
                    counter += 1
                y += 1
            sum_array.append(counter)
        x += 1

    # adding up all the counters being stored in the sum_array
    total = 0
    for sum in sum_array:
        total += sum

    # using the modulo operation to know if it is odd or even
    if (total % 2 != 0):
        solvable = False
    else:
        solvable = True

def check_if_solvable(gridBoard):
    # transfering the numbers from 2D array to 1D array for easy access
    alternative_arr = []
    for row in range(len(gridBoard)):
        for col in range(len(gridBoard[row])):
            alternative_arr.append(gridBoard[row][col])

    # comparing each number to each number to its right handside and then incrementing the value of the counter by 1 whenever the number on its right is less than the number being compared to
    # storing it to sum_array
    sum_array = []
    x = 0
    while x < len(alternative_arr):
        y = x + 1
        counter = 0
        if (alternative_arr[x] != 0):
            while y < len(alternative_arr):
                if (alternative_arr[x] > alternative_arr[y]) and (alternative_arr[y] != 0):
                    counter += 1
                y += 1
            sum_array.append(counter)
        x += 1

    # adding up all the counters being stored in the sum_array
    total = 0
    for sum in sum_array:
        total += sum

    # using the modulo operation to know if it is odd or even
    if (total % 2 != 0):
        return False
    else:
        return True

def config_solved_label(solved_label):
    if solved:
        solved_label.config(text="Solved!")
    else:
        solved_label.config(text="")
    
def config_solvable_label(solvable_label, gridBoard, button_frame, buttons):
    global algorithm_menu
    global solution_button
    global pathcost_label
    if solvable:
        solvable_label.config(text="Solvable")
        config_gridBoard(gridBoard, button_frame, buttons)
        algorithm_menu.pack()
        solution_button.pack()
        pathcost_label.pack()
    else:
        solvable_label.config(text="Sorry! The puzzle is unsolvable")

def config_gridBoard(gridBoard, button_frame, buttons):
    # iterates on each row and column in the gridBoard
    for row in range(len(gridBoard)):
        for col in range(len(gridBoard[row])):
            i = gridBoard[row][col] # holds the value given the indeces row and col
            # creates a button widget from the button_frame, uses i as its label text, and creates a callback for the function button_click with row and col as parameters
            b = Button(
                button_frame,
                text=str(i),
                command=partial(button_click, row, col),
                width=BUTTON_WIDTH,
                height=BUTTON_HEIGHT,
            ) 
            b.grid(row=row, column=col) # uses the grid method to specify the row and column where the button b should be placed within the button_frame
            buttons[row][col] = b # stores a reference to the created button b in the buttons 2D list
    # Set the size of the button_frame
    button_frame.config(width=FRAME_WIDTH, height=FRAME_HEIGHT)

def select_algorithm(selected_algorithm):
    global is_bfs
    global is_dfs
    global is_astar
    if selected_algorithm == "BFS":
        is_dfs = False
        is_bfs = True
        is_astar = False
    elif selected_algorithm == "DFS":
        is_dfs = True
        is_bfs = False
        is_astar = False
    elif selected_algorithm == "AStar":
        is_dfs = False
        is_bfs = False
        is_astar = True

def open_file():
    global playable
    global next_button
    global path_cost
    global solution_action
    global done_action
    global gridBoard
    global gridBoardCopy
    global button_frame
    global solvable
    
    file_path = filedialog.askopenfilename(filetypes=[("Input Files", "*.in")])
    if file_path:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
            copy_only = [list(map(int, line.split())) for line in lines]
            solvable = check_if_solvable(copy_only)
            if solvable:
                solvable_label.config(text="Solvable")
                button_frame.pack()
                open_button.pack_forget()
                open_button.pack()
                algorithm_menu.pack()
                solution_button.pack()

                gridBoard = copy_only
                gridBoardCopy = copy.deepcopy(gridBoard)
                config_gridBoard(gridBoardCopy, button_frame, buttons) # after loading the new file, the board will reconfigure along with the other widgets
                
                playable = True # makes the board playable
                next_button.pack_forget() # hides the next button

                path_cost = 0
                path = "Path Cost: {}".format(path_cost)
                pathcost_label.config(text=path)
                pathcost_label.pack_forget() # hides the pathcost label

                action_solution_text = "Solution: {}".format(" ".join(solution_action))
                action_solution_label.config(text=action_solution_text)
                action_solution_label.pack_forget() # hides the action solution label

                done_action = []
                done_action_text = ""
                done_action_label.config(text=done_action_text)
                done_action_label.pack_forget() # hides the done action label
            else:
                button_frame.pack_forget()
                algorithm_menu.pack_forget()
                solution_button.pack_forget()
                done_action_label.pack_forget()
                action_solution_label.pack_forget()
                pathcost_label.pack_forget()
                next_button.pack_forget()
                solvable_label.config(text="Sorry! The puzzle is unsolvable")

def solution_clicked():
    global playable
    global is_bfs
    global is_dfs
    global next_button
    global path_cost
    global gridBoardCopy
    global solution_action
    global done_action

    check_solved()
    if solved:
        return
    else:
        gridBoardCopy2 = copy.deepcopy(gridBoardCopy)

        playable = False # makes the board unplayable
        next_button.pack() # shows up the next button

        config_gridBoard(gridBoardCopy2, button_frame, buttons)

        path_cost = 0
        path = "Path Cost: {}".format(path_cost)
        pathcost_label.config(text=path)
        pathcost_label.pack()

        action_solution_text = "Solution: {}".format(" ".join(solution_action))
        action_solution_label.config(text=action_solution_text)
        action_solution_label.pack()

        done_action = []
        done_action_text = ""
        done_action_label.config(text=done_action_text)
        done_action_label.pack()
            
        if is_bfs:
            BFS_solution()
        elif is_dfs:
            DFS_solution()
        elif is_astar:
            AStar_solution()
        with open("puzzle.out", "w") as outfile:
            outfile.write(" ".join(map(str, solution_action)))

# Increase the button size by specifying width and height
BUTTON_WIDTH = 5
BUTTON_HEIGHT = 2
# Increase the frame size by specifying width and height
FRAME_WIDTH = 300
FRAME_HEIGHT = 300

# this list will be used to store references to Tkinter Button widgets that will be created later
buttons = [[None, None, None], [None, None, None], [None, None, None]] 

# initializing variables needed
gridBoard = []
solved = False
solvable = True
read_puzzle() # function call for reading the contents of the puzzle.in file

root = Tk() # create the root window for GUI application using the Tkinter library
root.title("Sliding Puzzle")

# setting up the label text that will indicate if the puzzle is either solvable or unsolvable
solvable_label = Label(root, text="", font=("Century Gothic", 12))
solvable_label.pack()

solved_label = Label(root, text="", font=("Century Gothic", 12))
solved_label.pack()

button_frame = Frame(root) # creates a tkinter Frame widget that is a child of the root window
button_frame.pack() # this packs the button_frame widget within the root window

check_solved()
config_solved_label(solved_label)

selected_algorithm = StringVar()
selected_algorithm.set("BFS")

open_button = Button(root, text="Open File", command=open_file)
open_button.pack()

algorithm_menu = OptionMenu(root, selected_algorithm, "BFS", "DFS", "AStar", command=select_algorithm)
algorithm_menu.pack_forget()

solution_button = Button(root, text="Solution", font=("Century Gothic", 12), command=solution_clicked)
solution_button.pack_forget()

pathcost_label = Label(root, text="", font=("Century Gothic", 12))
pathcost_label.pack_forget()

# conditional statements that will change the text label depending on the state of the puzzle
check_solvable()
config_solvable_label(solvable_label, gridBoard, button_frame, buttons)

def GoalTest(currentState):
    gridBoard = currentState.get("gridboard")
    if(gridBoard == [[1,2,3],[4,5,6],[7,8,0]]):
        return True
    else:
        return False
    
def Action(currentState):
    action = []
    gridBoard = currentState.get("gridboard")
    for row in range(len(gridBoard)):
        for col in range(len(gridBoard[row])):
            if gridBoard[row][col] == 0:
                # URDL
                if row == 0 and col == 0: # if the button in the [0][0] is clicked
                    action.append("R")
                    action.append("D")
                elif row == 0 and col == 1: # if the button in the [0][1] is clicked
                    action.append("R")
                    action.append("D")
                    action.append("L")
                elif row == 0 and col == 2: # if the button in the [0][2] is clicked
                    action.append("D")
                    action.append("L")
                elif row == 1 and col == 0: # if the button in the [1][0] is clicked
                    action.append("U")
                    action.append("R")
                    action.append("D")
                elif row == 1 and col == 1: # if the button in the [1][1] is clicked
                    action.append("U")
                    action.append("R")
                    action.append("D")
                    action.append("L")
                elif row == 1 and col == 2: # if the button in the [1][2] is clicked
                    action.append("U")
                    action.append("D")
                    action.append("L")
                elif row == 2 and col == 0: # if the button in the [2][0] is clicked
                    action.append("U")
                    action.append("R")
                elif row == 2 and col == 1: # if the button in the [2][1] is clicked
                    action.append("U")
                    action.append("R")
                    action.append("L")
                elif row == 2 and col == 2: # if the button in the [2][2] is clicked
                    action.append("U")
                    action.append("L")
    return action

def Result(currentState, action):
    gridBoard = copy.deepcopy(currentState.get("gridboard"))
    empty_row, empty_col = find_empty_position(gridBoard)  # Find the current position of the empty cell

    if action == 'U' and empty_row > 0:
        gridBoard[empty_row][empty_col], gridBoard[empty_row - 1][empty_col] = gridBoard[empty_row - 1][empty_col], gridBoard[empty_row][empty_col]
    elif action == 'R' and empty_col < 2:
        gridBoard[empty_row][empty_col], gridBoard[empty_row][empty_col + 1] = gridBoard[empty_row][empty_col + 1], gridBoard[empty_row][empty_col]
    elif action == 'D' and empty_row < 2:
        gridBoard[empty_row][empty_col], gridBoard[empty_row + 1][empty_col] = gridBoard[empty_row + 1][empty_col], gridBoard[empty_row][empty_col]
    elif action == 'L' and empty_col > 0:
        gridBoard[empty_row][empty_col], gridBoard[empty_row][empty_col - 1] = gridBoard[empty_row][empty_col - 1], gridBoard[empty_row][empty_col]

    return gridBoard

def find_empty_position(gridBoard):
    for row in range(len(gridBoard)):
        for col in range(len(gridBoard[row])):
            if gridBoard[row][col] == 0:
                return row, col

def PathCost(currentState, explored_dict):
    cost = 0
    parent = currentState.get("parent")
    while True:
        for ex in explored_dict:
            if ex.get("name") == parent:
                cost += 1
                break
        if ex.get("parent") == 0:
            break
        else:
            parent = ex.get("parent")
    return cost

def Solution(solution_array, currentState, explored_dict):
    solution_array.append(currentState)
    parent = currentState.get("parent")
    while True:
        for ex in explored_dict:
            if ex.get("name") == parent:
                break
        if ex.get("parent") == 0:
            break
        else:
            solution_array.append(ex)
            parent = ex.get("parent")
    solution_array.reverse()
    return solution_array

def BFS_solution():
    global gridBoardCopy
    global solution_gridBoard
    global solution_action
    frontier = []
    explored = []
    explored_dict = []
    solution_array = []
    action_array = []
    gridboard_path = []

    gridBoardCopy2 = copy.deepcopy(gridBoardCopy)
    
    parent = 0
    state_num = 1
    state = {
        "name": "S" + str(state_num),
        "parent": parent,
        "gridboard": gridBoardCopy2,
        "action": ""
    }
    
    frontier.append(state) # appends the initial state to the frontier
    currentState = frontier.pop(0) # dequeues the frontier queue

    while True:
        parent = currentState.get("name")
        explored_dict.append(currentState)
        explored.append(currentState.get("gridboard")) #appends the initial state to the explored states
        print("explored states:", len(explored))
        if GoalTest(currentState)==True:
            cost = PathCost(currentState, explored_dict)
            solution = Solution(solution_array, currentState, explored_dict)
            for s in solution:
                action_array.append(s.get("action"))
                gridboard_path.append(s.get("gridboard"))

            print("path cost: ", cost)
            print("solution: ", action_array)
            print("explored states:", len(explored))

            action_solution = "Solution: {}".format(" ".join(action_array))
            action_solution_label.config(text=action_solution)

            solution_gridBoard = copy.deepcopy(gridboard_path)
            solution_action = copy.deepcopy(action_array)

            return
        else:
            actions = Action(currentState)
            for action in actions:
                result = Result(currentState, action)
                if result not in [state.get("gridboard") for state in frontier]:
                    if result not in explored:
                        state_num += 1
                        state = {
                            "name": "S" + str(state_num),
                            "parent": parent,
                            "gridboard": result,
                            "action": action
                        }
                        frontier.append(state) # frontier.enqueue

        currentState = frontier.pop(0) # dequeues the frontier queue

        if len(frontier) == 0:
            break

def DFS_solution():
    global gridBoardCopy
    global solution_gridBoard
    global solution_action
    frontier = []
    explored = []
    explored_dict = []
    solution_array = []
    action_array = []
    gridboard_path = []

    gridBoardCopy2 = copy.deepcopy(gridBoardCopy)
    
    parent = 0
    state_num = 1
    state = {
        "name": "S" + str(state_num),
        "parent": parent,
        "gridboard": gridBoardCopy2,
        "action": ""
    }
    
    frontier.append(state) # appends the initial state to the frontier
    currentState = frontier.pop(0) # dequeues the frontier queue

    while True:
        parent = currentState.get("name")
        explored_dict.append(currentState)
        explored.append(currentState.get("gridboard")) #appends the initial state to the explored states
        print("explored states:", len(explored))
        if GoalTest(currentState)==True:
            cost = PathCost(currentState, explored_dict)
            solution = Solution(solution_array, currentState, explored_dict)
            for s in solution:
                action_array.append(s.get("action"))
                gridboard_path.append(s.get("gridboard"))

            print("path cost: ", cost)
            print("solution: ", action_array)
            print("explored states:", len(explored))

            action_solution = "Solution: {}".format(" ".join(action_array))
            action_solution_label.config(text=action_solution)

            solution_gridBoard = copy.deepcopy(gridboard_path)
            solution_action = copy.deepcopy(action_array)

            return
        else:
            actions = Action(currentState)
            for action in actions:
                result = Result(currentState, action)
                if result not in [state.get("gridboard") for state in frontier]:
                    if result not in explored:
                        state_num += 1
                        state = {
                            "name": "S" + str(state_num),
                            "parent": parent,
                            "gridboard": result,
                            "action": action
                        }
                        frontier.insert(0, state) # frontier.enqueue

        currentState = frontier.pop(0) # dequeues the frontier queue

        if len(frontier) == 0:
            break

def calculate_F(resultingGrid, bestNode, explored_dict):
    f = 0
    col_diff = 0
    row_diff = 0
    g = PathCost(bestNode, explored_dict)
    h = 0
    for row in range(len(resultingGrid)):
        for col in range(len(resultingGrid[row])):
            gridValue = resultingGrid[row][col]
            if gridValue == 1:
                row_diff = abs(0 - row)
                col_diff = abs(0 - col)
                h = h + row_diff + col_diff
            elif gridValue == 2:
                row_diff = abs(0 - row)
                col_diff = abs(1 - col)
                h = h + row_diff + col_diff
            elif gridValue == 3:
                row_diff = abs(0 - row)
                col_diff = abs(2- col)
                h = h + row_diff + col_diff
            elif gridValue == 4:
                row_diff = abs(1 - row)
                col_diff = abs(0 - col)
                h = h + row_diff + col_diff
            elif gridValue == 5:
                row_diff = abs(1 - row)
                col_diff = abs(1 - col)
                h = h + row_diff + col_diff
            elif gridValue == 6:
                row_diff = abs(1 - row)
                col_diff = abs(2 - col)
                h = h + row_diff + col_diff
            elif gridValue == 7:
                row_diff = abs(2 - row)
                col_diff = abs(0 - col)
                h = h + row_diff + col_diff
            elif gridValue == 8:
                row_diff = abs(2 - row)
                col_diff = abs(1 - col)
                h = h + row_diff + col_diff
                
    f = g + h
    return f 

def calculate_G(bestNode, explored_dict):
    g = PathCost(bestNode, explored_dict)
    return g

def calculate_H(resultingGrid):
    col_diff = 0
    row_diff = 0
    h = 0
    for row in range(len(resultingGrid)):
        for col in range(len(resultingGrid[row])):
            gridValue = resultingGrid[row][col]
            if gridValue == 1:
                row_diff = abs(0 - row)
                col_diff = abs(0 - col)
                h = h + row_diff + col_diff
            elif gridValue == 2:
                row_diff = abs(0 - row)
                col_diff = abs(1 - col)
                h = h + row_diff + col_diff
            elif gridValue == 3:
                row_diff = abs(0 - row)
                col_diff = abs(2- col)
                h = h + row_diff + col_diff
            elif gridValue == 4:
                row_diff = abs(1 - row)
                col_diff = abs(0 - col)
                h = h + row_diff + col_diff
            elif gridValue == 5:
                row_diff = abs(1 - row)
                col_diff = abs(1 - col)
                h = h + row_diff + col_diff
            elif gridValue == 6:
                row_diff = abs(1 - row)
                col_diff = abs(2 - col)
                h = h + row_diff + col_diff
            elif gridValue == 7:
                row_diff = abs(2 - row)
                col_diff = abs(0 - col)
                h = h + row_diff + col_diff
            elif gridValue == 8:
                row_diff = abs(2 - row)
                col_diff = abs(1 - col)
                h = h + row_diff + col_diff
                
    return h 

def getMinF(openList):
    min_F_value = openList[0].get("F")
    index_min_F_value = 0
    state_counter = 0
    for node in openList:
        F_value = node.get("F")
        if F_value < min_F_value:
            min_F_value = F_value
            index_min_F_value = state_counter
        state_counter += 1
    return index_min_F_value

def AStar_solution():
    global gridBoardCopy
    global solution_gridBoard
    global solution_action
    openList = []
    closedList = []
    explored_dict = []
    solution_array = []
    action_array = []
    gridboard_path = []
    
    gridBoardCopy2 = copy.deepcopy(gridBoardCopy)

    parent = 0
    state_num = 1
    state = {
        "name": "S" + str(state_num),
        "parent": parent,
        "gridboard": gridBoardCopy2,
        "action": "",
        "F": 0,
        "G": 0,
        "H": 0,
    }
    
    openList.append(state) # appends the initial state to the openList
    list_index = getMinF(openList)
    bestNode = openList.pop(list_index) # pops the node with minimum F value 
    
    parent = bestNode.get("name")
    explored_dict.append(bestNode)
    
    F_value = calculate_F(bestNode.get("gridboard"), bestNode, explored_dict)
    bestNode["F"] = F_value
    
    G_value = calculate_G(bestNode, explored_dict)
    bestNode["G"] = G_value
    
    H_value = calculate_H(bestNode.get("gridboard"))
    bestNode["H"] = H_value

    while True:
        closedList.append(bestNode.get("gridboard")) #appends the initial state to the explored states
        print("explored states:", len(closedList))
        
        if GoalTest(bestNode)==True:
            cost = PathCost(bestNode, explored_dict)
            solution = Solution(solution_array, bestNode, explored_dict)
            for s in solution:
                action_array.append(s.get("action"))
                gridboard_path.append(s.get("gridboard"))

            print("path cost: ", cost)
            print("solution: ", action_array)
            print("explored states:", len(closedList))

            action_solution = "Solution: {}".format(" ".join(action_array))
            action_solution_label.config(text=action_solution)

            solution_gridBoard = copy.deepcopy(gridboard_path)
            solution_action = copy.deepcopy(action_array)

            return
        else:
            actions = Action(bestNode)
            for action in actions:
                result = Result(bestNode, action)
                if result not in [state.get("gridboard") for state in openList]:
                    if result not in closedList:
                        state_num += 1
                        state = {
                            "name": "S" + str(state_num),
                            "parent": parent,
                            "gridboard": result,
                            "action": action,
                            "F": calculate_F(result, bestNode, explored_dict) + 1,
                            "G": calculate_G(bestNode, explored_dict) + 1,
                            "H": calculate_H(result)
                        }
                        openList.append(state) # openList.enqueue
                else:
                    for state in openList:
                        if state.get("gridboard") == result:
                            result_g_value = calculate_G(bestNode, explored_dict) + 1
                            if result_g_value < state.get("G"):
                                state_num += 1
                                node = {
                                    "name": "S" + str(state_num),
                                    "parent": parent,
                                    "gridboard": result,
                                    "action": action,
                                    "F": calculate_F(result, bestNode, explored_dict) + 1,
                                    "G": calculate_G(bestNode, explored_dict) + 1,
                                    "H": calculate_H(result)
                                }
                                openList.append(node) # openList.enqueue
        
        list_index = getMinF(openList)
        bestNode = openList.pop(list_index)
        
        parent = bestNode.get("name")
        explored_dict.append(bestNode)

        if len(openList) == 0:
            break

def next_state():
    global button_frame
    global buttons
    global solution_gridBoard
    global path_cost
    global solution_action
    global done_action

    if len(solution_gridBoard) == 0:
        messagebox.showinfo("Invalid Move", "You already reached the goal")
    elif len(solution_gridBoard) == 1:
        path_cost += 1
        path = "Path Cost: {}".format(path_cost)
        pathcost_label.config(text=path) # updates the path cost on ui

        board = solution_gridBoard.pop(0)
        config_gridBoard(board, button_frame, buttons) # updates the gridboard config while next button is clicked

        done = solution_action.pop(0)
        done_action.append(done)
        action_solution_text = "Solution: {}".format(" ".join(solution_action))
        action_solution_label.config(text=action_solution_text)
        done_action_text = "Actions Done: {}".format(" ".join(done_action))
        done_action_label.config(text=done_action_text)

        message = "The puzzle was solved with a solution guide with {} path cost".format(path_cost)
        messagebox.showinfo("Goal reached!", message)
    else:
        path_cost += 1
        path = "Path Cost: {}".format(path_cost)
        pathcost_label.config(text=path) # updates the path cost on ui

        board = solution_gridBoard.pop(0)
        config_gridBoard(board, button_frame, buttons) # updates the gridboard config while next button is clicked

        done = solution_action.pop(0)
        done_action.append(done)
        action_solution_text = "Solution: {}".format(" ".join(solution_action))
        action_solution_label.config(text=action_solution_text)
        done_action_text = "Actions Done: {}".format(" ".join(done_action))
        done_action_label.config(text=done_action_text)

    
is_bfs = True
is_dfs = False
is_astar = False
playable = True
solution_gridBoard = []
solution_action = []
done_action = []
path_cost = 0
gridBoardCopy = copy.deepcopy(gridBoard)

action_solution_label = Label(root, text="", font=("Century Gothic", 12))
action_solution_label.pack()

done_action_label = Label(root, text="", font=("Century Gothic", 12))
done_action_label.pack()

# initially the next button is invisible
next_button = Button(root, text="Next", font=("Century Gothic", 12), command=next_state)
next_button.pack_forget()

root.mainloop()
