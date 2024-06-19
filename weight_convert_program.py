weight = input('weight: ')
unit = input('(L)bs or (K)g: ')

if unit.upper() == "k":
  converted = int(weight) // 0.45
  print(f'You are {converted} pounds')
elif unit.upper() == "l":
  converted= int(weight) * 0.45
  print(f'You are {converted} kilos')
print(f"Final Program!")
