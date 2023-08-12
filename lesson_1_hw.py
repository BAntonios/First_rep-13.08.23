class Item:
    def __init__(self, num):
            self.num = num
    def __add__(self, other):
        return self.num + other.num
    def __sub__(self, other):
        return self.num - other.num
    def __mul__(self, other):
        return self.num * other.num
    def __truediv__(self, other):
        return self.num / other.num
item1 = Item(2)
item2 = Item(2)

summa = item1 + item2
raznost= item1 - item2
proizvedenie = item1 * item2
chastnoe = item1 / item2
print(summa)
print(raznost)
print(proizvedenie)
print(chastnoe)
