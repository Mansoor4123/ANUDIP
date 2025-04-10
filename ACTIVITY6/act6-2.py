#Write a program to count the even and odd numbers in a list.
def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return even_count, odd_count

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
even_count, odd_count = count_even_odd(numbers)

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
