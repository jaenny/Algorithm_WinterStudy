# 220406
# 이분탐색
def solution(a, b, g, s, w, t):
  start = 0
  # a,b 최대 : 10**9
  # 도시 개수 최대 : 10**5
  # 두 도시에 각각 금과 은만 존재 : 2 도시 모두 방문 필요
  # 왕복 계산 : 2
  end = (10**9)*(10**5)*4
  answer = end

  while start <= end :
    mid = (start + end) // 2
    current_gold = 0
    current_silver = 0
    total = 0

    for i, time in enumerate(t) :
      cnt = mid // (time * 2) # 현재 시간에서 왕복할 수 있는 횟수

      # 편도 추가
      if mid % (time*2) >= time :
        cnt += 1

      if cnt*w[i] > g[i] :
        current_gold += g[i]
      else :
        current_gold += cnt * w[i]
      
      if cnt*w[i] > s[i] :
        current_silver += s[i]
      else :
        current_silver += cnt * w[i]
      
      if s[i] + g[i] < cnt*w[i] :
        total += s[i] + g[i]
      else :
        total += cnt*w[i]
    
    if current_gold >= a and current_silver >= b and total >= a + b :
      end = mid - 1
      answer = min(answer, mid)
    else :
      start = mid + 1
  
  return answer

print(solution(10, 10, [100], [100], [7], [10]))