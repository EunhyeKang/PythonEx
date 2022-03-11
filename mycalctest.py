from tkinter import *

btn = Tk() # 창생성
btn.title("my calc") # 타이틀
btn.geometry("500x500") # 창크
btn.resizable(False,False) #창크기조절 불가능하게 설정




def print_text():
    print("button으로출력")

button = Button(btn, text="출력",command=print_text)
button.pack()
btn.mainloop() #창유지
