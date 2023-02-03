from pathlib import Path
class Product:

    def __int__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


# product = Product()
# product.price = 5
# print(product.price)

path = Path("")
for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("*.py")]
all_py_files_recursively = [p for p in path.rglob("*.py")]
print("")
print(paths)
print("")
print(py_files)
print("")
print(all_py_files_recursively)

