import tkinter as tk
import random as r


def disp_label():
    num = int(txt.get())
    if num == a+b:
        lbl.configure(text="정답")
    else:
        lbl.configure(text="오답")


a = r.randint(1, 100)
b = r.randint(1, 100)

root = tk.Tk()
root.geometry("200x100")

ans = tk.StringVar()

lbl_quize = tk.Label(text="%d + %d=" % (a, b))
txt = tk.Entry(textvariable=ans)
lbl = tk.Label(text="")
btn = tk.Button(text="풀기", command=disp_label)

lbl_quize.pack()
txt.pack()
btn.pack()
lbl.pack()
tk.mainloop()
