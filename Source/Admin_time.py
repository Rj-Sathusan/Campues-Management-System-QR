from tkinter import *


def btn_clicked():
    ko=(entry0.get(),entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get(),entry10.get(),entry11.get(),entry12.get(),entry13.get(),entry14.get(),entry15.get(),entry16.get(),entry17.get(),entry18.get(),entry19.get(),entry20.get(),entry21.get(),entry22.get(),entry23.get(),entry24.get(),entry25.get(),entry26.get(),entry27.get(),entry28.get())
    kj=(entry29.get())
    print(ko)
    str1 = ','.join(ko)
    str2 = ','+kj
    o=(str1+str2)
    f = open("Data.txt", "w")
    f.write(o)
    f.close()
    
f = open("Data.txt", "r")
ok=(f.read())
k=(ok.split(","))
print(k)

def btn_clicked2():
      import win32api
      win32api.MessageBox(0, 'Back', 'Alert')
      window.destroy()
      import Menu
      
window = Tk()
window.geometry("920x571")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 571,
    width = 920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    460.5, 287.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 5,
    highlightthickness = 30,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 740, y = 538,
    width = 170,
    height = 38)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    503.5, 141.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,
    )

entry0.place(entry0.insert(0,k[0]),
    x = 395.5, y = 132,
    width = 216.0,
    height = 17)


entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    503.5, 96.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(entry1.insert(0,k[1]),
    x = 395.5, y = 87,
    width = 216.0,
    height = 17)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    503.5, 225.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry2.place(entry2.insert(0,k[2]),
    x = 395.5, y = 216,
    width = 216.0,
    height = 17)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    503.5, 180.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry3.place(entry3.insert(0,k[3]),
    x = 395.5, y = 171,
    width = 216.0,
    height = 17)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    503.5, 502.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry4.place(entry4.insert(0,k[4]),
    x = 395.5, y = 493,
    width = 216.0,
    height = 17)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    503.5, 264.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry5.place(entry5.insert(0,k[5]),
    x = 395.5, y = 255,
    width = 216.0,
    height = 17)

entry6_img = PhotoImage(file = f"img_textBox6.png")
entry6_bg = canvas.create_image(
    503.5, 387.5,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry6.place(entry6.insert(0,k[6]),
    x = 395.5, y = 378,
    width = 216.0,
    height = 17)

entry7_img = PhotoImage(file = f"img_textBox7.png")
entry7_bg = canvas.create_image(
    503.5, 465.5,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry7.place(entry7.insert(0,k[7]),
    x = 395.5, y = 456,
    width = 216.0,
    height = 17)

entry8_img = PhotoImage(file = f"img_textBox8.png")
entry8_bg = canvas.create_image(
    503.5, 426.5,
    image = entry8_img)

entry8 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry8.place(entry8.insert(0,k[8]),
    x = 395.5, y = 417,
    width = 216.0,
    height = 17)

entry9_img = PhotoImage(file = f"img_textBox9.png")
entry9_bg = canvas.create_image(
    503.5, 342.5,
    image = entry9_img)

entry9 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry9.place(entry9.insert(0,k[9]),
    x = 395.5, y = 333,
    width = 216.0,
    height = 17)

entry10_img = PhotoImage(file = f"img_textBox10.png")
entry10_bg = canvas.create_image(
    762.0, 141.5,
    image = entry10_img)

entry10 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry10.place(entry10.insert(0,k[10]),
    x = 696.5, y = 132,
    width = 131.0,
    height = 17)

entry11_img = PhotoImage(file = f"img_textBox11.png")
entry11_bg = canvas.create_image(
    762.0, 96.5,
    image = entry11_img)

entry11 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry11.place(entry11.insert(0,k[11]),
    x = 696.5, y = 87,
    width = 131.0,
    height = 17)

entry12_img = PhotoImage(file = f"img_textBox12.png")
entry12_bg = canvas.create_image(
    762.0, 225.5,
    image = entry12_img)

entry12 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry12.place(entry12.insert(0,k[12]),
    x = 696.5, y = 216,
    width = 131.0,
    height = 17)

entry13_img = PhotoImage(file = f"img_textBox13.png")
entry13_bg = canvas.create_image(
    762.0, 180.5,
    image = entry13_img)

entry13 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry13.place(entry13.insert(0,k[13]),
    x = 696.5, y = 171,
    width = 131.0,
    height = 17)

entry14_img = PhotoImage(file = f"img_textBox14.png")
entry14_bg = canvas.create_image(
    765.0, 500.5,
    image = entry14_img)

entry14 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry14.place(entry14.insert(0,k[14]),
    x = 699.5, y = 491,
    width = 131.0,
    height = 17)

entry15_img = PhotoImage(file = f"img_textBox15.png")
entry15_bg = canvas.create_image(
    762.0, 264.5,
    image = entry15_img)

entry15 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry15.place(entry15.insert(0,k[15]),
    x = 696.5, y = 255,
    width = 131.0,
    height = 17)

entry16_img = PhotoImage(file = f"img_textBox16.png")
entry16_bg = canvas.create_image(
    762.0, 387.5,
    image = entry16_img)

entry16 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry16.place(entry16.insert(0,k[16]),
    x = 696.5, y = 378,
    width = 131.0,
    height = 17)

entry17_img = PhotoImage(file = f"img_textBox17.png")
entry17_bg = canvas.create_image(
    762.0, 465.5,
    image = entry17_img)

entry17 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry17.place(entry17.insert(0,k[17]),
    x = 696.5, y = 456,
    width = 131.0,
    height = 17)

entry18_img = PhotoImage(file = f"img_textBox18.png")
entry18_bg = canvas.create_image(
    762.0, 426.5,
    image = entry18_img)

entry18 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry18.place(entry18.insert(0,k[18]),
    x = 696.5, y = 417,
    width = 131.0,
    height = 17)

entry19_img = PhotoImage(file = f"img_textBox19.png")
entry19_bg = canvas.create_image(
    762.0, 342.5,
    image = entry19_img)

entry19 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry19.place(entry19.insert(0,k[19]),
    x = 696.5, y = 333,
    width = 131.0,
    height = 17)

entry20_img = PhotoImage(file = f"img_textBox20.png")
entry20_bg = canvas.create_image(
    169.0, 500.5,
    image = entry20_img)

entry20 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry20.place(entry20.insert(0,k[20]),
    x = 40.5, y = 491,
    width = 257.0,
    height = 17)

entry21_img = PhotoImage(file = f"img_textBox21.png")
entry21_bg = canvas.create_image(
    169.0, 465.5,
    image = entry21_img)

entry21 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry21.place(entry21.insert(0,k[21]),
    x = 40.5, y = 456,
    width = 257.0,
    height = 17)

entry22_img = PhotoImage(file = f"img_textBox22.png")
entry22_bg = canvas.create_image(
    169.0, 426.5,
    image = entry22_img)

entry22 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry22.place(entry22.insert(0,k[22]),
    x = 40.5, y = 417,
    width = 257.0,
    height = 17)

entry23_img = PhotoImage(file = f"img_textBox23.png")
entry23_bg = canvas.create_image(
    169.0, 387.5,
    image = entry23_img)

entry23 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry23.place(entry23.insert(0,k[23]),
    x = 40.5, y = 378,
    width = 257.0,
    height = 17)

entry24_img = PhotoImage(file = f"img_textBox24.png")
entry24_bg = canvas.create_image(
    169.0, 342.5,
    image = entry24_img)

entry24 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry24.place(entry24.insert(0,k[24]),
    x = 40.5, y = 333,
    width = 257.0,
    height = 17)

entry25_img = PhotoImage(file = f"img_textBox25.png")
entry25_bg = canvas.create_image(
    169.0, 264.5,
    image = entry25_img)

entry25 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry25.place(entry25.insert(0,k[25]),
    x = 40.5, y = 255,
    width = 257.0,
    height = 17)

entry26_img = PhotoImage(file = f"img_textBox26.png")
entry26_bg = canvas.create_image(
    169.0, 225.5,
    image = entry26_img)

entry26 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry26.place(entry26.insert(0,k[26]),
    x = 40.5, y = 216,
    width = 257.0,
    height = 17)

entry27_img = PhotoImage(file = f"img_textBox27.png")
entry27_bg = canvas.create_image(
    169.0, 180.5,
    image = entry27_img)

entry27 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry27.place(entry27.insert(0,k[27]),
    x = 40.5, y = 171,
    width = 257.0,
    height = 17)

entry28_img = PhotoImage(file = f"img_textBox28.png")
entry28_bg = canvas.create_image(
    169.0, 141.5,
    image = entry28_img)

entry28 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry28.place(entry28.insert(0,k[28]),
    x = 40.5, y = 132,
    width = 257.0,
    height = 17)

entry29_img = PhotoImage(file = f"img_textBox29.png")
entry29_bg = canvas.create_image(
    169.0, 96.5,
    image = entry29_img)

entry29 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry29.place(entry29.insert(0,k[29]),
    x = 40.5, y = 87,
    width = 257.0,
    height = 17)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 1,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b1.place(
    x = 861, y = 9,
    width = 48,
    height = 47)

window.resizable(False, False)
window.mainloop()
