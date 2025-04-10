#Write a program to print a pyramid pattern using stars (*).
def print_pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

n = int(input("Enter the number of rows for the pyramid: "))
print_pyramid(n)
