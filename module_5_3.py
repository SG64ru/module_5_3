
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        #print(new_floor, type(new_floor))
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f"В {self.name} Такого этажа не существует")
        else:
            for i in range(1, new_floor+1):
                print(f"{i}, этаж, {self.name}")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"{self.name}, {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        print(type(self), "self")
        print(type(value), "value")
        return self.number_of_floors + value

    def __radd__(self, value):
        print(isinstance(value, int))
        print(isinstance(value, House))
        return self.number_of_floors + value







h1 = House('ЖК Горский ', 18)
print(type(h1), "h1")
h2 = House('Домик в деревне ', 2)
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
h1.go_to(5)
h2.go_to(10)
print(f"Этажей в {h1.name} {len(h1)} - ВОЗВРАТ ЧЕРЕЗ len")
print(f"Этажей в {h2.name} {len(h2)} - ВОЗВРАТ ЧЕРЕЗ len")

print(str(h1), "- Используем магию STR")
print(str(h2), "- Используем магию STR")
print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 >= h2)
print(h1 != h2)
print(h1 + 10)
print(10 + h2)




