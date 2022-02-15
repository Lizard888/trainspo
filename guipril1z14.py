#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from datetime import date
import requests
import datetime
from bs4 import BeautifulSoup
from xml.dom import minidom
import json
import xml.etree.ElementTree as ET
import tkinter.scrolledtext as st
import tkinter as tk
from tkinter.ttk import Combobox  
import pdb



res1=0
res2=0
res=0



def  clicked1():
    global res2
    global res
    global res1
    global combo1
    res = combo.get()
   
    slov={"Вельяминово":"9602029", "Жилево":"9600694", "Михнево":"9600749", "Павелецкий вокзал":"2000005",  "Ступино":"9601202",  "Акри":"9601726", "Белопесоцкий":"9600772", "Грачевская":"9603877", "Моссельмаш":"9603478", "Химки":"9603401",
          "Малино":"9600212", "Ленинградский вокзал":"2006004", "Конаково":"9603735"}
    res1=slov.get(res)
 
   
    if res1=='9603877':
       lbl1 = Label(window, text="Ленинградское")  
       lbl1.grid(column=0, row=6)
       combo1 = Combobox(window)
       combo1['values'] = ("Ленинградский вокзал","Химки","Моссельмаш")  
       combo1.current(1)  # установите вариант по умолчанию  
       combo1.grid(column=0, row=8) 
       
 
    
    elif res1=='2000005':
       lbl1 = Label(window, text="Павелецкое")  
       lbl1.grid(column=0, row=6)
       combo1 = Combobox(window)  
       combo1['values'] = ("Михнево", "Акри", "Ступино", "Белопесоцкий")  
       combo1.current(1)  # установите вариант по умолчанию
       combo1.grid(column=0, row=8)
    

      #pdb.set_trace()  
    return(res1)
    
def clicked2():
      global res3
      global res5
      global res6
      global txt3
      global txt4
    
      res3=combo1.get()
     
      lbl3 = Label(window, text="час")  
      lbl3.grid(column=0, row=14)  
      txt3 = Entry(window,width=10)  
      txt3.grid(column=0, row=16)

      lbl4 = Label(window, text="мин")  
      lbl4.grid(column=0, row=18)  
      txt4 = Entry(window,width=10)  
      txt4.grid(column=0, row=20)
     
    
      return(res3)
def clicked(text6):
      
       global res5
       global res6
      
       c=0
       m=0
       cm=0
       res2=combo.get()
      
       slov1=[]
       res5=txt3.get()
       res6= txt4.get()
    
       k=0
       nak=0
       
       nk=0
       slov={"Вельяминово":"9602029", "Жилево":"9600694", "Михнево":"9600749", "Павелецкий вокзал":"2000005",  "Ступино":"9601202",  "Акри":"9601726", "Белопесоцкий":"9600772", "Грачевская":"9603877", "Моссельмаш":"9603478", "Химки":"9603401",
          "Малино":"9600212", "Ленинградский вокзал":"2006004", "Конаково":"9603735"}
       res1=slov.get(res2)
       if res1=="2000005": nak=1

    
    
       res4=slov.get(res3)
     
      
       current_date = date.today()
       url11=chr(34)

       url="https://api.rasp.yandex.net/v3.0/search/?apikey=622f978d-a274-41bd-b297-e7de99a7ab1f&format=json&from=s"
       url1=res4
       url2="&to=s"
       url3=res1
       url4="&lang=ru_RU&page=1&date="
       url5=str(current_date)
       url6=url+url3+url2+url1+url4+url5
      
       response = requests.get(url6.strip())
       data = response.json()
       i=0
       
#работаем со временем
    
    
       try:
         chas2=int(res5)
        
       except ValueError:
     
        ls='Это что ещё такое?'
        k=1 
       try:  
         min2=int(res6)
       except ValueError:
       
         ls='Это что ещё такое?'
         k==1
       except UnboundLocalError:
       
         ls='Это что ещё такое?'
         k=1
     
       if k==1: text6.insert(tk.INSERT," Введите время")
       else:      
          now = datetime.datetime.now()  
       
          #pdb.set_trace()
          realchas=int(now.hour)
          realmin=int( now.minute)
          min=realmin+min2+20
          
          if (min>=60):
            min=min-60
            if (nak==1):chas=realchas+chas2+2      
            else:chas=realchas+chas2+1
           
          else:     
            if nak==1: chas=realchas+chas2+1
            else:chas=realchas+chas2      
       
          #for item in data:
       
          for item in data['segments']:
            it=item
            it1=item['departure']
       
            dt=it1[11:16]
            ch=dt[0:2]
            mn=dt[3:5]
          
      
            ch1=int(ch)
            mn1=int(mn)
       
            if (ch1>chas) :
             
              slov1.append(it1[11:16])
            elif (ch1==chas) and (mn1>=min):
             
              slov1.append(it1[11:16])
            i=i+1
         
         
          i=0
    
      
       
          text6.delete(1.0, END) 
          if len(slov1)!=0:
            while i<=(len(slov1)-1):
             
            
             text6.insert(tk.INSERT,slov1[i])
             text6.insert(tk.INSERT,"                                                  ")
             i=i+1
          else: text6.insert(tk.INSERT," Вы не успеваете ни на один")     

 
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")  
 
window.geometry('400x250')  
lbl = Label(window, text="станция отправления")  
lbl.grid(column=0, row=0)


window.geometry('400x250')  
combo = Combobox(window)  
combo['values'] = ("Павелецкий вокзал", "Грачевская")  
combo.current(1)  # установите вариант по умолчанию  
combo.grid(column=0, row=2)
btn = Button(window, text="станция прибытия", command=clicked1)  
btn.grid(column=0, row=4)



def new_window(event):#второе окно
    root = Toplevel(window)
    root.geometry('400x400')
    root.title('Второе окно')
 
    text6 = st.ScrolledText(root,width = 30, height = 8,font = ("Times New Roman",15))
    text6.grid(column = 0, pady = 10, padx = 10)


  
    clicked(text6)





btn = Button(window, text="время до выхода", command=clicked2)  
btn.grid(column=0, row=12)


btn = Button(window, text='Клик')
btn.grid(column=0, row=24)

btn.bind('<Button->', new_window)
val = StringVar()
 
entry = Entry(window, textvariable=val)





window.mainloop()


























