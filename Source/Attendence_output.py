from tkinter import *


def btn_clicked():
    window.destroy()
    import Attendence_input


def reader1():
    import ast
    f = open("Attendence.txt", "r")
    string=str(f.read())
    attendence = ast.literal_eval(string)
    change=str((attendence[entry0.get()]))
    disallowed_characters = "()'"

    for character in disallowed_characters:
          change = change.replace(character, "")
          change = change.replace(",", "\n")
          

    ser_name = Label(window, 
                  text = " "+change,font=('Helvatical bold',7)).place(x = 102,
                                           y = 233) 

def reader():
    if len(entry0.get())<12:
        reader1()
        print("done")
    else:
            import ast
            f = open("Attendence.txt", "r")
            string=str(f.read())
            ol=(entry0.get())
            dl=ol[:10]
            print(dl)
            attendence = ast.literal_eval(string)
            change=str((attendence[dl]))
            op=((entry0.get()[11:]))
            index = change.find(op)
            ind=(index+len(entry0.get())+2)
            print(ind)
            impo=(change[index:ind])
            print(impo)
                  

            ser_name = Label(window, 
                  text = " "+impo,font=('Helvatical bold',15)).place(x = 700,
                                           y = 252) 

window = Tk()

window.geometry("950x633")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 633,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background222.png")
background = canvas.create_image(
    481.0, 61.5,
    image=background_img)

img0 = PhotoImage(file = f"img0222.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 883, y = 10,
    width = 55,
    height = 52)

img1 = PhotoImage(file = f"img1222.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = reader,
    relief = "flat")

b1.place(
    x = 767, y = 163,
    width = 171,
    height = 35)

entry0_img = PhotoImage(file = f"img_textBox0222.png")
entry0_bg = canvas.create_image(
    129.5, 183.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 45.5, y = 169,
    width = 168.0,
    height = 27)
scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill = Y )


window.resizable(True, True)
window.mainloop()
