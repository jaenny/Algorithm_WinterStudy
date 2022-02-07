def solution(numbers):
    answer = ''

    numbers_srt = list(map(str,numbers))

    for i in range(len(numbers_srt)) :
      # 1000까지 숫자가 올 수 있으니 각 문자열을 3번 연결후 비교
      numbers_srt[i] = numbers_srt[i]*3
    
    numbers_srt.sort(reverse=True)

    for i in range(len(numbers_srt)) :
      end = len(numbers_srt[i])//3
      numbers_srt[i] = numbers_srt[i][:end]

    # [0,0,0,0] => '0' 을 return 하기 위해 int로 바꾸고 다시 str로 바꿈
    return str(int(''.join(numbers_srt)))

print(solution([2,231,23,20]))