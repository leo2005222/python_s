# 숫자 맞추기
import tkinter as tk
import random

q = random.randint(1, 100)
def check_num(a_num):
    global q
    if a_num == q:
        msg = "정답!"
        txt.configure(state='readonly')
    elif a_num > q:
        msg = "DOWN"
    else:
        msg = "UP"
    return msg

def disp_msg():
    a_num = int(num.get())
    msg = check_num(a_num)
    lbl.configure(text=msg)


root = tk.Tk()
root.geometry("300x300")

num = tk.StringVar()
lbl = tk.Label(text="")
txt = tk.Entry(textvariable=num)
btn = tk.Button(text="시도!", command=disp_msg)

lbl.pack()
txt.pack()
btn.pack()

tk.mainloop()