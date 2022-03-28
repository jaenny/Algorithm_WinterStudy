n = int(input())
m = int(input())
s = input()

target = ['I' if x%2==0 else 'O' for x in range(2*n+1) ]
target = ''.join(target)

answer = 0

for i in range(len(s)-(2*n+1)) :
  if s[i:i+2*n+1] == target :
    answer += 1
print(answer)