def check(place) :
  visit = [[0]*5 for _ in range(5)]
  di = [1,-1,0,0]
  dj = [0,0,1,-1]

  for i in range(5) :
    for j in range(5) :
      if place[i][j] == 'P' :
        visit[i][j] = 1
        for d in range(4) :
          ni = i + di[d]
          nj = j + dj[d]
          if ni < 0 or ni >= 5 or nj < 0 or nj >= 5 : continue
          if place[ni][nj] == 'P' : return 0
          elif place[ni][nj] == 'X' : continue
          else :
            for d in range(4) :
              mi = ni + di[d]
              mj = nj + dj[d]
              if mi < 0 or mi >= 5 or mj < 0 or mj >= 5 : continue
              if [i,j] == [mi,mj] : continue
              if place[mi][mj] == 'P' : return 0
  return 1

def solution(places):
  answer = []
  for place in places :
    answer.append(check(place))
  return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))