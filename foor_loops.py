for item in 'Python'.upper():
    print(item)
for item_list in ['Walt', 'Python', 1, 2, 3, 4]:
    print(item_list)

# for item_n in range(10000000000000000000):
#     print(item_n)


prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print("*" * number)

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
