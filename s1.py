from tkinter import *
from tkinter import ttk
# from tkinter import Tk
import tkinter as tk
from backend import *
from bs4 import BeautifulSoup as bs
from pywebcopy import save_website
from tkinter import messagebox
from tkhtmlview import HTMLLabel

gui= Tk()
gui.title("SYNAPSE")
gui.geometry("1024x400")
gui.config(bg="#fff")

top_frame=Frame(gui,borderwidth=0, bg="lemonchiffon",relief='sunken',pady=40,)
top_frame.pack(fill='x')
outputframe=Frame(top_frame,bg='lemonchiffon',borderwidth=0,pady=30)
outputframe.pack(anchor='center')

my_input = Text(outputframe,height=1,width=76,pady=20,padx=20)
my_input.grid(row=0, column=1,padx=45)

# def saveinput():
#     var=my_input.get(1.0,"end-1c")
#     params=tab1.get(1.0,"end-1c")
#     author=tab2.get(1.0,"end-1c")
#     head=tab3.get(1.0,"end-1c")
#     json1=tab4.get(1.0,"end-1c")
#     tab_1.config(text=var)
#     print(var)
#     print(params)
#     print(author)
#     print(head)
#     print(json1)


def dropdown():
    newvar=clicked.get()
    # print(newvar)
    return newvar

def saveinput():
    url=my_input.get(1.0,"end-1c")
    auth=tab2.get(1.0,"end-1c")
    head=tab3.get(1.0,"end-1c")
    drop=dropdown()
    code,text,header=request(drop,url,auth,head)
    soup = bs(text,'html.parser')
    prettyHTML = soup.prettify()
    print(prettyHTML)
    lbl1.delete("1.0","end")
    lbl1.insert(tk.END,prettyHTML) #due to insert() we get a scroll bar too!!
    lbl2.set_html(text)
    print(header)
    lbl3.delete("1.0","end")
    lbl3.insert(tk.END,header)
    # lbl1.config(text=text)
    # lbl2.config(text=text)
    status.config(text="Status Code:"+str(code))

def saveproject():
    link=my_input.get(1.0,"end-1c")
    save_website(url=link,project_folder="./saved_folder/")
    messagebox.showinfo("Success!","Project folder saved")
    


sendbtn=Button(outputframe,text="send",bg='lavender',fg='black',padx=20,command=saveinput)
sendbtn.grid(row=0, column=2)
savebtn=Button(outputframe,text="save",bg='lavender',fg='black',padx=20,command=saveproject)
savebtn.grid(row=0, column=4)

option=[
    "GET",
    "PUT",
    "POST",
    "PATCH",
    "DELETE"
]
clicked=StringVar()
clicked.set("GET")
drop= OptionMenu(outputframe,clicked,*option,command=dropdown)
drop.grid(row=0,column=0)
drop.configure(bg="lavender",fg="black",padx=20)

tabcontrol=ttk.Notebook(top_frame,height=100,width=400)
tab1=Text(tabcontrol,width=100)
tab2=Text(tabcontrol,width=100)
tab3=Text(tabcontrol,width=100)
tab4=Text(tabcontrol,width=100)
tabcontrol.add(tab1,text='params')
tabcontrol.add(tab2,text='authorization')
tabcontrol.add(tab3,text='headers')
tabcontrol.add(tab4,text='json')
tabcontrol.pack(fill='both',padx=40,pady=45)

#responseframe
responseframe=Frame(gui,borderwidth=0,bg='#fff')
responseframe.pack()
sframe=Frame(responseframe,padx=3,pady=3,bg='#fff',highlightbackground='black',highlightthickness=3)
sframe.pack()
statusframe=Frame(sframe,bg="#fff")
statusframe.pack()



#tab output
tabcontrol=ttk.Notebook(gui,height=700,width=1200)
tab_1=Label(tabcontrol,width=100,height=10,text="",bg='#fff')
tab_2=Label(tabcontrol,width=100,height=9,text="",bg='#fff')
tab_3=Label(tabcontrol,width=100,height=9,text="",bg='#fff')
tabcontrol.add(tab_1,text ='Raw')
tabcontrol.add(tab_2,text ='Preview')
tabcontrol.add(tab_3,text ='Headers')
tabcontrol.pack()

# Status Code 
status=Label(statusframe,text="Status Code:000",height=1,width=16)
status.pack()

# Label Creation
lbl1=Text(tab_1,height=1150,width=100,padx=50,pady=50,bg="#fff",fg="black")
lbl1.pack()
lbl2=HTMLLabel(tab_2,html="preview",height=1150,width=100,padx=50,pady=50,bg="#fff",fg="black")
lbl2.pack()
lbl3=Text(tab_3,height=1150,width=100,padx=50,pady=50,bg="#fff",fg="black")
lbl3.pack()

# status=Label(statusframe,text="status code:000",height=1,width=16)
# status.pack()

gui.mainloop()