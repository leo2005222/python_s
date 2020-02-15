import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk


# 이미지 출력 함수
def disp_img(path):
    # 경로 path의 이미지 불러오기
    newImage = PIL.Image.open(path)

    # 불러온 이미지를 레이블에 출력하기
    imageData = PIL.ImageTk.PhotoImage(newImage)
    lbl_img.configure(image=imageData)
    lbl_img.image = imageData


# 파일 오픈선언
def open_file():
    fpath = fd.askopenfilename()

    if fpath:
        # lbl_img.configure(text=fpath)
        disp_img(fpath)

# 윈도우 창 생성
root = tk.Tk()
root.geometry("400x350")

# 버튼과 레이블 생성
btn = tk.Button(text="파일 열기", command=open_file)
lbl_img = tk.Label()

# 컨트롤(버튼, 레이블) 화면에 배치
btn.pack()
lbl_img.pack()

# 화면유지
tk.mainloop()
