import tkinter as tk
import random


def disp_label():
    fortune = ['좋음', '보통', '나쁨']
    f = random.choice(fortune)
    lbl.configure(text="%s님 오늘의 운세는 %s입니다." % (lbl_name.get(), f))


root = tk.Tk()
root.geometry("200x100")

name = tk.StringVar()

lbl = tk.Label(text="")
lbl_name = tk.Entry(textvariable=name)
txt = tk.Button(text="BUTTON", command=disp_label)

lbl.pack()
lbl_name.pack()
txt.pack()
tk.mainloop()
