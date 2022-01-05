def solution(n, lost, reserve):
  setReserve = set(reserve) - set(lost)
  setLost = set(lost) - set(reserve) # 도난당했는데 여분이 있는 사람들 빼줌

  for i in setReserve :
    if i-1 in setLost :
      setLost.remove(i-1)
    elif i+1 in setLost :
      setLost.remove(i+1)
  return n-len(setLost)

