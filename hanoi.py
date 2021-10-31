def move(no : int,x : int,y : int) -> None:
    if no > 1:
        move(no -1, x, 6 - x - y)
    print(f'move disc{no} {x} to {y}')
    if no >1 :
        move(no - 1, 6 - x - y, y)

print('hanoi tower')
n = int(input('input the number of disc : '))
move(n,1,3)