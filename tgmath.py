def my_abs(n) -> int:
    """
    Return Absolute value of parameter n
    :param n:
    :return: absolute value
    """
    if n < 0:
        return -n
    return n

#print(my_abs(-99), my_abs(-909), my_abs(0))

def fibonacci_recursion(n) -> int:
    """
    피보나치 수 계산함수 (재귀함수 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)


def fibonacci_loop(n) -> int:
    """
    피보나치 수 계산함수 (반복문 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    n_list=[0 ,1]
    for i in range(n+1):
        n_list.append(n_list[i] + n_list[i + 1])
    return n_list[n]

if __name__ != "__main__": # main 현재 실행시키는 파일
    print("tgmath.py 파일을 실행하셨습니다.")