from pathlib import Path

path = Path("ecommerc1e")
print(path.exists())
if path == True:
    print('Good')
else:
    print('Error')


# mkd = Path('emails')
# print(mkd.mkdir())

pyfile = Path()
for file in pyfile.glob('*.py'):
    print(file)
