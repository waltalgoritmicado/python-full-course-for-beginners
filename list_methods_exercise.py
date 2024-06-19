# Write a program to remove the duplicates in list

numbers = [1, 3, 4, 55, 6, 67, 7, 13, 7]
uniques = []

for number in numbers:
    if number not in uniques:
      uniques.append(number)
print(uniques)
