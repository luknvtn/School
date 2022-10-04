
import numpy as np




def FindAdj(board,cors, num = 0):
    l = []
    for y in [-1,0,1]:
        for x in [-1,0,1]:
            if cors[0] + y < board.shape[0] and cors[1] + x < board.shape[1] and cors[0] + y >= 0 and cors[1] + x >= 0: 
                if x != y and x != - y and board[cors[0]+y,cors[1]+x] == num:
                    l.append([cors[0]+y,cors[1]+x])
    return l


def Looking(board,cors,iteration):
    if np.where(board == 0)[0].size == 0:
        if FindAdj(board,cors,board.size):
            return board
        else:
            return 1
    for cor in FindAdj(board,cors):
        fboard = np.copy(board)
        fboard[cor[0],cor[1]] = iteration
        found = Looking(fboard,cor,iteration+1)
        if type(found) == np.ndarray:
            return found
    
    return 1

def lookForSnake(board):
    l = []
    for i in range(board.size):
        a = np.where(board == i+1)
        l.append([a[0][0],a[1][0]])
    return l

def main(board_size,head,tail):
    head = [head[1],head[0]]
    tail = [tail[1],tail[0]]
    board = np.zeros(board_size)
    board[tail[0],tail[1]] = board_size[0]*board_size[1]
    board[head[0],head[1]] = 1

    b = Looking(board,head,2)
    print(type(b))
    if type(b) != np.ndarray:
        print("Impossible setup")
        return []
    list = lookForSnake(b)
    out = []
    for item in list:
        out.append([item[1],item[0]])
    #print(b)                                               #Uncomment to see the board
    return out


rozmery = [3,3]
zacatek = [0,2]
konec = [2,2]

print(main(rozmery,zacatek,konec))
