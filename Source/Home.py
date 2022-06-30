from tkinter import *
import webbrowser
import time

def btn_clicked3():
    url = 'https://www.idmedu.lk/branches/batticaloa/'
    webbrowser.open_new(url)

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
def ok():
    if True==True:
        import Home

def btn_clicked1():
    window.destroy()
    import Login
def btn_clicked2():
    try:
      window.destroy()
      import Menu1
    except:
      import win32api
      win32api.MessageBox(0, 'Somthing wrong', 'Error')
      ok()

        
background_img = PhotoImage(file = f"BackgroundS.png")
background = canvas.create_image(
    427.5, 267.5,
    image=background_img)

img0 = PhotoImage(file = f"Buttonf.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b0.place(
    x = 363, y = 358,
    width = 219,
    height = 148)

img1 = PhotoImage(file = f"ButtonA.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b1.place(
    x = 650, y = 365,
    width = 219,
    height = 159)

img2 = PhotoImage(file = f"img5.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked3,
    relief = "flat")

b2.place(
    x = 812, y = 8.59,
    width = 46,
    height = 40)

window.resizable(False, False)
window.mainloop()
