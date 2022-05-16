from collections import deque

def solution(a, edges):
    answer = -1
    
    queue = deque()
    queue.append([a, 0])
    
    while queue :
        dp, cnt = queue.popleft()
        

        if dp == [0]*len(a) : 
            return cnt
        # if len(queue) > 3 : break

        for edge in edges :
            new1 = dp.copy()
            new2 = dp.copy()
            i, j = edge
            new1[i] += 1
            new1[j] -= 1
            queue.append([new1, cnt+1])
            new2[i] -= 1
            new2[j] += 1
            queue.append([new2, cnt+1])
        # print(queue)

    
    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))