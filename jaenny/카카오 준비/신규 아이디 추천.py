def solution(new_id):
    # 규칙에 맞는 아이디인지 판단
    def rightID(id) :
      if len(id) < 3 or len(id) > 15 : return False
      if id[0] == '.' or id[-1] == '.' or '..' in id : return False
      for s in id :
        if s.islower() == False : 
          if s in ['-','_','.'] : continue
          else : return False
      return True

    flag = rightID(new_id)
    print(flag)

    if flag == False :
      # 소문자로 치환
      new_id = new_id.lower()

      # 소문자, 숫자, 빼기, 밑줄, 마침표 제외한 모든 문자 제거
      for s in new_id :
        if s.isalnum() : continue
        if s in ['-','_','.'] : continue
        else : new_id = new_id.replace(s, ' ')
      new_id = new_id.replace(' ', '')

      # 마침표 둘 -> 하나
      while '..' in new_id :
        new_id = new_id.replace('..','.')

      # 맨 앞 or 맨 뒤 마침표 -> 삭제
      if new_id[0] == '.' : 
        if new_id == '.' : new_id = ''
        else : new_id = new_id[1:]
      if len(new_id) > 0 and new_id[-1] == '.' : 
        if new_id == '.' : new_id = ''
        else : new_id = new_id[:len(new_id)-1]

      # 빈 문자열 -> a
      if new_id == '' : new_id = 'a'

      # 길이 16 이상 -> 15까지로 줄이기
      if len(new_id) >= 16 : new_id = new_id[:15]
      # 줄였는데 마지막이 마침표 -> 삭제
      if new_id[-1] == '.' : new_id = new_id[:len(new_id)-1]

      # 길이 2 이하 -> 마지막 문자 붙이기
      if len(new_id) <= 2 : 
        if len(new_id) == 1 : new_id = new_id*3
        else : new_id = new_id + new_id[1]

    return new_id



solution("abcdefghijklmn.p")