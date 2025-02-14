def cl(n):
    for i in range(n, -1, -1):
        if i == 0:
            print("펑~!")
        else:
            print(i)

def cr(n):
    if n < 0:
        return
    elif n == 0 :
        print("펑~!")
    else:
        print(n)
    cr(n-1)



s = int(input())
cl(s)
cr(s)
