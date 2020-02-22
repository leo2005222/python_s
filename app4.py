# 텍스트 상자 만들기
# app4.py

import tkinter as tk

def dispLabel():
    lbl.configure(text="hello, %s" % name.get())


root = tk.Tk()
root.geometry("200x100")

name = tk.StringVar()
lbl = tk.Label(text="")
txt = tk.Entry(textvariable=name)
btn = tk.Button(text="PUSH", command=dispLabel)

txt.pack()
lbl.pack()
btn.pack()
tk.mainloop()
