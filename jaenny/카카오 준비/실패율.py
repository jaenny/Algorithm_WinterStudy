def solution(N, stages):
    failrate = [[0,0] for _ in range(N)] # 실패율 저장

    for n in range(1,N+1) :
      total = 0
      fail = 0
      for stage in stages :
        if stage >= n :
          total += 1
          if stage == n :
            fail += 1
      
      rate = fail/total if total > 0 else 0
      failrate[n-1] = [n, rate]
    
    failrate.sort(key = lambda x : (-x[1],x[0]))



    return [x[0] for x in failrate]

print(solution(7, [2, 1, 2, 6, 2, 4, 3, 3]	))