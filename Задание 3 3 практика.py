class Product:
    def __init__(self, nm, pr, st, ct):
        self.nm = nm
        self.pr = pr
        self.st = st
        self.ct = ct
class SCart:
    def __init__(self):
        self.itms = {}
    def ap(self, prd, qty):
        if prd in self.itms:
            self.itms[prd] += qty
        else:
            self.itms[prd] = qty
        print("Добавлено в корзину:" + prd.nm + "(" + str(qty) + "шт)")
    def rp(self, prd):
        if prd in self.itms:
            del self.itms[prd]
            print("Удалено из корзины:" + prd.nm)
        else:
            print("Товара " + prd.nm + " нет в корзине")
    def tp(self):
        ttl = 0
        for prd, qty in self.itms.items():
            ttl += prd.pr * qty
        return ttl
class Customer:
    def __init__(self, nm):
        self.nm = nm
        self.oh = []
    def ao(self, ord):
        self.oh.append(ord)
        print("Заказ добавлен в историю покупателя" + self.nm)
class Order:
    def __init__(self, cst, crt):
        self.cst = cst
        self.prds = crt.itms.copy()
        self.amt = crt.tp()
    def po(self):
        tx = self.amt * 0.1
        fp = self.amt + tx
        print(
            "Заказ оформлен.Сумма без налога:"
            + str(self.amt)
            + ",с налогом: "
            + str(fp)
        )
        self.cst.ao(self)
