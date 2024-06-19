names = ['John', 'Bob', 'Mosh', 'Sarah', 'Marie']
print(names[2:])
print(names)

# Write a program to find the largest number in a list
numbers = [2, 5, 6, 7, 7, 8, 89, 9, 45]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)