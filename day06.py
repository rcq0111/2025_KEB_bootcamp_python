def sum(n):
    # if  n == 0:
    #     return 0
    # else:
    #     return sum(n - 1) + n
    temp = 0
    for i in range(n+1):
        temp = temp + i
    return temp

print("숫자를 입력하시오 : ", end='')
n = int(input())
print(sum(n))
