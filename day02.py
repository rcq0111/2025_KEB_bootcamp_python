n = int(input("input numbers : "))

is_prime = True

if n>= 2:
    for i in range(2, n):
        if n % i == 0:
            #count = count + 1
            is_prime =False
            break
else:
    is_prime = False

#if count == 0:
if is_prime:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")