import tkinter as tk

# BMI 결과 출력 함수
def disp_label():
    h = int(txt_height.get())/100
    BMI = int(txt_weight.get())/h**2
    if BMI < 18.5:
        lbl.configure(text="저체중")
    elif 18.5 <= BMI < 23:
        lbl.configure(text="정상")
    elif 23 <= BMI < 25:
        lbl.configure(text="과체중")
    elif 25 <= BMI < 30:
        lbl.configure(text="비만")
    else:
        lbl.configure(text="고도비만")
    lbl_bmi.configure(text="당신의 BMI는 %.2f입니다."% BMI)


root = tk.Tk()
root.geometry("200x100")

height = tk.StringVar()
weight = tk.StringVar()

txt_height = tk.Entry(textvariable=height)
txt_weight = tk.Entry(textvariable=weight)
btn = tk.Button(text="측정", command=disp_label)
lbl = tk.Label(text="")
lbl_bmi = tk.Label(text="")

txt_height.pack()
txt_weight.pack()
btn.pack()
lbl.pack()
lbl_bmi.pack()
tk.mainloop()
