# author wukat
'''
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first 
ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

import itertools

def count_divisors(number):
    div_amount = 2
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            div_amount += 1
            if number != i ** 2:
                div_amount += 1
    return div_amount

def triangle_numbers_generator():
    act = 0
    for i in itertools.count():
        act += i
        yield act

def find_first_triangle_with_at_least_n_divisors(amount_of_divisors):
    for triangle in triangle_numbers_generator():
        if count_divisors(triangle) >= amount_of_divisors:
            return triangle

if __name__ == "__main__":
    print(find_first_triangle_with_at_least_n_divisors(500))
    