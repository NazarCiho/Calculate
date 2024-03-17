from tkinter import *
import tkinter.colorchooser
from tkinter import messagebox
from tkinter.filedialog import *
root=Tk()
root.title('Вибір автомобіля')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'700x500+{int((w/2)-350)}+{int((h/2)-250)}')
def color():
    global rgb_color
    counting('color')
    rgb_color, web_color = tkinter.colorchooser.askcolor(parent=root,initialcolor=(255, 0, 0))
    if rgb_color==None:
        rgb_color=(255,255,255)
        web_color='#FFFFFF'
    lab_color['bg']=web_color
    lab_color['activebackground']=web_color
def counting(zminna):
    global p1,p2,p3,p4,p5,p6
    if zminna=='stan':
        p1=1
    elif zminna=='marka':
        p2=1
    elif zminna=='year':
        p3=1
    elif zminna=='motor':
        p4=1
    elif zminna=='country':
        p5=1
    elif zminna=='color':
        p6=1
def rez():
    global text_rez
    try:
        if p1 and p2 and p3 and p4 and p5 and p6:
            text_rez=f'֍ Стан: {stan.get()}, ֍ Марка: {marka.get()}, ֍ Рік випуску: {year.get()}, ֍ Вид мотору: {motor.get()}, ֍ Країна виробник: {country.get()}, ֍ Колір: {rgb_color}֍'
            rez_text.delete(1.0,END)
            rez_text.insert(1.0,text_rez)
            but_save.place(x=595, y=450)
    except:
        messagebox.showerror('ПОМИЛКА!','Помилка! ви не обрали всі пункти')
def save():
    name = askopenfilename()
    try:
        with open(name, 'w', encoding="utf-8") as file:
            file.write(text_rez)
    except:
        messagebox.showerror('ERROR','Ви не обрали файл')
but_save=Button(root,text='Зберегти',font=(None,13),command=save)
root.config(background='bisque')
rez_text=Text(width=72,height=4,font=('Times new roman',14))
rez_text.place(x=25,y=350)
but_rez=Button(root,text='Результат вибору',font=('Times new roman',14),command=rez,relief=SOLID,background='lime')
but_rez.place(x=275,y=450)
but_color=Button(text='Оберіть колір',command=color,relief=SOLID,background='yellow')
lab_color=Button(text='',relief=SOLID,width=30,height=3,command=color)
but_color.place(x=487,y=225)
lab_color.place(x=420,y=265)
#############Стан###################################
stan_lab=LabelFrame(root, text='Оберіть стан авто',relief=SOLID,background='bisque')
stan_lab.place(x=25,y=20)
stan=StringVar()
stan.set(None)
stan_rbNew=Radiobutton(stan_lab,text='Новий автомобіль', variable=stan,value='Новий автомобіль',font=(None,11),background='bisque',activebackground='lime',foreground='blue',command=lambda:counting('stan')).pack()
stan_rbBy=Radiobutton(stan_lab,text='Б\У автомобіль', variable=stan,value='Б\У автомобіль',font=(None,11),background='bisque',activebackground='lime',foreground='blue',command=lambda:counting('stan')).pack(side=LEFT)
#############Марка###################################
marka_lab=LabelFrame(root, text='Виберіть марку',relief=SOLID,background='bisque')
marka_lab.place(x=25,y=120)
marka=StringVar()
marka.set(None)
marka_BMW=Radiobutton(marka_lab,text='BMW', variable=marka,value='BMW',font=(None,11),background='bisque',activebackground='lime',foreground='red',command=lambda:counting('marka')).pack(anchor=W)
marka_MERCEDES=Radiobutton(marka_lab,text='Mercedes', variable=marka,value='Mercedes',background='bisque',activebackground='lime',foreground='red',font=(None,11),command=lambda:counting('marka')).pack(anchor=W)
marka_KIA=Radiobutton(marka_lab,text='KIA', variable=marka,value='KIA',font=(None,11),background='bisque',activebackground='lime',foreground='red',command=lambda:counting('marka')).pack(anchor=W)
marka_TOYOTA=Radiobutton(marka_lab,text='Toyota', variable=marka,value='Toyota',font=(None,11),background='bisque',activebackground='lime',foreground='red',command=lambda:counting('marka')).pack(anchor=W)
marka_AUDI=Radiobutton(marka_lab,text='Audi', variable=marka,value='Audi',font=(None,11),background='bisque',activebackground='lime',foreground='red',command=lambda:counting('marka')).pack(anchor=W)
marka_MAZDA=Radiobutton(marka_lab,text='Mazda', variable=marka,value='Mazda',font=(None,11),background='bisque',activebackground='lime',foreground='red',command=lambda:counting('marka')).pack(anchor=W)
marka_INSHE=Radiobutton(marka_lab,text='Інша', variable=marka,value='Інша',font=(None,11),background='bisque',activebackground='lime',foreground='red',command=lambda:counting('marka')).pack(anchor=W)
#############Рік випуску###################################
year_lab=LabelFrame(root, text='Оберіть рік випуску',relief=SOLID,background='bisque')
year_lab.place(x=235,y=20)
year=StringVar()
year.set(None)
year_1=Radiobutton(year_lab,text='2024', variable=year,value='2024',font=(None,11),background='bisque',activebackground='lime',foreground='green',command=lambda:counting('year')).pack(anchor=W)
year_2=Radiobutton(year_lab,text='2020-2023', variable=year,value='2020-2023',font=(None,11),background='bisque',activebackground='lime',foreground='green',command=lambda:counting('year')).pack(anchor=W)
year_3=Radiobutton(year_lab,text='2010-2019', variable=year,value='2010-2019',font=(None,11),background='bisque',activebackground='lime',foreground='green',command=lambda:counting('year')).pack(anchor=W)
year_4=Radiobutton(year_lab,text='2000-2009', variable=year,value='22000-2009',font=(None,11),background='bisque',activebackground='lime',foreground='green',command=lambda:counting('year')).pack(anchor=W)
year_5=Radiobutton(year_lab,text='1990-1999', variable=year,value='1990-1999',font=(None,11),background='bisque',activebackground='lime',foreground='green',command=lambda:counting('year')).pack(anchor=W)
year_6=Radiobutton(year_lab,text='1980-1989', variable=year,value='1980-1989',font=(None,11),background='bisque',activebackground='lime',foreground='green',command=lambda:counting('year')).pack(anchor=W)
year_7=Radiobutton(year_lab,text='<1980', variable=year,value='<1980',font=(None,11),background='bisque',activebackground='lime',foreground='green',command=lambda:counting('year')).pack(anchor=W)
#############Вид мотору###################################
motor_lab=LabelFrame(root, text='Оберіть вид мотору',relief=SOLID,background='bisque')
motor_lab.place(x=235,y=255)
motor=StringVar()
motor.set(None)
motor_1=Radiobutton(motor_lab,text='Бензиновий', variable=motor,value='Бензиновий',font=(None,11),background='bisque',activebackground='lime',foreground='orange',command=lambda:counting('motor')).pack(anchor=W)
motor_2=Radiobutton(motor_lab,text='Дизельний', variable=motor,value='Дизельний',font=(None,11),background='bisque',activebackground='lime',foreground='orange',command=lambda:counting('motor')).pack(anchor=W)
#############Країна виробник###################################
country_lab=LabelFrame(root, text='Оберіть виробника',relief=SOLID,background='bisque')
country_lab.place(x=470,y=20)
country=StringVar()
country.set(None)
country_1=Radiobutton(country_lab,text='США', variable=country,value='США',font=(None,11),background='bisque',activebackground='lime',foreground='maroon',command=lambda:counting('country')).pack(anchor=W)
country_2=Radiobutton(country_lab,text='Україна', variable=country,value='Україна',font=(None,11),background='bisque',activebackground='lime',foreground='maroon',command=lambda:counting('country')).pack(anchor=W)
country_3=Radiobutton(country_lab,text='Німеччина', variable=country,value='Німеччина',font=(None,11),background='bisque',activebackground='lime',foreground='maroon',command=lambda:counting('country')).pack(anchor=W)
country_4=Radiobutton(country_lab,text='Японія', variable=country,value='Японія',font=(None,11),background='bisque',activebackground='lime',foreground='maroon',command=lambda:counting('country')).pack(anchor=W)
country_5=Radiobutton(country_lab,text='Китай', variable=country,value='Китай',font=(None,11),background='bisque',activebackground='lime',foreground='maroon',command=lambda:counting('country')).pack(anchor=W)
country_6=Radiobutton(country_lab,text='Інша', variable=country,value='Інша',font=(None,11),background='bisque',activebackground='lime',foreground='maroon',command=lambda:counting('country')).pack(anchor=W)
root.mainloop()