import random,string
a = random.choices(string.ascii_uppercase,k=3)
b = random.choices(string.digits,k=3)
c = random.choices('!@#$%^&*',k=2)
p = a + b + c
random.shuffle(p)
print('Ваш пароль:',''.join(p))
