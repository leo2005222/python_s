import tkinter as tk

def dispLabel():
    lbl.configure(text="안녕하세요")

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command=dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()
