# O(1)
def sum(n):
    return n * (n + 1) // 2

print("숫자를 입력하시오 : ", end='')
n = int(input())
print(sum(n))
