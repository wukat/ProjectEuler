""" Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. """

limit = 4000000
fst_tmp = 1
snd_tmp = 1
element = 2
sum_of_even = 0

while element <= limit:
    if element % 2 == 0:
        sum_of_even += element
    fst_tmp = snd_tmp
    snd_tmp = element
    element = fst_tmp + snd_tmp
    
print(sum_of_even)