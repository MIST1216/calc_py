sum = 0
calc_int = 0

while 1:
    com = input("コマンド入力 : add / min / mul / div / equal >> ")
    if com == "add":
        calc_int = input("数値の入力 >> ")
        sum += float(calc_int)
    elif com == "min":
        calc_int = input("数値の入力 >> ")
        sum -= float(calc_int)
    elif com == "mul":
        calc_int = input("数値の入力 >> ")
        sum *= float(calc_int)
    elif com == "div":
        calc_int = input("数値の入力 >> ")
        sum /= float(calc_int)
    elif com == "equal":
        break
    else:
        print("入力した値が違います。")
    print(round(sum, 1))

print(round(sum, 1))
while input():  #キー入力があるまで画面を残す
    break