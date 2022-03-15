# 재연 코드 - 시간초과
n = int(input())
a = input()
s = [[1]*n for _ in range(n)]
c = 0
for i in range(n) :
  for j in range(i,n) :
    s[i][j] = a[c]
    c+= 1

def go(index, num):
  if index == n :
    for i in range(n) :
      for j in range(i,n) :
        _sum = sum(num[i:j+1])
        if _sum == 0 and s[i][j] != '0' :
          return 
        if _sum > 0 and s[i][j] != '+' :
          return 
        if _sum < 0 and s[i][j] != '-' :
          return 
    res.append(' '.join(map(str,num))) 
    return
  
  for i in range(-10,11) :
    if check[i] : continue

    check[i] = True
    go(index+1, num+[i])
    check[i] = False

check = [False]*21
res=[]
go(0, [])
print(res[0])

# 백준님 풀이

def check(index) :
  s = 0
  for i in range(index, -1, -1) :
    s += ans[i]
    if sign[i][index] == 0 :
      if s != 0 :
        return False
    elif sign[i][index] < 0 :
      if s >= 0 :
        return False
    elif sign[i][index] > 0 :
      if s <= 0 : 
        return False
  return True


def go(index) :
  if index == n :
    return True
  
  if sign[index][index] == 0 :
    ans[index] = 0
    return check(index) and go(index+1)
  else :
    for i in range(1, 11) :
      ans[index] = i * sign[index][index]
      if check(index) and go(index+1) : return True
    return False

n = int(input())
s = input()

sign = [[0]*n for _ in range(n)]
ans = [0]*n # 정답 숫자들
cnt = 0

# sign 배열 채우기
for i in range(n) :
  for j in range(i,n) :
    if s[cnt] == '0' :
      sign[i][j] = 0
    elif s[cnt] == '+' :
      sign[i][j] = 1
    else :
      sign[i][j] = -1
    cnt += 1

go(0)
print(' '.join(map(str, ans)))