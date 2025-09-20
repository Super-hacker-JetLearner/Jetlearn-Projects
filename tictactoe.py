import pgzrun
import pygame

WIDTH = 600
HEIGHT = 600

import copy
print('imported')
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def check_if_win(board, player):
  # if board[0] == [player, player, player]:
  #   return 1
  for i in board:
    if i == [player, player, player]:
      return 1
  for i in range (0,3):
    if board[0][i] == player and board[1][i] == player and board[2][i] == player:
      return 1
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return 1
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return 1
  return 0

# b = [[1,3,1],
#      [3,3,0],
#      [1,0,1]]

# print(check_if_win(b, 1))
# print(check_if_win(b, 0))

def draw_x(index):
    x,y = index
    x = x * 200 + 100
    y = y * 200 + 100
    # for i in range(20):
    #     screen.draw.line((x-75+i,y-75+i),(x+75+i,y+75+i),("red"))
    #     screen.draw.line((x+75-i,y-75+i),(x-75+i,y+75+i),("red"))
    # closeness = 100
    # for i in range(500):
    #   screen.draw.line((x-75+(i/closeness),y-75-(i/closeness)), (x+75+(i/closeness),y+75-(i/closeness)), ("red"))
    #   screen.draw.line((x+75-(i/closeness),y-75-(i/closeness)), (x-75-(i/closeness),y+75-(i/closeness)), ("red"))
    # screen.draw.line((x-75,y-75),(x+75,y+75),("red"))
    # screen.draw.line((x+75,y-75),(x-75,y+75),("red"))
    pygame.draw.line(screen.surface, (255, 0, 0), (x-75, y-75), (x+75, y+75), 10)
    pygame.draw.line(screen.surface, (255, 0, 0), (x+75, y-75), (x-75, y+75), 10)


def draw_o(index):
    x,y = index
    x = x * 200 + 100
    y = y * 200 + 100
    screen.draw.filled_circle((x,y), 75, ("blue"))
    screen.draw.filled_circle((x,y), 70, ("white"))



def display_board(board):
  for i in range(len(board)):
      for j in range (len(board[0])):
          if board[i][j] == 1:
                draw_x((j,i))
          elif board[i][j] == 2:
                draw_o((j,i))

          else:
              pass

def make_possibilities(board,player):
  possibility_list = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        new_board = copy.deepcopy(board)
        new_board[i][j] = player
        possibility_list.append(new_board)
  return possibility_list

# def evaluate_board_old(board, player):
#   if check_if_win(board,player) is 1:
#     return 1
#   else:
#     if player == 1:
#       if check_if_win(board,2) is 1:
#         return 0
#     else:
#       if check_if_win(board,1) is 1:
#         return 0

def is_draw(board):
  for i in board:
    if 0 in i:
      return False
  return True


def opposite(player):
  if player == 1:
    return 2
  elif player == 2:
    return 1
  else:
    raise Exception("Oops!")

def evaluate_board(board, player):
  if check_if_win(board, 1) == 1:
    return 1
  elif check_if_win(board,2) == 1:
    return 0
  elif is_draw(board):
    return 0.5

#   possibilities = make_possibilities(board, player)

#   possibility_list = []
  evaluated_possibilities = []

  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        board[i][j] = player
        evaluated_possibilities.append(evaluate_board(board,opposite(player)))
        board[i][j] = 0
  if player == 1:
    best = max(evaluated_possibilities)
    return best
  else:
    worst = min(evaluated_possibilities)
    return worst


def find_best_move(board):
  player = 1
  possibilities = make_possibilities(board, player)
  evaluated_possibilities = []
  for i in possibilities:
    evaluated_possibilities.append(evaluate_board(i, opposite(player)))
  choose_move = possibilities[evaluated_possibilities.index(max(evaluated_possibilities))]
  return choose_move

# def recurrance(board, player):
#   next_moves = make_possibilities(board, player)
#   output_list = []
#   for i in next_moves:
#     if player == 1:
#       output_list.append(recurrance(i,2))
#     else:
#       output_list.append(recurrance(i,2))
#   return output_list


# all_possibilities = recurrance(board,1)
# print(all_possibilities)

# print(evaluate_board(board,2))
# position = None
# def on_mouse_down(pos):
#   global position
#   position = pos
  


print('before draw')

def draw():
    global board, stop, status
    screen.clear()
    screen.fill("white")
    screen.draw.line((200,0),(200,600),("black"))
    screen.draw.line((400,0),(400,600),("black"))
    screen.draw.line((0,200),(600,200),("black"))
    screen.draw.line((0,400),(600,400),("black"))
    display_board(board)
    if stop:
        if status == "x":
            screen.draw.text("Player X wins!", (200, 300), color="red", fontsize=50)
        elif status == "o":
            screen.draw.text("Player O wins!", (200, 300), color="blue", fontsize=50)
        elif status == "draw":
            screen.draw.text("It's a draw!", (200, 300), color="black", fontsize=50)
        return

print('after draw')
# pgzrun.go()

# start = 2

turn = 2 # 1 for x, 2 for o
stop = False
def on_mouse_down(pos):
  global turn, o_row, o_column, board, status, stop
  if stop:
    return
  if turn == 2:
    o_row = pos[1] // 200
    o_column = pos[0] // 200
    if board[int(o_row)][int(o_column)] == 0:
        board[int(o_row)][int(o_column)] = 2
    else:
        # print("please enter a spot that is free! you can try again")
        return

    
    
    
    
    if check_if_win(board,2):
        # print("player o has won!!!")
        status = "o"
        stop = True
        return
    elif is_draw(board):
        # print("Draw!")
        status = "draw"
        stop = True
        return
    status = "nothing"

    turn = 1
    board, status = play_x(board)
    turn = 2
    if status == "x":
        # print("player x has won!!!")
        stop = True
        return
    elif status == "draw":
        # print("Draw!")
        stop = True
        return

# def play_o(board):
#     global position, status, o_row, o_column
#     print("it is your turn, player o!")
#     # o_row = input("Enter the row number of where you want to place your o (1-3): ")
#     # o_column = input("Enter the column number of where you want to place your o (1-3): ")
    
    
  
  



def play_x(board):
    # print("it is your turn, player x!")
    board = find_best_move(board)
    # display_board(board)
    if check_if_win(board,1):
      # print("player x has won!!!")
      return board, "x"
    elif is_draw(board):
      # print("Draw!")
      return board, "draw"

    return board, "nothing"

# def update():
#     global board, turn, stop, status
#     if stop:
#         return

#     if turn == 2:
#         pass
#         # board, status = play_o(board)
#         # if status == "o":
#         #     stop = True
#         #     return
#         # elif status == "draw":
#         #     stop = True
#         #     return
#     turn = 1
#     board, status = play_x(board)
#     if status == "x":
#         stop = True
#         return
#     elif status == "draw":
#         stop = True
#         return
print('done')
#     turn = 2
if __name__ == 'main':
  pgzrun.go()
