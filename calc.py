import tkinter as tk

def btn_click():
    # 入力した値を取得
    num_left = num_left*10
    # 入力した値をラベルに出力
    sum = num_left

baseGround = tk.Tk()
# メインウィンドウを作成
 
baseGround.geometry('396x467')
# ウィンドウのサイズを設定

baseGround.title('簡易電卓')
# ウィンドウのタイトルを設定

sum = 0
num_left = 0
num_right = 0

labelsum = tk.Label(text=sum, foreground='black', background='white', font=("MSゴシック", "40"))

labelsum.grid(row=0, columnspan=4, sticky = tk.EW, ipady=30)

button7 = tk.Button(baseGround, text = '7', font=("MSゴシック", "20")).grid(row=1, column=0, ipadx=32, ipady=20)
 
button8 = tk.Button(baseGround, text = '8', font=("MSゴシック", "20")).grid(row=1, column=1, ipadx=32, ipady=20)
 
button9 = tk.Button(baseGround, text = '9', font=("MSゴシック", "20")).grid(row=1, column=2, ipadx=32, ipady=20)

buttonP = tk.Button(baseGround, text = '+', font=("MSゴシック", "20")).grid(row=1, column=3, ipadx=32, ipady=20)
 
button4 = tk.Button(baseGround, text = '4', font=("MSゴシック", "20")).grid(row=2, column=0, ipadx=32, ipady=20)
 
button5 = tk.Button(baseGround, text = '5', font=("MSゴシック", "20")).grid(row=2, column=1, ipadx=32, ipady=20)
 
button6 = tk.Button(baseGround, text = '6', font=("MSゴシック", "20")).grid(row=2, column=2, ipadx=32, ipady=20)

buttonMi = tk.Button(baseGround, text = '-', font=("MSゴシック", "20")).grid(row=2, column=3, ipadx=32, ipady=20)
 
button1 = tk.Button(baseGround, text = '1', font=("MSゴシック", "20")).grid(row=3, column=0, ipadx=32, ipady=20)
 
button2 = tk.Button(baseGround, text = '2', font=("MSゴシック", "20")).grid(row=3, column=1, ipadx=32, ipady=20)
 
button3 = tk.Button(baseGround, text = '3', font=("MSゴシック", "20")).grid(row=3, column=2, ipadx=32, ipady=20)

buttonMu = tk.Button(baseGround, text = 'X', font=("MSゴシック", "20")).grid(row=3, column=3, ipadx=31, ipady=20)

buttonMo = tk.Button(baseGround, text = '%', font=("MSゴシック", "20")).grid(row=4, column=0, ipadx=32, ipady=20)
 
button0 = tk.Button(baseGround, text = '0', font=("MSゴシック", "20")).grid(row=4, column=1, ipadx=32, ipady=20)
 
buttonD = tk.Button(baseGround, text = '÷', font=("MSゴシック", "20")).grid(row=4, column=2, ipadx=25, ipady=20)

buttonE = tk.Button(baseGround, text = '=', font=("MSゴシック", "20")).grid(row=4, column=3, ipadx=32, ipady=20)

baseGround.mainloop()

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