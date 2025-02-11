def is_prime(num):
    """
    소수 여부를 판정해서 소수면 True 소수가아니면 False를 리턴하는 함수.
    :param num: integer number
    :return:  boolean type
    """
    if num >= 2:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
                # count = count + 1
                #is_prime = False
                #break
            #print(i, end=' ')
    else:
        return False
    return True

# main
help(is_prime)
3n = int(input("input numbers : "))

if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")