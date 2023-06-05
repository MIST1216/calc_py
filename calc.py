sum = 0

while 1:
    com = input("コマンド入力 : add / min / mul / div / equal >> ")
    calc_num = input("数値の入力 >> ")
    if com == "equal":
        break
    if calc_num.isdigit()==False:
        print("入力値が数値ではありません")
        continue
    if com == "add":
        sum += float(calc_num)
    elif com == "min":
        sum -= float(calc_num)
    elif com == "mul":
        sum *= float(calc_num)
    elif com == "div":
        sum /= float(calc_num)
    else:
        print("入力した値が違います。")
    print(round(sum, 1))

print(round(sum, 1))
while input():  #キー入力があるまで画面を残す
    break
