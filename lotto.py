import tkinter as tk
import random

def lotto():
    a = list(range(1, 46))
    random.shuffle(a)
    lbl.configure(text= a[:6])

# 200x100 픽셀 창 만들기
root = tk.Tk()
root.geometry("200x100")

# 레이블과 버튼 생성하기
lbl = tk.Label(text="")
btn = tk.Button(text="생성하기", command=lotto)

# 레이블과 버튼 화면에 배치하기
lbl.pack()
btn.pack()
tk.mainloop()
