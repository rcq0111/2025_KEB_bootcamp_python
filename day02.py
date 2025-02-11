n = int(input("input numbers : "))
count = 0
for i in range(1, 1+n):
    if n % i == 0:
        count = count + 1

if count == 2:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")