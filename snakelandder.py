board = []
for i in range(10):
    row = input().split()
    if i % 2 == 0:
        board.insert(0, row[::-1])
    else:
        board.insert(0, row)
from itertools import chain
flatten_board = list(chain.from_iterable(board))

moves = list(map(int, input().split()))
cur_pos = -1
snakes = 0
ladders = 0
flag = 0
for move in moves:
    cur_pos += move
    if flatten_board[cur_pos] == "End":
        flag = 1
        print("Possible", snakes, ladders)
        break
    elif flatten_board[cur_pos][0] == "S" and flatten_board[cur_pos] != "Start":
        snakes += 1
        if flatten_board[cur_pos][2:-1] == "Start":
            cur_pos = 0
        else:
            cur_pos = int(flatten_board[cur_pos][2:-1]) - 1
    elif flatten_board[cur_pos][0] == "L":
        ladders += 1
        cur_pos = int(flatten_board[cur_pos][2:-1]) - 1
if flag == 0:
    print("Not possible", snakes, ladders, cur_pos + 1)
