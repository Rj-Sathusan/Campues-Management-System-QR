from tkinter import *
import tkinter as tk
from tkinter import ttk


def btn_clicked():
    ok=str(t.get("1.0",END))
    import requests
    pload = {"entry.1724623701":"NAME: "+entry0.get()+"\n"+"FEEDBACK: "+ok}
    r = requests.post('https://docs.google.com/forms/u/0/d/e/1FAIpQLSe7PEBjUIJq697haT93HY_yh6crHN4JQpbkRxt3bFXxcZ7vNQ/formResponse',data = pload)
    import win32api
    win32api.MessageBox(0, 'Complete ', 'Sucess')
    window.destroy()
    import Menu1

window = tk.Tk()

window.geometry("580x388")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 388,
    width = 580,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background--.png")
background = canvas.create_image(
    296.5, 172.0,
    image=background_img)

img0 = PhotoImage(file = f"img0--.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 450, y = 344,
    width = 122,
    height = 33)

entry0_img = PhotoImage(file = f"img_textBox0--.png")
entry0_bg = canvas.create_image(
    241.5, 357.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 123.0, y = 344,
    width = 237.0,
    height = 24)

ttk.Label(window, text="\n\n\n\n\n",
          font=("Times New Roman", 1)).grid(
column=0, row=5, padx=15, pady=25)
t = tk.Text(window, width=50, height=14)
  
t.grid(column=5, row=15)

window.resizable(False, False)
window.mainloop()
