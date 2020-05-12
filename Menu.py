class Dish:
    def __init__(self, dish):
        self.num = dish[0]
        self.name = dish[1]
        self.price = dish[2]
        self.description = dish[3]
        self.url_pic = dish[4]
        self.a = 1

    def __str__(self):
        return f'Пицца "{self.name}"\n{self.description}\nЦена: {self.price} рублей\nКол-во в корзине:{self.a}\n'


class Basket:
    def __init__(self, dishes=[]):
        self.dishes_li = dishes

    def sum_up(self):
        summ = 0
        for dish in self.dishes_li:
            summ += dish.price
        return summ

    def inside(self):
        text = ''
        for num, dish in enumerate(self.dishes_li):
            text += str(num + 1) + ')' + str(dish) + '\n'
        text.rstrip()
        return text

    def __str__(self):
        inside = self.inside()
        price = self.sum_up()
        if inside:
            return 'Ваша корзина:\n\n' + inside + '\nИтого: ' + str(price) + ' рублей'
        else:
            return 'Ваша корзина пуста. Наполните ее и возвращайтесь!'

    def append(self, dish):
        if dish.name not in self.names():
            self.dishes_li.append(dish)
        else:
            for elem in self.dishes_li:
                if elem.name == dish.name:
                    elem.a += 1

    def delete(self, i):
        for num, dish in enumerate(self.dishes_li):
            if num + 1 == i:
                del self.dishes_li[i]

    def __len__(self):
        return len(self.dishes_li)

    def names(self):
        text = ''
        for dish in self.dishes_li:
            text += dish.name + ','
        return text

    def reduce(self, i):
        for num, dish in enumerate(self.dishes_li):
            if num + 1 == i:
                if self.dishes_li[i].a > 0:
                    self.dishes_li[i].a -= 1
                elif self.dishes_li[i].a == 0:
                    self.delete(i)
