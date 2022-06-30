from tkinter import *
import webbrowser



def time():
    window.destroy()
    import Admin_time
def qr():
    window.destroy()
    import Attendence_input
def feedback():
    url = 'https://docs.google.com/forms/d/1wuVrw_OVeCD5DOcfGk3OpigfrfjETZ0slc5q91Js4DI/viewanalytics'
# Open URL in a new tab, if a browser window is already open.
    webbrowser.open_new_tab(url)


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
