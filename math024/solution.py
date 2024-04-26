def factHelper(number):
  if number == 0:
    return 1
  return number*factHelper(number-1)

def solution(perm_list,n):
  ans = ''
  perm_list = sorted(perm_list)

  n -= 1

  while len(perm_list) > 0:
    fact = factHelper(len(perm_list)-1)
    index = n // fact
    ans += str(perm_list.pop(index))
    n %= fact
  return ans

print(solution([0,1,2,3,4,5,7,8,9],1_000_000))