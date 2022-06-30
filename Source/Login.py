from tkinter import *


def btn_clicked():
      if(entry0.get())=="012" and (entry1.get())=="ad":
          window.destroy()
          import Menu
      else:
          import win32api
          win32api.MessageBox(0, 'You are not allowed', 'Warning')




def btn_clicked2():
      window.destroy()
      import Home
          
window = Tk()
window.title('')
window.iconbitmap(default='dk.ico')
lab = Label(window, text='Window with transparent icon.')
lab.pack()
window.geometry("857x525")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 525,
    width = 857,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background1.png")
background = canvas.create_image(
    427.5, 257.0,

    image=background_img)

entry0_img = PhotoImage(file = f"textBox0.png")
entry0_bg = canvas.create_image(
    656.0, 194.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    show="*",
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 516.0, y = 182,
    width = 276.0,
    height = 27)

entry1_img = PhotoImage(file = f"textBox0.png")
entry1_bg = canvas.create_image(
    710.0, 292.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 516.0, y = 278,
    width = 276.0,
    height = 27)

img0 = PhotoImage(file = f"img00.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 544, y = 353,
    width = 250,
    height = 31)
entry1_img = PhotoImage(file = f"textBox1.png")
entry1_bg = canvas.create_image(
    656.0, 292.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 516.0, y = 278,
    width = 276.0,
    height = 27)

img1 = PhotoImage(file = f"img01.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b1.place(
    x = 528, y = 406,
    width = 282,
    height = 31)


window.resizable(False, False)
window.mainloop()
