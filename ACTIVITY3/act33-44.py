#4.Write a Python program to create a list of squares of all even numbers from 1 to 20 using list comprehension, and then calculate the sum of all those squares.

even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
sum_of_squares = sum(even_squares)
print(f"The list of squares of even numbers from 1 to 20: {even_squares}")
print(f"The sum of all those squares is: {sum_of_squares}")
