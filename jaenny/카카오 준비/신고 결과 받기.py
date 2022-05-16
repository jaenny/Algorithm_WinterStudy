def solution(id_list, report, k):
    answer = [0]*len(id_list)

    reportCount = {x : 0 for x in id_list} # 각 유저별로 신고당한 횟수

    reportBoard = dict()

    report = set(report) # 중복 신고는 1회로 처리

    for r in report :
      user, badUser = r.split()
      reportCount[badUser] += 1
    
    for r in report :
      user, badUser = r.split()
      if reportCount[badUser] >= k :
        answer[id_list.index(user)] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

# 한 번에 한 명의 유저 신고, 횟수 제한은 없음. 한 유저를 여러번 신고해도 1회로 처리
# k번 이상 신고된 유저는 게시판 이용이 정지, 신고한 유저에게 정지된 사실 메일로 발송

