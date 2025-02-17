def dec_oct (n):
    """
    10진수를 8진수로 바꾸는 함수
    :param n: 변환될 숫자
    :return: 8진수
    """
    if n == 0 :
        return ""
    else:
        return dec_oct(n // 8) + str(n % 8)

    # return oct(n)


print("숫자를 입력하시오 : ", end='')
n = int(input())
print(dec_oct(n))