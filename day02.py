#for -> while
#while 문으로 구간 소수를 출력하는 프로그램

number = int(input("Input number : "))
is_prime = True  # int -> bool
i = 2
while i < number:
    if number % i == 0:
        is_prime = False  # remove +
        break
    #print(i, end=' ')
    i = i + 1

if is_prime:  # remove ==
    print(f'{number} is prime number')
else:
    print(f'{number} is NOT prime number!')
#main
# numbers = input("숫자를 두개 입력하시오. : ").split(',')
# n1 = int(numbers[0])
# n2 = int(numbers[1])
#
# if n1 > n2:
#     n1, n2 = n2, n1



