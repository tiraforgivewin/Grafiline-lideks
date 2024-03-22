from tkinter import *
kl=0
def vajuta():
    global kl
    kl+=1
    nupp.configure(text=kl)
def vajuta2(event):
    global kl
    kl-=1
    nupp.configure(text=kl)
def tst_psse(event):
    t=textbox.get()
    pealkiri.configure(text=t,width=len(t))
    textbox.delete(0,END)
def valik():
    arv=var.get()
    textbox.insert(END,arv)





aken=Tk()
aken.geometry("400x400")
aken.iconbitmap('robin.ico')
aken.title("Tkineri kasutamine")
tekst1="Pealkiri"
pealkiri=Label(aken,
               text="tekst1",
               bg="#bcee68",
               fg="#f44336",
               font="Algerian 20",
               height=3,
               width=len(tekst1))
textbox=Entry(aken,
               bg="#47aaef",
               fg="#000000",
               font="Algerian 20",
               width=20,
               justify=CENTER)
tekst2="Vajuta mind! "
nupp=Button(aken,
            text=tekst2,
            height=3,
            width=len(tekst2),
            bg="#34ffef",
            command=vajuta,
            font="Arial 20",
            relief=RAISED)



var=IntVar()
f=Frame(aken)
e=Radiobutton(f,text="Esimine",variable=var,value=1,bg="#c7bdf0",font="Algerian 20",command=valik)
t=Radiobutton(f,text="Teine",variable=var,valu=2,bg="#c7bdf0",font="Algerian 20",command=valik)
k=Radiobutton(f,text="Kolmas",variable=var,value=3,bg="#c7bdf0",font="Algerian 20",command=valik)



nupp.bind("<Button-3>",vajuta2)
textbox.bind("<Return>",tst_psse)

obj=[pealkiri,textbox,nupp,f]
for i in obj:
    i.pack()

obj2=[e,t,k]
for i in range(len(obj2)):
    obj2[i].grid(row=0,column=i)

aken.mainloop()
