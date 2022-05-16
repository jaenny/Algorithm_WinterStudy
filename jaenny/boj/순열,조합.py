input_list = [1,2,3,4,5]
used = [0]*len(input_list)
permutation = []

def perm(arr, r):
    if r == 0:
        permutation.append(arr)
        print(arr)
        return
    for i in range(len(input_list)):
        if not used[i]:
            used[i] = 1
            arr.append(input_list[i])
            perm(arr, r-1)
            arr.pop()
            used[i] = 0

perm([], 2) # perm(arr, r) r개 뽑기

used = [0]*len(input_list)
combination = []
def comb(arr, r) :
  if r == 0 :
    combination.append(arr)
    print(arr)
    return
  
  j = 0 if len(arr) == 0 else input_list.index(arr[-1])

  for i in range(j, len(input_list)) :
    if not used[i] :
      used[i] = 1
      arr.append(input_list[i])
      comb(arr, r-1)
      arr.pop()
      used[i] = 0

comb([],2) # comb(arr, r) r개 뽑기