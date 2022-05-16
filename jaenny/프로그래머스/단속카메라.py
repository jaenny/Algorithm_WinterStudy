def solution(routes):
    answer = 0

    routes = sorted(routes, key = lambda x: x[1])

    camera = -30001

    for start, end in routes :
        if start > camera :
            answer += 1
            camera = end


    return answer

print(solution([[-20,-15], [-5,-3]]))