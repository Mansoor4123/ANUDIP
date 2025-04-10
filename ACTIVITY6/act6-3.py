#Write a program to calculate the sum of all even numbers in a given range.
def sum_of_even_numbers(start, end):
    return sum(num for num in range(start, end + 1) if num % 2 == 0)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = sum_of_even_numbers(start, end)
print(f"The sum of even numbers in the range is: {result}")
