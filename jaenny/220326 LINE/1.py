def solution(logs):
  answer = 0

  for log in logs :
    # print(log)
    if len(log) > 100 : # 로그 길이는 100 이하
      # print(6)
      answer += 1
      continue
    
    if 'team_name' in log :
      log = log.split('team_name')
      if log[0] == '' :
        log = log[1]
        if 'application_name' in log :
          log = log.split('application_name')
          log0 = log[0].split(' : ')
          if log0[0] == '' and log0[1][:-1].isalpha() :
            log = log[1]
            if 'error_level' in log :
              log = log.split('error_level')
              log0 = log[0].split(' : ')
              if log0[0] == '' and log0[1][:-1].isalpha() :
                log = log[1]
                if 'message' in log :
                  log = log.split('message')
                  log0 = log[0].split(' : ')
                  log1 = log[1].split(' : ')
                  if not (log0[0] == '' and log0[1][:-1].isalpha() and log1[0] == '' and log1[1].isalpha()) :
                    # print(1)
                    answer += 1
                else :
                  # print('message 누락')
                  answer += 1
              else :
                # print(2)
                answer += 1
            else :
              # print('error_level 누락')
              answer += 1
          else :
            # print(3)
            answer += 1
        else :
          # print('application_level 누락')
          answer += 1
      else : # 처음에 공백이 있는 경우
        # print(4)
        answer += 1
    else :
      # print(5)
      answer += 1

  return answer

# print(solution(["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]))
# print(solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))