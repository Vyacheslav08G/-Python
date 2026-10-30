class Kl:
    def gn(self):
        return "Транспортное средство"
class Car(Kl):
    def gn(self):
        return "Это легковой автомобиль"
class Bic(Kl):
    def gn(self):
        return "Это велосипед"
class Air(Kl):
    def gn(self):
        return "Это самолёт"
ss = [Car(),Bic(),Air()]
for v in ss:
    print(v.gn())
