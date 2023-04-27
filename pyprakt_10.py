from random import randint

def ziehung(a=1, b=49, c=6):
    x = []
    y = 0
    while y < c:
        z = randint(a,b)
        if z not in x:
            x.append(z)
            y = y + 1
    return x


if __name__ == '__main__':
    print(__name__)
    print(ziehung())
    print(ziehung(0,1,2))