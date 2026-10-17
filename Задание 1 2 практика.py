en_low_chars = "abcdefghijklmnopqrstuvwxyz"
en_up_chars  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_low_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
rus_up_chars  = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
def check_l(text):
    for c in text:
        if c in rus_low_chars or c in rus_up_chars:
            return "rus"
        if c in en_low_chars or c in en_up_chars:
            return "eng"
    return "none"
def do_c(text, shift):
    lang = check_l(text)
    if lang == "none":
        return text
    if lang == "rus":
        low_chars = rus_low_chars
        up_chars  = rus_up_chars
    else:
        low_chars = en_low_chars
        up_chars  = en_up_chars
    leng = len(low_chars)
    f_text = ""
    for c in text:
        if c in low_chars:
            f_text += low_chars[(low_chars.find(c) + shift) % leng]
        elif c in up_chars:
            f_text += up_chars[(up_chars.find(c) + shift) % leng]
        else:
            f_text += c
    return f_text
while True:
    u_choice = input("1-Зашифровать, 2-Расшифровать, 0-Выход: ")
    if u_choice == "0":
        break
    elif u_choice in ("1", "2"):
        u_text = input("Текст: ")
        try:
            u_shift = int(input("(сдвиг): "))
        except ValueError:
            print("Ошибка: введите число")
            continue
        if u_choice == "1":
            f_text = do_c(u_text, u_shift)
        else:
            f_text = do_c(u_text, -u_shift)
        print("Результат:", f_text)
    else:
        print("Ошибка: выберите 1, 2 или 0")
