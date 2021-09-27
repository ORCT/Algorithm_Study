import numpy
print('find maximum number of 3 integers')
a = int(input('input integer a : '))
b = int(input('input integer b : '))
c = int(input('input integer c : '))
maximum = a
if b>maximum:maximum=b
if c>maximum:maximum=c
print(f'maximum number is {maximum}.')
#This algorithm is sequential structure.
#The if sentencs is select structure.
print(type(numpy))