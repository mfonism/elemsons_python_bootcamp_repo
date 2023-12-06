"""
1.
Write a program that will take a number and print out the multiplication table column for that number. 
Multipliers in the column should go from 1 to 12.
"""
def mul_table(num):
    x = 1
    while x <= 12:
        print(f'{num} x {x} = {num*x}')
        x += 1

"""
2.
Write a program that takes a number n, and prints out: one 1, two 2's, three 3's... 
and continues the pattern till n.
"""

def repeater(n):
    rep = 1
    for num in range(1,n+1):
        num = str(num)
        print(num*rep)
        rep +=1

"""
3.
Now write a program that takes a number n, and prints out the reverse of 
what the program in number 2 above prints.
"""

def repeater_rev(n):
    rep = n
    for num in range(n,0,-1):
        num = str(num)
        print(num*rep)
        rep -=1
"""
4.
Write a program that takes a number n and returns the sum of all the numbers from 1 to n.
For example, if the program is given the number 6, it should return 21 (which is 1 + 2 + 3 + 4 + 5 + 6).
"""

def sum_of_nos(num):
    res = 0
    for x in range (num+1):
        res += x
    print(res)

"""
5.
Write a program that takes a number and returns its factorial. 
The factorial of a number is the product of all the numbers from 1 to that number.
For example, the factorial of 6 is 720 (which is 1 * 2 * 3 * 4 * 5 * 6).
"""

def fact_of_nos(num):
    v = 1
    fact = 1
    for x in range (1, num+1):
       fact = v * x
       v = fact
    print(fact)  

"""
6.
Write a program that returns the largest number in a list of numbers.
For example, if the program takes the list [1, 4, 6, 2, 3, -9] it should return 6.
Please do not use the `max` function.
"""

def largest(list):
    list.sort()
    return list[-1]

"""
7.
Write a program that returns the smallest number in a list of numbers.
For example, if the program takes the list [13, 7, 12, 11, 6, 8] it should return 6.
Please do not use the `min` function.
"""

def smallest(list):
    list.sort()
    return list[0]

"""
8.
Write a program that returns the length of a list.
For example, if the program takes the list 
["Python", "Haskell", "Smalltalk", "Scheme", "Rust", "Elixir"] it should return 6.
Please do not use the `len` function.
"""

def length(list):
    freq = 0
    for x in list:
        freq += 1
    return freq

"""
9.
Write a program that returns the sum of the numbers in a list of numbers.
For example, if the program takes the list [1, 2, 3] it should return 6.
Please do not use the `sum` function.
"""

def list_sum(list):
    sum = 0
    for x in list:
        sum += x
    return sum

"""
10.
Write a program that checks the validity of a password.
"""  

def validity():
    v = input('Enter Password ')
    if v == 'Assignment_Completed':
        print ('Very Good!')
    else:
        print('Bad Student! Mfon will flog you!')
