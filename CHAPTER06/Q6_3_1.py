class Nigiri:
    category = "にぎり"
    top = "ねた"
    base = "シャリ"

    def show_attributes(self):
        print(
            "top: {}, base: {}, category: {}".format(self.top, self.base, self.category)
        )


class Katuo(Nigiri):
    top = "かつお"
    topping = "生姜ネギ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("topping: {}".format(self.topping))

        k1 = Katuo()
        k1.show_attributes()
