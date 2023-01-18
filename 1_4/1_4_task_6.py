class Translator:
    DATA = {}

    def add(self, eng, rus):
        if eng in self.DATA:
            if rus not in self.DATA[eng]:
                self.DATA[eng].append(rus)
        else:
            self.DATA[eng] = [rus]

    def remove(self, eng):
        del self.DATA[eng]

    def translate(self, eng):
        return self.DATA[eng]


tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate('go'))
print(tr.DATA)
