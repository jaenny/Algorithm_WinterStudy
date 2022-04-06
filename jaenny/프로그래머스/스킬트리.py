from collections import deque
def solution(skill, skill_trees):
  answer = 0

  def check(skill, skill_tree) :
    sk = deque(list(map(str, skill)))
    
    for i in range(len(skill_tree)) :
      target = skill_tree[i]

      if target in sk :
        a = sk.popleft()
        if a == target :
          continue
        else :
          return False
    return True

  for s in skill_trees :
    if check(skill, s) : answer += 1

  return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))