import sys

lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
# lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, date):
        for i in date:
            self.lst_data.append(dict(zip(self.FIELDS, i.split(' '))))

    def select(self, a, b):
        return self.lst_data[a:b + 1]


db = DataBase()
db.insert(lst_in)

