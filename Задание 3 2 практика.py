num = int(input())
def print_pack_report(s_num):
    if s_num <= 1:
        print("Ошибка:число должно быть больше 1")
        return
    while s_num > 0:
        if s_num % 3 == 0 and s_num % 5 == 0:
            print(s_num,"- расфасуем по 3 или по 5")
        elif s_num % 5 == 0 and s_num % 3 != 0:
            print(s_num,"- расфасуем по 5")
        elif s_num % 3 == 0 and s_num % 5 != 0:
            print(s_num,"- расфасуем по 3")
        else:
            print(s_num,"- не заказываем!")
        s_num -= 1
print_pack_report(num)
