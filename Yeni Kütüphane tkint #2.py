#----Tkinter----#
import tkinter as tk #Tkinter kütüphanesini içeri aktar
form =tk.Tk()#Pencereyi açar
form.geometry("500x500+250+150")
#----Functions----#
def topla():
    sonuc_1.pack(expand=True)
    form.after(2000, lambda: sonuc_1.pack_forget())
#----Butonlar----#
buton_1 =tk.Button(form,text="1+1",fg="green",bg="red",font="Times 30 bold",command=topla)
#----Labels----#
sonuc_1 =tk.Label(form,text="2",fg="black",font="Times 17")
#----Packs----#
buton_1.pack(side=tk.BOTTOM) # BOTTOM ALT TOP ÜST EXPAND =TRUE ORTA LEFT SOL RIGHT SAĞ
sonuc_1.pack_forget()



form.mainloop()#Pencereyi x e basana kadar açık tut