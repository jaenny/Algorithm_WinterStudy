def solution(phone_book):
    answer = True
    
    nums = dict()
    phone_book = sorted(phone_book, key = lambda x : len(x))

    print(phone_book)

    
    return answer

print(solution(["12","123","1235","567","88"]))