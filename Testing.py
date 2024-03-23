from tkinter import *
import random, time
from tkinter import messagebox, ttk
root=Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'500x500+{int((w/2)-250)}+{int((h/2)-270)}')
root.title('Тестування')
def start():
    but_start.place_forget()
    lab_bg.place(x=50,y=50)
    lab_test.place(x=65, y=140)
    lab_oberit.place(x=65, y=100)
    lab_num.place(x=65, y=63)
    lab_quest.place(x=95, y=62)
    but_next.place(x=175, y=300)
    but_end.place(x=175, y=350)
    lab_time.place(x=392, y=55)
    lab_time_text.place(x=320, y=55)
    update_time()
    next()
x=0
rating = 0
def next():
    global x, rating

    words = {'Cat': 'Кіт', 'Chair': 'Крісло', 'Window': 'Вікно', 'Laptop': 'Ноутбук', 'Car': 'Машина',
             'Number': 'Номер', 'Circle': 'Коло',
             'Database': 'База даних', 'Interface': 'Інтерфейс', 'Width': 'Ширина', 'State': 'Стан',
             'Network': 'Мережа','end':'end'}
    name = list(words.keys())[x]
    lab_num['text']=f'{x+1})'
    if x!=0:
        select=variant.get()
        if select==0:
            lab_num['text'] = f'{x})'
            messagebox.showerror('Помилка вибору', 'Ви не обрали жодного варіанту відповіді!')
            return
        elif select==1:
            select_text=rb_1['text']
            if select_text==list(words.values())[x-1]:
                rating+=1
        elif select == 2:
            select_text=rb_2['text']
            if select_text==list(words.values())[x-1]:
                rating+=1
        elif select==3:
            select_text=rb_3['text']
            if select_text==list(words.values())[x-1]:
                rating+=1
    variant.set(0)
    variants=['Стіл','Програма','Собака',"Комп'ютер",'Велосипед','Програмне забезпечення','Висота',
              'Довжина','Штат','Інтернет','Місто','Безпека','Квадрат','Озеро','Літо','Колесо','Миша']
    lab_quest['text']=f'Перекладіть слово {name}'
    x+=1
    rand_number=random.randint(1,3)
    if rand_number==1:
        rb_1['text']=words[name]
        ran1=random.randint(0,16)
        ran2=ran1
        while ran2==ran1:
            ran2 = random.randint(0, 16)
        rb_2['text']=variants[ran1]
        rb_3['text']=variants[ran2]
    elif rand_number==2:
        rb_2['text']=words[name]
        ran1 = random.randint(0, 16)
        ran2 = ran1
        while ran2 == ran1:
            ran2 = random.randint(0, 16)
        rb_1['text'] = variants[ran1]
        rb_3['text'] = variants[ran2]
    elif rand_number==3:
        rb_3['text']=words[name]
        ran1 = random.randint(0, 16)
        ran2 = ran1
        while ran2 == ran1:
            ran2 = random.randint(0, 16)
        rb_1['text'] = variants[ran1]
        rb_2['text'] = variants[ran2]
    if name == 'end':
        end(rating)
        return
    return rating
def end(rating):
    but_next.place_forget()
    lab_quest.place_forget()
    lab_test.place_forget()
    lab_oberit.place_forget()
    lab_num.place_forget()
    but_end.place_forget()
    lab_end_time=Label(text=f"Ви справилися за {lab_time['text']} сек",background='SlateGray1',foreground='orange',font=('Times new roman',12))
    lab_end_time.place(x=105,y=100)
    lab_time.place_forget()
    lab_time_text.place_forget()
    lab_kinec=Label(text='Вітаємо!!! Ви пройшли тест\n Ваша оцінка:',font=('Times new roman',18),background='SlateGray1',foreground='red')
    lab_kinec.place(x=105,y=150)
    lab_bal=Label(text=f'{rating} з 12',font=('Times new roman',18),background='SlateGray1')
    lab_bal.place(x=220,y=220)
    progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate", maximum=100, value=0,)
    progress['value']=100/12*rating
    progress.place(x=155,y=280)
lab_testing=Label(text='Тестування з англійської мови',font=(None, 12),background='orange')
lab_testing.place(x=20,y=15)
################ТЕСТИ##################
root.config(background='paleturquoise1')
lab_bg=Label(root, width=56, height=26, bg="SlateGray1")
but_start=Button(text='Почати тестування',font=('Times new roman',15),height=4,width=19,command=start,background='orange')
but_start.place(x=145,y=220)
lab_oberit=Label(text='Оберіть один варіант відповіді',font=('Times new roman',11),background='SlateGray1')
lab_num=Label(text='1)',font=('Times new roman',13),background='SlateGray1')
lab_quest=Label(text='Перекладіть слово',font=('Times new roman',14),background='SlateGray1')
but_next=Button(text='Наступний тест',font=('Times new roman',14),background='cyan',foreground='slate blue',command=next)
lab_test=Frame(background='deep sky blue')
variant=IntVar()
rb_1=Radiobutton(lab_test,text='dd',variable=variant,value=1,font=('Times new roman',17),background='deep sky blue',activebackground='deep sky blue')
rb_1.pack(anchor=W)
rb_2=Radiobutton(lab_test,text='ww',variable=variant,value=2,font=('Times new roman',17),background='deep sky blue',activebackground='deep sky blue')
rb_2.pack(anchor=W)
rb_3=Radiobutton(lab_test,text='qq',variable=variant,value=3,font=('Times new roman',17),background='deep sky blue',activebackground='deep sky blue')
rb_3.pack(anchor=W)
lab_time_text=Label(text='Пройшло       сек',font=('Times new roman',13),background='black',foreground='lime')
lab_time = Label(text='-1',font=('Times new roman',13),background='black',foreground='lime')
def update_time():
    lab_time['text'] = int(lab_time['text']) + 1
    root.after(1000, update_time)
but_end=Button(text='Завершити тест', font=('Times new roman',14), background='light blue', foreground='blue', command=lambda: end(rating))
root.mainloop()
