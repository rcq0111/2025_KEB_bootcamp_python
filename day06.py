def is_even(n) -> bool :
    """
    짝수 판정 함수
    :param n: 판정할 정수
    :return: 짝수면 True, 홀수면 False
    """
    return not n & 1
    # if n % 2 == 0 :
    #     return True
    # return  False

n = int(input())
print(is_even(n))

# print(not 1) # False
# print(not 0) # True

# a = 10 # 0000 1010
# b = 11 # 0000 1011 & -> 0000 1010
# # bit operation
# print(a & b)
# print(a | b) # | -> 0000 1011
# print(a ^ b) # ^ -> 0000 0001 exclusiveOr
