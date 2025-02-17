def print_poly(f_x, t_x) -> str:
    poly_expression = "f(x) = "

    for i in range(len(fx)):
        coefficient = f_x[i]
        term = t_x[i]
        if coefficient >= 0 & i != 0:
            poly_expression = poly_expression + "+"
        poly_expression = poly_expression + f'{coefficient}x^{term} '

    return poly_expression


def calculation_poly(x_value, f_x, t_x) -> int:
    return_value = 0

    for i in range(len(fx)):
        coefficient = f_x[i]
        term = t_x[i]
        return_value += coefficient * pow(x_value, term)

    return return_value


#fx = [2, 3, 4, 0, -9]
fx = [-2, 5, -9, 11]
tx = [20, 7 , 2, 0]

# if __name__ == "__main__":
#     print(print_poly(fx,tx))
#     print(calculation_poly(int(input("x 값 : ")), fx, tx))

memo = dict()
# 재귀의 장점 : 간결함
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
        return fibonacci_recursion(n - 2) + fibonacci_recursion(n - 1) # 재귀 함수에서는 side effect가 발생할 확률이 0이다

def fibonacci_recursion_dp(n) -> int:
    """
    딕셔너리에 이미 계산된 값이 있으면 그 값을 리턴
    :param n:
    :return: 0, 1이 오면 그 값을 바로 리턴
    """
    if n in memo:
        return memo[n]
    elif n <= 1: # 0이나 1이오면 바로 그값을 리턴
        return n
    else:
        memo[n] = fibonacci_recursion_dp(n - 2) + fibonacci_recursion_dp(n - 1) # 딕셔너리에 계산된 값이 없을 경우 딕셔너리에 추가
        return memo[n]

def fibonacci_loop(n) -> int:
    """
    피보나치 수 계산함수 (반복문 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    n_list = [0, 1]
    for i in range(n + 1):
        n_list.append(n_list[i] + n_list[i + 1])

    return n_list[n]


n = int(input())
print(fibonacci_loop(n))
print(fibonacci_recursion(n))
print(fibonacci_recursion_dp(n))