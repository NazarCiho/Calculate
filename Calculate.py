
from tkinter import *
from tkinter import ttk, messagebox
import math
root=Tk()
root.title('Калькулятор')
root.geometry('360x513+600+200')
root.resizable(width=False, height=False)
def calculating():
    try:
        res = eval(ryadok.get().replace('²','**2').replace('³','**3').replace('sin(','math.sin(').replace('%','/100*'))
        ryadok.delete(0, 'end')
        ryadok.insert(0, res)
    except Exception as e:
        messagebox.showerror('Помилка', f'Помилка виконання операції: {e}')
def deleting(a):
    if a==1:
        cursor_position = ryadok.index(INSERT)
        if cursor_position > 0:
            ryadok.delete(cursor_position-1, cursor_position)
    else:
        ryadok.delete(0,'end')
def input_numbers(number):
    ryadok.insert('insert',number)
but_frame=Button(relief='solid',bg='DeepSkyBlue', borderwidth=0, state='disabled',width=49,height=33)
but_frame.place(x=5,y=5)
but_frame2=Button(relief='solid',bg='lavender', borderwidth=0, state='disabled',width=47,height=32)
but_frame2.place(x=12,y=12)
#----------ROW1---------#
but_percent=Button(text='%', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers('%'))
but_0 = Button(text='0', font=(None, 20), width=4, relief='solid', bg='snow', borderwidth=1,activeforeground='DimGray', activebackground='seashell2', command=lambda: input_numbers(0))
but_koma=Button(text='.', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers('.'))
but_equal=Button(text='=', font=(None, 20),width=4, relief='solid', bg='dodgerblue',borderwidth=3,activeforeground='DimGray', activebackground='seashell2', command=calculating)

but_percent.place(x=20,y=440)
but_0.place(x=102,y=440)
but_koma.place(x=184,y=440)
but_equal.place(x=266,y=438)
#----------ROW2---------#
but_1=Button(text='1', font=(None, 20),width=4, relief='solid', bg='snow',borderwidth=1,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers(1))
but_2=Button(text='2', font=(None, 20),width=4, relief='solid', bg='snow',borderwidth=1,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers(2))
but_3=Button(text='3', font=(None, 20),width=4, relief='solid', bg='snow',borderwidth=1,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers(3))
but_plus=Button(text='+', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers('+'))

but_1.place(x=20,y=375)
but_2.place(x=102,y=375)
but_3.place(x=184,y=375)
but_plus.place(x=266,y=375)
#----------ROW3---------#
but_4=Button(text='4', font=(None, 20),width=4, relief='solid', bg='snow',borderwidth=1,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers(4))
but_5=Button(text='5', font=(None, 20),width=4, relief='solid', bg='snow',borderwidth=1,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers(5))
but_6=Button(text='6', font=(None, 20),width=4, relief='solid', bg='snow',borderwidth=1,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers(6))
but_minus=Button(text='-', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers('-'))

but_4.place(x=20,y=310)
but_5.place(x=102,y=310)
but_6.place(x=184,y=310)
but_minus.place(x=266,y=310)
#----------ROW4---------#
but_7=Button(text='7', font=(None, 20),width=4, relief='solid', bg='snow',borderwidth=1,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers(7))
but_8=Button(text='8', font=(None, 20),width=4, relief='solid', bg='snow',borderwidth=1,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers(8))
but_9=Button(text='9', font=(None, 20),width=4, relief='solid', bg='snow',borderwidth=1,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers(9))
but_multiplication=Button(text='×', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers('*'))

but_7.place(x=20,y=245)
but_8.place(x=102,y=245)
but_9.place(x=184,y=245)
but_multiplication.place(x=266,y=245)
#----------ROW5---------#
but_dk4=Button(text='x³', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers('³'))
but_dk1=Button(text='sin()', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2', command=lambda: input_numbers('sin()'))
but_dk2=Button(text='x²', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers('²'))
but_division=Button(text='÷', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers('/'))

but_dk1.place(x=20,y=180)
but_dk4.place(x=102,y=180)
but_dk2.place(x=184,y=180)
but_division.place(x=266,y=180)
#----------ROW6---------#
but_bracket=Button(text=')', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers(')'))
but_C=Button(text='C', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2',command=lambda:deleting(2))
but_bracket2=Button(text='(', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2', command=lambda:input_numbers('('))
but_baccspace=Button(text='⌫', font=(None, 20),width=4, relief='solid', bg='deepskyblue',borderwidth=2,activeforeground='DimGray', activebackground='seashell2',command=lambda:deleting(1))

but_bracket.place(x=102,y=115)
but_C.place(x=184,y=115)
but_bracket2.place(x=20,y=115)
but_baccspace.place(x=266,y=115)
#--------OTHER----------#
ryadok=Entry(width=50, font=('Times new roman', 28), relief='solid',justify='right',borderwidth=2,validate="key")
ryadok.place(x=20, y=22, width=316,height=70)
but_line=Button(bg='cyan2', width=152, height=1, font=(None,3),relief='solid', state=DISABLED,borderwidth=1)
but_line.place(y=99, x=21)
root.mainloop()