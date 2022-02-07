def solution(numbers):
    answer = ''

    numbers_srt = list(map(str,numbers))

    for i in range(len(numbers_srt)) :
      numbers_srt[i] = numbers_srt[i]*3
    
    numbers_srt.sort(reverse=True)

    for i in range(len(numbers_srt)) :
      end = len(numbers_srt[i])//3
      numbers_srt[i] = numbers_srt[i][:end]

    return str(int(''.join(numbers_srt)))

print(solution([0, 0, 0]))