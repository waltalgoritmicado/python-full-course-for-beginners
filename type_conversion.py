birth_year = input('Birth year: ')
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)

# Ask user their weight (in pounds), convert it to kilograms and print on the terminal
weight_in_pounds = input('What your weight (in pounds)? ')
weight_in_km = int(weight_in_pounds) * 0.453592
print(f'{weight_in_pounds} in pounds equivalent {weight_in_km} kilograms')
