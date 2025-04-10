#Write a Python program to find the sum of digits of a number using a while loop.

num = [1, 2, 3, 4]
sum_of_digits = 0
for n in num:
    while n > 0:
        digit = n % 10  
        sum_of_digits += digit  
        n //= 10 

print(f"The sum of digits is: {sum_of_digits}")
