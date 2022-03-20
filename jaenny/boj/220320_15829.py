L = int(input())
string = input()

alpha = dict()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26) :
  alpha[alphabet[i]] = i+1
res = 0
r = 31

for j in range(L) :
  # print(alpha[string[j]]*(r**j))
  res += alpha[string[j]]*(r**j)

print(res%1234567891)