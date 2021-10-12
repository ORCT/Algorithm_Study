def gcd(x :int, y: int) -> int:
    if y == 0:
        return x
    else:
        return(gcd(y, x % y))

if __name__ == '__main__':
    x = int(input('input integer x : '))
    y = int(input('input integer y : '))
    print(f'the gcd is {gcd(x,y)}')