answer = 0
def divide(x,y,n) :
  global answer
  for i in range(y, y+n) :
    for j in range(x, x+n) :
      if n == 1 and i == r and j == c :
        print(answer)
        exit(0)
      elif n//2 > 0 :
        divide(x, y, n//2)
        divide(x+n//2, y, n//2)
        divide(x, y+n//2, n//2)
        divide(x+n//2, y+n//2, n//2)
        return 
      else :
        answer+=1
        return

n,r,c = map(int,input().split())
if r+c == 0 : print(0)
else :
  divide(0,0,2**n)

# 정답코드
N, r, c = map(int, input().split())

ans = 0

while N != 0:

	N -= 1

	# 1사분면
	if r < 2 ** N and c < 2 ** N:
		ans += ( 2 ** N ) * ( 2 ** N ) * 0

	# 2사분면
	elif r < 2 ** N and c >= 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 1
		c -= ( 2 ** N )
        
	# 3사분면    
	elif r >= 2 ** N and c < 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 2
		r -= ( 2 ** N )
        
	# 4사분면    
	else:
		ans += ( 2 ** N ) * ( 2 ** N ) * 3
		r -= ( 2 ** N )
		c -= ( 2 ** N )
    
print(ans)