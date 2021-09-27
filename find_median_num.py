def median3(a,b,c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('find median')
a = int(input('input integer a : '))
b = int(input('input integer b : '))
c = int(input('input integer c : '))

print(f'median value is {median3(a,b,c)}')