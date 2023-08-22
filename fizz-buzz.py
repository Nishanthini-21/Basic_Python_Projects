'''
Question: Write a program that prints the numbers from 1 to 100.
But for multiples of 3, print "Fizz" instead of the number, and for the multiples of 5, print "Buzz" instead. 
For numbers that are multiples of both 3 and 5, print "FizzBuzz".
'''
#solution
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
