def factorial_recursion(n : int) -> int:
    if n > 0:
        return n * factorial_recursion(n-1)
    else:
        return 1

if __name__ == '__main__':
    n = int(input('input n : '))
    print(f'{n} factorial is {factorial_recursion(n)}')
