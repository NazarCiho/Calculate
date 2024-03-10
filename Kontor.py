from tkinter import *
from tkinter import LabelFrame, messagebox
from tkinter.ttk import Combobox
root=Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'630x400+{int((w/2)-315)}+{int((h/2)-200)}')
root.title('Програма-кантор')
root.config(background='pale green')
#####################Functions################################################
def kyrs(kyr):
    entry_price.delete(0,END)
    entry_price.insert(0,kyr)
    entry_count.insert(0,1)
original_text_buy = 'До сплати: '
original_text_sell = 'Ви отримаєте: '

def calculation():
    try:
        if diya.get() == 'Продаж' or diya.get() == 'Купівля':
            price=float(entry_price.get())
            count=float(entry_count.get())
            suma=price*count
            if diya.get()=='Продаж':
                lab_splata['text']=original_text_sell+str(suma)
            elif diya.get()=='Купівля':
                lab_splata['text']=original_text_buy+str(suma)
        else:
            messagebox.showerror('Помилка вибору дії','Ви не вибрали дію (Купівля чи Продаж)')
    except ValueError:
        messagebox.showerror('Помилка введення даних!','Ви ввели некоректні дані!!!!!')
def state_of_but_action(a,b):
    rb2.config(state=b)
    rb1.config(state=a)
def current_valute(event):
    v=combo.get()
    entry_price.delete(0,END)
    entry_price.delete(0, END)
    entry_price.insert(0, valutes[v])
    if v=='USD - $ (Долар)':
        lab_val['text']='$'
    elif v=='EUR - € (Євро)':
        lab_val['text']='€'
    elif v=='PLN - zł (Польський злотий)':
        lab_val['text']='zł'
    elif v=='GBP - £ (Фунт стерлінгів)':
        lab_val['text']='£'
    elif v=='CZK - Kč (Чеська крона)':
        lab_val['text']='Kč'
def buy_sell():

    if diya.get()=='Продаж':
        lab_splata['text']='Ви отримаєте: '
    elif diya.get()=='Купівля':
        lab_splata['text']='До сплати: '

##########################Choice a Valute###########################################
lab_vubir=Label(text='Оберіть валюту',font=('Times New Roman',15),background='pale green')
lab_vubir.place(x=255,y=6)
combo=Combobox(root, width=23,state='readonly',font=('Times New Roman',13))
valutes={'USD - $ (Долар)':38.5,'EUR - € (Євро)':42,'PLN - zł (Польський злотий)':9,'GBP - £ (Фунт стерлінгів)':49,'CZK - Kč (Чеська крона)':1.65}
combo['values'] = list(valutes.keys())
combo.current(0)
combo.place(x=210,y=34)
combo.bind("<Return>",current_valute)
combo.bind("<ButtonPress-1>",current_valute)
##########################Choice Action###########################################
lab_diya=LabelFrame(root,text='Оберіть дію',font=('Times New Roman',14),relief=SOLID,background='pale green',foreground='purple')
lab_diya.place(x=40,y=66)
diya=StringVar()
rb1=Radiobutton(lab_diya,text='Купівля',variable=diya,value='Купівля',font=('Times New Roman',14),indicatoron=0,
                command=buy_sell, background='Red',foreground='gold',activebackground='tan1')
rb1.pack(side=LEFT)
rb2=Radiobutton(lab_diya,text='Продаж',variable=diya,value='Продаж',font=('Times New Roman',14),indicatoron=0,
                command=buy_sell,background='lime green', foreground='blue',activebackground='tan1')
rb2.pack()
diya.set('Купівля')
##########################Enter price###########################################
lab_price=Label(root, text='Курс: ',font=('Times New Roman',14),background='pale green')
lab_price.place(x=25,y=135)
entry_price=Entry(font=('Times New Roman',13),relief=SOLID)
entry_price.place(x=25,y=165)
##########################Enter count###########################################
lab_count=Label(root, text='Кількість: ',font=('Times New Roman',14),background='pale green')
lab_count.place(x=25,y=195)
entry_count=Entry(font=('Times New Roman',13),relief=SOLID)
entry_count.place(x=25,y=225)
##########################Splata###########################################
lab_splata=Label(text='До сплати: ',font=('Times New Roman',15),background='yellow', relief=SOLID)
lab_splata.place(x=250,y=320)
but_calc=Button(text='Підрахунок',font=('Times New Roman',15),relief=SOLID,command=calculation,background='yellow')
but_calc.place(x=245,y=265)
lab_val=Label(text='$',font=(None,55),background='pale green')
lab_val.place(x=230,y=130)
kyrs(38.5)
root.mainloop()