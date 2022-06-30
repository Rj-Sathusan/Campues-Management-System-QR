from tkinter import *
import sys



def btn_clicked():
    window.destroy()
    import Menu
    


def qrread():
    import cv2
    import os
    import ast
    from datetime import datetime

    # initalize the cam
    cap = cv2.VideoCapture(0)
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    n=1
    while n==1:
        _, img = cap.read()
        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if data:
            a=data
            break
        # display the result
        cv2.imshow("    IDM qr code scanner", img)    
        if cv2.waitKey(1) == ord("q"):
            break
        n=(n+1)


    now = datetime.now()
    date=(now.strftime("%Y-%m-%d"))
    time=(now.strftime('%H:%M:%S'))

    f = open("Attendence.txt", "r")

    string=str(f.read())

    attendence = ast.literal_eval(string)

    name=str(a)+"     "+time
    if date in attendence:
      attendence[date] = ((attendence[date]),name)
    else:
      attendence[date] = name

    f = open("Attendence.txt", "w")
    f.write(str(attendence))
    f.close()

    print(str(a))
    import win32api
    win32api.MessageBox(0, str(a), 'Saved')
    qrread()

    
def next():
    window.destroy()
    import Attendence_output

window = Tk()

window.geometry("791x423")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 423,
    width = 791,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background111.png")
background = canvas.create_image(
    393.5, 216.5,
    image=background_img)

img0 = PhotoImage(file = f"img011.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command =next,
    relief = "flat")

b0.place(
    x = 545, y = 224,
    width = 212,
    height = 35)

img1 = PhotoImage(file = f"img111.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = qrread,
    relief = "flat")

b1.place(
    x = 8, y = 229,
    width = 259,
    height = 39)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 721, y = 18,
    width = 51,
    height = 31)

window.resizable(False, False)
window.mainloop()
