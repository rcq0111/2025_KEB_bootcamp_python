# O(1)
def sum(n):
    return n * (n + 1) // 2

print("숫자를 입력하시오 : ", end='')
n = int(input())
print(sum(n))

# f(n) = x^3 + 1_000_000_000 O표기법이 항상 적용 되는 것은 아니다.
