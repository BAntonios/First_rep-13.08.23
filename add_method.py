class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    def __add__(self, other):
        if isinstance(other, int):
            return self.price  + other
        elif isinstance(other, Item):
            return self.price + other.price
item_1 = Item('Видеокарта', 15000, 0.8)
item_2 = Item('Клавиатура', 4000, 0.5)
total_price = item_1 + item_2
print(total_price)