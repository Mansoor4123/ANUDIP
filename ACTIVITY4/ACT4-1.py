#1: Write a program that takes a person's age and prints the ticket price:

age = int(input("Enter age: "))

if age < 5:
    print("THE TICKET IS FREE")
elif 5 <= age <= 18:
    print("THE TICKET IS 100")
elif 19 <= age <= 60:
    print("THE TICKET IS 200")
elif age > 60:
    print("THE TICKET IS 150")
else:
    print("ENTER THE VALID AGE:")
