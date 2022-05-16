def solution(num_teams, remote_tasks, office_tasks, employees):
  answer = []

  home = [] # 재택 근무 업무를 가진 사원들

  team = dict()
  for t in range(1,num_teams+1) :
    team[t] = []
  
  homeTeam = set() # 재택 근무하는 직원이 있는 팀
  for i in range(1,len(employees)+1) :
    employee = employees[i-1].split()
    teamNum, tasks = employee[0], employee[1:]
    team[int(teamNum)].append(i)

    all_remote = True
    for task in tasks :
      if task in office_tasks :
        all_remote = False
        continue

    if all_remote :
        home.append(i)
        homeTeam.add(int(teamNum))
  
  for ht in list(homeTeam) :
    check = True # False라면 한 명이라도 출근
    for people in team[ht] :
      if people not in home : check = False
    
    if check :
      home.remove(team[ht][0])
  
  return home

nt = 3
rt = ["development","marketing","hometask"]
ot = ["recruitment","education","officetask"]
e = ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]

print(solution(nt,rt,ot,e))