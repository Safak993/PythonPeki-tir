#----Tkinter----#
import tkinter as tk # Tkinter kütüphanesini içe aktar
form = tk.Tk()#Pencereyi masaüstünde aç
#----Geometrys----#
form.geometry("500x500+250+170")
#----Labels----#
yazi = tk.Label(form,text="Selamin aleykum",fg="red",bg="blue",font="Times 20 italic")#fg = yazının rengi bg ise yazının arka plan
#----Butonlar----#
buton =tk.Button(form,text="Tıkla",fg="black",bg="purple",font="Times 30")
#----Packs----#
yazi.pack()
buton.pack(side=tk.RIGHT)
form.mainloop() #Pencereyi x e basana kadar açık tut
