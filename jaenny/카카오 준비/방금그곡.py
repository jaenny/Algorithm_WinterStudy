import datetime

def replaceM(melody) :
  melody = melody.replace('C#','c')
  melody = melody.replace('D#','d')
  melody = melody.replace('F#','f')
  melody = melody.replace('G#','g')
  melody = melody.replace('A#','a')
  return melody

def solution(m, musicinfos):
  answer = []
  m = replaceM(m)
  for j in range(len(musicinfos)) :
    music = musicinfos[j]
    start, end, title, melody = music.split(',')

    sHour,sMinute = start.split(':')
    eHour,eMinute = end.split(':')

    time_1 = datetime.timedelta(hours= int(sHour), minutes=int(sMinute))
    time_2 = datetime.timedelta(hours= int(eHour), minutes=int(eMinute))
    
    hour, minute = str(time_2 - time_1)[:-3].split(':')
    minute = int(minute)
    if int(hour) != 0 : minute = minute + int(hour)*60

    # print(minute)

    melody = replaceM(melody)

    totalMelody = ''
    if len(melody) < minute : 
      totalMelody = melody*(minute // len(melody)) + melody[:minute % len(melody)]
    else :
      totalMelody = melody[:minute]
    # print(totalMelody)
    
    if m in totalMelody :
      answer.append([minute, j, title])
  if len(answer) > 0 :
    answer.sort(key=lambda x : (-x[0],x[1],x[2]))
  else : return "(None)"
  return answer[0][2]

print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))