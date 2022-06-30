from tkinter import *



def time():
    try:
      window.destroy()
      import User_time
    except:
      import win32api
      win32api.MessageBox(0, 'Check your internet conection ', 'Error')
def qr():
    window.destroy()
    import Attendence_input
def feedback():
    window.destroy()
    import Feedback_students
def downloader():
    window.destroy()
    import D_Downloader


window = Tk()
window.title('')
window.geometry("866x434")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 434,
    width = 866,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img-0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = downloader,
    relief = "flat")

b0.place(
    x = 690, y = 152,
    width = 134,
    height = 142)

img1 = PhotoImage(file = f"img-1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = time,
    relief = "flat")

b1.place(
    x = 27, y = 168,
    width = 159,
    height = 126)

img2 = PhotoImage(file = f"img-2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = qr,
    relief = "flat")

b2.place(
    x = 472, y = 159,
    width = 133,
    height = 126)

img3 = PhotoImage(file = f"img-3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = feedback,
    relief = "flat")

b3.place(
    x = 249, y = 168,
    width = 149,
    height = 126)

background_img = PhotoImage(file = f"back.png")
background = canvas.create_image(
    587.5, 241.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
