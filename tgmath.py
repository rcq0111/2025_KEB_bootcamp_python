def my_abs(n) -> int:
    """
    Return Absolute value of parameter n
    :param n:
    :return: absolute value
    """
    if n < 0:
        return -n
    return n

print(my_abs(-99), my_abs(-909), my_abs(0))