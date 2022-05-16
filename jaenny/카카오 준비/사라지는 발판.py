
di = [-1,1,0,0]
dj = [0,0,-1,1]

n = 0
m = 0

def isRange(i,j) :
  global n,m
  return 0<=i<n and 0<=j<m

def isFinished(board, i, j) :
  for d in range(4) :
    ni = i + di[d]
    nj = j + dj[d]
    if isRange(ni,nj) and board[ni][nj] : return False
  
  return True
import math
def solve(board, i1, j1, i2, j2) :

  # base case
  if isFinished(board, i1, j1) : return [False, 0]
  if (i1 == i2 and j1 == j2) : return [True, 1]

  canWin = False
  minTurn = math.inf
  maxTurn = 0

  for d in range(4) :
    ni = i1 + di[d]
    nj = j1 + dj[d]
    if (not isRange(ni, nj) or not board[ni][nj]) : continue

    # dfs
    board[i1][j1] = 0
    res = solve(board, i2, j2, ni, nj)
    board[i1][j1] = 1

    if (not res[0]) : 
      canWin = True
      minTurn = min(minTurn, res[1])
    elif not canWin :
      maxTurn = max(maxTurn, res[1])

  turn = minTurn if canWin else maxTurn
  return [canWin, turn + 1]

def solution(board, aloc, bloc) :
  global n, m
  n = len(board)
  m = len(board[0])

  return solve(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]]	, [1,0], [1,2]))