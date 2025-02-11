def my_pow(b, e):
    """
    밑과 지수를  입력 받아 거듭제곱을 한 결과를 실수 형태로 리턴 받는다.
    :param b:
    :param e:
    :return:
    """
    return b**e




# prime number

numbers = input("Input first second number : ").split(',')
n1 = int(numbers[0])
n2 = int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1
while n1 <= n2:
    is_prime = True

    if n1 < 2:
        pass
    else:
        i = 2
        while i < int(my_pow(n1,0.5)+1):
            if n1 % i == 0:
                is_prime = False
                break
            i = i +1
        if is_prime: print(n1, end=' ')
    n1 = n1 + 1





