import random
print("=========================================================")
print("===          ГЕНЕРАТОР СЛОЖНЫХ ПАРОЛЕЙ                ===")
print("=========================================================")
print("Сейчас программа попросит вас ввести данные")
print("Вводить нужно одну строку,в которой будет 5 чисел через пробел")
print("Первое число - это длина пароля")
print("Второе число - включать строчные буквы?(1 - да,0 - нет)")
print("Третье число - включать заглавные буквы?(1 - да,0 - нет)")
print("Четвертое число - включать цифры?(1 - да,0 - нет)")
print("Пятое число - включать спецсимволы?(1 - да,0 - нет)")
print("Пример правильного ввода:12 1 1 1 1")
def random_char(text):
    index = random.randint(0,len(text) - 1)
    return text[index]
while True:
    u_input = input("Введите настройки через пробел:")
    parts = u_input.split()
    if len(parts) != 5:
        print("Ошибка:вы должны ввести ровно 5 чисел через пробел!")
        print("Попробуйте ещё раз")
        continue
    try:
        password_len = int(parts[0])
        u_lower = int(parts[1])
        u_upper = int(parts[2])
        u_numbers = int(parts[3])
        u_symbols = int(parts[4])
    except ValueError:
        print("Ошибка:нужно вводить только целые числа")
        print("Попробуйте ещё раз")
        continue
    if password_len <= 0:
        print("Ошибка:длина пароля должна быть больше нуля")
        print("Попробуйте ещё раз")
        continue
    if u_lower != 0 and u_lower != 1:
        print("Ошибка:второе число должно быть 0 или 1")
        print("Попробуйте ещё раз")
        continue
    if u_upper != 0 and u_upper != 1:
        print("Ошибка:третье число должно быть 0 или 1")
        print("Попробуйте ещё раз")
        continue
    if u_numbers != 0 and u_numbers != 1:
        print("Ошибка:четвёртое число должно быть 0 или 1")
        print("Попробуйте ещё раз")
        continue
    if u_symbols != 0 and u_symbols != 1:
        print("Ошибка:пятое число должно быть 0 или 1")
        print("Попробуйте ещё раз")
        continue
    count = u_lower + u_upper + u_numbers + u_symbols
    if count == 0:
        print("Ошибка вы не выбрали ни одного типа символов (все нули)")
        print("Попробуйте ещё раз")
        continue
    if password_len < count:
        print("Ошибка:длина пароля слишком маленькая")
        print("Для ваших настроек минимальная длина должна быть:",count)
        print("Попробуйте ещё раз")
        continue
    break
low_chars = "abcdefghijklmnopqrstuvwxyz"
up_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num_chars = "0123456789"
sym_chars = "!@#$%^&*"
all_chars = ""
password = ""
if u_lower == 1:
    all_chars = all_chars + low_chars
    password = password + random_char(low_chars)
if u_upper == 1:
    all_chars = all_chars + up_chars
    password = password + random_char(up_chars)
if u_numbers == 1:
    all_chars = all_chars + num_chars
    password = password + random_char(num_chars)
if u_symbols == 1:
    all_chars = all_chars + sym_chars
    password = password + random_char(sym_chars)
while len(password) < password_len:
    password = password + random_char(all_chars)
password_list = []
for char in password:
    password_list.append(char)
for i in range(len(password_list) - 1,0,-1):
    j = random.randint(0, i)
    t = password_list[i]
    password_list[i] = password_list[j]
    password_list[j] = t
f_password = ""
for char in password_list:
    f_password = f_password + char
print("=========================================================")
print("===                  ВАШ ПАРОЛЬ                       ===")
print("=== ",               f_password,"                                    ===")
print("=========================================================")
