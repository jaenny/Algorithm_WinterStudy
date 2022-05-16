from collections import defaultdict
import math
def solution(fees, records):
  answer = []
  basicTime, basicFee, unitTime, unitFee = fees

  dic = defaultdict(list)

  for record in records :
    time, number, inout = record.split()
    dic[number].append(time)
  
  for num in dic.keys() :
    totalFee = 0
    totalTime = 0
    for i in range(0,len(dic[num]),2) :
      start = dic[num][i].split(':')
      end = ('23:59' if i == len(dic[num])-1 else dic[num][i+1]).split(':')

      start = int(start[0])*60 + int(start[1])
      end = int(end[0])*60 + int(end[1])
      time = end - start
      totalTime += time

    if totalTime <= basicTime :
      answer.append([num, basicFee])
    else :
      totalFee += basicFee
      totalFee += math.ceil((totalTime-basicTime)/unitTime)*unitFee
      answer.append([num,totalFee])

  answer.sort()
  answer = [y for x, y in answer]
  return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))