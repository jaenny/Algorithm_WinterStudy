# 재연 풀이
from itertools import permutations

k = int(input())
signs = input().split()

result = []
for per in permutations([0,1,2,3,4,5,6,7,8,9],k+1) :
  flag = True
  for i in range(len(signs)) :
    if signs[i] == '<' :
      if per[i] < per[i+1] : continue
      else : 
        flag = False
        break
    else :
      if per[i] > per[i+1] : continue
      else : 
        flag = False
        break
  if flag :
    result.append(per)

print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))

# 백준님 풀이
def good(x, y, op) :
  if op == '<' :
    if x > y : return False
  if op == '>' :
    if x < y : return False
  return True

def go(index, num) :
  if index == n+1 : # 부등호가 n개 입력되니까 숫자는 n+1개 필요
    ans.append(num)
    return
  
  for i in range(10) :
    if check[i]: continue # 해당 숫자를 이미 사용했다면 pass

    if index == 0 or good(num[index-1], str(i), a[index-1]):
      check[i] = True
      go(index+1, num+str(i))
      check[i] = False

n = int(input())
a = input().split()

ans = []
check = [False]*10 # 해당 숫자를 사용했는지 안 했는지 체크

go(0, '')

ans.sort()
print(ans[-1])
print(ans[0])