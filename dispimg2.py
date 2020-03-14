import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk


# 이미지 출력 함수
def disp_img(path):
    newImage = PIL.Image.open(path). resize((200, 200))

    # 불러온 이미지를 레이블에 출력하기
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData
    flabel.configure(text=path)


# 파일 오픈선언
def open_file():
    fpath = fd.askopenfilename()

    if fpath:
        disp_img(fpath)


# 윈도우 창 생성
root = tk.Tk()
root.geometry("400x350")

# 버튼과 레이블 생성
btn = tk.Button(text="파일열기", command=open_file)
imageLabel = tk.Label()
flabel = tk.Label(text="")

btn.pack()
imageLabel.pack()
flabel.pack()

tk.mainloop()
