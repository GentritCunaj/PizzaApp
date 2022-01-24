from tkinter import *
from PIL import ImageTk,Image
import smtplib
root = Tk()
root.geometry("600x800")

# Emri piceris
Emri_frame = LabelFrame(root,padx=250,pady=5)
Emri_frame.pack()

Emri = Label(Emri_frame, text="Piceria")
Emri.pack()

#Figura picers
pica_img = ImageTk.PhotoImage(Image.open("picafig.jpg"))
pica_label = Label(image=pica_img)
pica_label.pack(anchor=E,padx=30,pady=30)

# Funksionet e madhesise se pices

vogelvar=StringVar()
mesmevar=StringVar()
madhevar=StringVar()
numrivar=IntVar()
numrivar.set(1)

def click_small():
    if small_pica_but["state"] == med_pica_but["state"] and big_pica_but["state"]:
        med_pica_but.config(state=DISABLED)
        big_pica_but.config(state=DISABLED)
    else:
        med_pica_but.config(state=NORMAL)
        big_pica_but.config(state=NORMAL)
    checkState()

def click_med():
    if med_pica_but["state"] == small_pica_but["state"] and big_pica_but["state"]:
        small_pica_but.config(state=DISABLED)
        big_pica_but.config(state=DISABLED)
    else:
        small_pica_but.config(state=NORMAL)
        big_pica_but.config(state=NORMAL)
    checkState()


def click_big():
    if big_pica_but["state"] == med_pica_but["state"] and small_pica_but["state"]:
        med_pica_but.config(state=DISABLED)
        small_pica_but.config(state=DISABLED)
    else:
        med_pica_but.config(state=NORMAL)
        small_pica_but.config(state=NORMAL)
    checkState()





# Butonat e madhesise se pices dhe numrat e porosise
numri_drop = OptionMenu(root,numrivar,1,2,3,4,5,6,7,8,9,10)
numri_drop.place(x=30,y=60)

small_pica_but = Checkbutton(root,text="E vogel",variable=vogelvar,onvalue="E vogel",offvalue="",command=click_small)
small_pica_but.deselect()
small_pica_but.place(x=80,y=60)
med_pica_but = Checkbutton(root,text="E mesme",variable=mesmevar,onvalue="E mesme",offvalue="",command=click_med)
small_pica_but.deselect()
med_pica_but.place(x=160,y=60)
big_pica_but = Checkbutton(root,text="E madhe",variable=madhevar,onvalue="E madhe",offvalue="",command=click_big)
small_pica_but.deselect()
big_pica_but.place(x=250,y=60)





#checkboxes of toppings
checkbox_var1 = StringVar()
checkbox_var2 = StringVar()
checkbox_var3 = StringVar()
checkbox_var4 = StringVar()

checkbox_list = [numrivar,checkbox_var1,checkbox_var2,checkbox_var3,checkbox_var4,vogelvar,mesmevar,madhevar]


c1 = Checkbutton(root,text="kaqkavall",variable=checkbox_var1, onvalue="kaqkavall", offvalue="")
c1.deselect()
c1.place(x=30,y=120)
c2 = Checkbutton(root,text="sallam",variable=checkbox_var2, onvalue="sallam", offvalue="")
c2.deselect()
c2.place(x=30,y=150)
c3 = Checkbutton(root,text="ereza",variable=checkbox_var3, onvalue="ereza", offvalue="")
c3.deselect()
c3.place(x=30,y=180)
c4 = Checkbutton(root,text="kerpurdha",variable=checkbox_var4, onvalue="kerpurdha", offvalue="")
c4.deselect()
c4.place(x=30,y=210)




#Funksionet e kohes

def checkTimeSmall():
    global numrivar
    t1=numrivar.get()
    e1 =str(t1*5) 
    l1 = Label(root,text=e1+" min").place(x=540,y=680)


def checkTimeMed():
    global numrivar
    t2=numrivar.get()
    e2 = str(t2*5+2)
    l2 = Label(root,text=e2+" min").place(x=540,y=680)
    
    

def checkTimeBig():
    global numrivar
    t3 = numrivar.get()
    e3 = str(t3*5+5)
    l3 = Label(root,text=e3+" min").place(x=540,y=680)
    
   



# funksionet e butonave konfirmo dhe fshi
orderbox = Listbox(root,width=60,height=25)

def konfirmo():  
    global orderbox
    orderbox.insert(END,"\n")  
    for i in range(len(checkbox_list)):
        if(checkbox_list[i].get() != ""):
            checkbox_label = Label(root, text=checkbox_list[i].get()) 
            orderbox.insert(END,checkbox_list[i].get())
            orderbox.pack(pady=100)
    if vogelvar.get() != "":
        checkTimeSmall()
    elif mesmevar.get() != "":
        checkTimeMed()
    elif madhevar.get() != "":
        checkTimeBig()

  

def delete_order():
    orderbox.delete(0,END)

    
    


 
 
konfirm_but = Button(root, text="Konfirmo",padx=10,pady=5,command=konfirmo, state=DISABLED)
konfirm_but.place(x=200,y=300)
delete_but = Button(root,text="Fshi",padx=15,pady=5,command=delete_order)
delete_but.place(x=300,y=300)



# cakto madhesine patjeter
def checkState():
    if vogelvar.get() != "" or  mesmevar.get() != "" or madhevar.get() != "" :
        konfirm_but.config(state=NORMAL)
    else: konfirm_but.config(state=DISABLED)


# dergo email
def send_mail():
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("gentrit.qunaj2044@gmail.com","jjlmdgdsnflguzmk")
    subject="Porosi e re" 
    body = orderbox.get(0,END)
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(
        "gentrit.qunaj2044@gmail.com",
        "qunajgentrit@gmail.com",
        msg
    )
    server.quit()

Dergo_but=Button(root,text="Dergo",command=send_mail,padx=10,pady=5)
Dergo_but.place(x=280,y=700)


# main loop
root.mainloop()