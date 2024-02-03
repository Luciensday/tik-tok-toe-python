
# Below is the same program as in the example. Your
# challenge is to implement some improvements:

# 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this.

# 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point.

# 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board.

# 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.

# This is getting really challenging now — and is entirely
# optional. Don't forget about your assessment!

def play_game():
  (board, board_size) = create_board()
  player = "X"
  
  while not is_game_over(board, board_size):
    print(print_board(board))
    print("It's " + player + "'s turn.")  

    make_move(board, board_size, player)
    if player == "X":
      player = "O"
    else:
      player = "X"
  print(print_board(board))
  print("Game over!")



def create_board(): 
  board_size = int(input("Enter board size in odd number: "))
  if board_size % 2 == 1 and board_size > 2:
    board = [["." for x in range(board_size)] for y in range(board_size)]
    return (board, board_size) 
  else: 
    print("choose odd number from 3")
    create_board()
    
    
def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid

def make_move(board, board_size, player):
  row = int(input("Enter a row: "))
  column = int(input("Enter a column: "))
  
  if row > board_size -1 or column > board_size -1:
    print(f'choose row and column between 0 to {board_size - 1}')
    make_move(board, board_size, player)
  elif board[row][column] == "." :
      board[row][column] = player
      return board
  else: 
    print("choose other tile!")
    make_move(board, board_size, player)



# This function will extract three cells from the board
def get_cells(board, *group):
  return  [board[row-1][col-1] for row, col in group]
 
def is_group_complete(board, *group):
  cells = get_cells(board, *group)
  return "." not in cells

# This function will check if the group is all the same
def are_all_cells_the_same(board, *group):
  cells = get_cells(board, *group)
  return all(cell == cells[0] for cell in cells)

# We'll make a list of groups to check:
def generate_groups_to_check(board_size): 
  groups_to_check = []
  # Rows
  for i in range(board_size): 
    row_group = [(i,j) for j in range(board_size)]
    groups_to_check.append(row_group)

  for j in range(board_size): 
    column_group = [(i, j ) for i in range(board_size)]
    groups_to_check.append(column_group)

  diagonals1 = [(i,i) for i in range(board_size)]
  groups_to_check.append(diagonals1)

  diagonals2 = [(i, board_size - i) for i in range(board_size)]
  groups_to_check.append(diagonals2)

  return groups_to_check



def is_game_over(board, board_size): 
  groups_to_check = generate_groups_to_check(board_size)
  for group in groups_to_check:
   
  
    
    if is_group_complete(board, *group) and are_all_cells_the_same(board, *group):
        return True # We found a winning row!
 
  if all("." not in row for row in board): 
    return True
  else: 
    return False # If we get here, we didn't find a winning row

# And test it out:

print("Game time!")
play_game()
