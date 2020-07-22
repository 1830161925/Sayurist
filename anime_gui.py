import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tkinter as tk
import os
import change_img
from tkinter.filedialog import *
window = tk.Tk()
window.title('动漫人物识别工具')
window.geometry('800x400')
l = tk.Label(window, text='点击第一个按钮开始5秒延时截屏或用第二个按钮读取图片，点击第三个按钮对刚才的图片进行识别', bg='green', font=('Arial', 12), width=80, height=5)
l.pack()   

var = tk.StringVar()   
l = tk.Label(window, textvariable = var, bg='blue', fg='white', font=('Arial', 12), width=30, height=2)
l.pack()
v1 = tk.StringVar()
ent = tk.Entry(window, width=50,textvariable=v1)

def button1():
    os.system("python screemshoot.py")
    var.set('Screenshot complete')
    image1 = mpimg.imread('screenshot.jpg')
    plt.imshow(image1)
    
def button2():
    os.system("python detect.py screenshot.jpg")
    var.set('Success!')
    image2 = mpimg.imread('out.png')
    plt.imshow(image2)
def button3():
    file_open = tk.filedialog.askopenfilename()
    if file_open:
        v1.set(file_open)
    change_img.change(file_open)
    var.set('Select complete')
b = tk.Button(window,text='①截取屏幕',font=('Arial',12),width = 10,height=1,command = button1)

c = tk.Button(window,text='开始识别动漫人物',font=('Arial',12),width = 50,height=1,command = button2)

d = tk.Button(window,text='②读取图片',font=('Arial',12),width = 10,height=1,command = button3)
b.pack()
d.pack()
ent.pack()
j = tk.Label(window, text='切记：使用读取图片功能切记地址不要有中文！否则会失败！', bg='red', font=('Arial', 12), width=80, height=2)
j.pack() 
c.pack()
window.mainloop()
    
