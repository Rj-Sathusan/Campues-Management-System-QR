from tkinter import *
from ttkwidgets.autocomplete import AutocompleteEntry
countries = [
        'Professional Practices', 'Programming','Networking','Database Design & Development','Security',
'Managing a Successful Computing project',
'Computer System Architecture',
'Web Design & Development',
'Business Intelligence',
'Computing Research Project',
'Data Structure & Algorithms',
'Advance Programming',
'Discrete Maths','System analysis Design','E-commerce']

def btn_clicked2():
        window.destroy()
        import Menu1

def ff(x):
        import wget
        import os
        remote_url = x
            # Define the local filename to save data
        local_file = entry.get()+' brief.zip'
            # Make http request for remote file data
        wget.download(remote_url, local_file)
def btn_clicked():
    if entry.get()==countries[0]:
        ff("")
    if entry.get()==countries[1]:
        ff("https://6kmg9w.dm.files.1drv.com/y4mdWR5iKqF9OxJQ0VIYCJ6CkNICdtZ3hifLe-9zOMVx8fPw1SkQRT6uZkkAiFNMArtTC5nAtGezsAIrRRuK1NyxJ7UMGyPEJsy4_xAxAKL2uX1YoezLugZpCqvoLvUepWCkRiKdjSb3IVSruDO2Etf2bsJAlbs8IMr4EI7qjr6RaicMdsPxpfO-lKGJBNsMWLb-iZQUYJcq7RSbbqww7dSTw")
    if entry.get()==countries[2]:
        ff("")
    if entry.get()==countries[3]:
        ff("")
    if entry.get()==countries[4]:
        ff("https://jbifpg.dm.files.1drv.com/y4mURpXN7vRjGPijjAvrgf55FEzXCB_3cPJoO9nrpHfR-lhYUYNKCrG3AlqD_DtEBGyfXZmX3BHNJpaydP_KawW3yaYKvbpXg2A1d7XF2kYnv7OU3UNf1NKskpSRwiGXx7YNPzZSq1FI_aC_uS2am4sZkwxz7QutivD0UZUsmIWtj98_CUJMV6HFpkDl3XUm22cdn50Quqmay1bu9RaY3gpwQ")
    if entry.get()==countries[5]:
        ff("")
    if entry.get()==countries[6]:
        ff("")
    if entry.get()==countries[7]:
        ff("")
    if entry.get()==countries[8]:
        ff("")
    if entry.get()==countries[9]:
        ff("")
    if entry.get()==countries[10]:
        ff("")
    if entry.get()==countries[11]:
        ff("")
    if entry.get()==countries[12]:
        ff("")
    if entry.get()==countries[13]:
        ff("")
    if entry.get()==countries[14]:
        ff("")





        

window = Tk()

window.geometry("385x192")
window.configure(bg = "#e5e5e5")
canvas = Canvas(
    window,
    bg = "#e5e5e5",
    height = 192,
    width = 385,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background==.png")
background = canvas.create_image(
    192.5, 96.0,
    image=background_img)

img0 = PhotoImage(file = f"img0==.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b0.place(
    x = 336, y = 8,
    width = 45,
    height = 21)

img1 = PhotoImage(file = f"img1==.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 126, y = 140,
    width = 126,
    height = 37)
Label(
    window, 
    font = ('Times',15),
    text='ASSIGNMENT DOCUMENTS\n\n'
    ).pack()

entry = AutocompleteEntry(
    window, 
    width=30, 
    font=('Times', 15),
    completevalues=countries
    )


entry.pack()

window.resizable(False, False)
window.mainloop()
