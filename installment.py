from tkinter import *

# تابع محاسبه و نمایش نتیجه
def natige():
    # دریافت مقادیر از ویجت‌های Entry و تبدیل آن‌ها به نوع مناسب
    mablagh = float(ent_mablgh.get())
    number = int(ent_number.get())
    sood = float(ent_sood.get())

    # انجام محاسبات
    y = mablagh * sood / 100
    x = (mablagh + y) / number

    # نمایش نتیجه با دو رقم اعشاری
    lbl_nahi.configure(text=f'$ مبلغ هر قسط : {x:.2f} تومان $')

# ایجاد پنجره اصلی
win = Tk()
win.geometry('350x500')
win.configure(bg = '#a4f9c9')

# ایجاد و قرار دادن برچسب‌ها
lbl_tooman = Label(win,text = '* مبلغ به تومان *',font = 'arial 15')
lbl_tooman.place(x=120,y = 10)
lbl_mablgh = Label(win, text='مبلغ وام :', font='arial 15 bold')
lbl_mablgh.place(x=50, y=50)
lbl_number = Label(win, text='تعداد اقساط :', font='arial 15 bold')
lbl_number.place(x=50, y=100)
lbl_sood = Label(win, text='سود وام :', font='arial 15 bold')
lbl_sood.place(x=50, y=150)
lbl_bank = Label(win, text='نام بانک :', font='arial 15 bold')
lbl_bank.place(x=50, y=200)

# ایجاد و قرار دادن ویجت‌های Entry
ent_mablgh = Entry(win, font='arial 15 bold', width=15)
ent_mablgh.place(x=150, y=50)
ent_number = Entry(win, font='arial 15 bold', width=15)
ent_number.place(x=150, y=100)
ent_sood = Entry(win, font='arial 15 bold', width=15)
ent_sood.place(x=150, y=150)
ent_bank = Entry(win, font='arial 15 bold', width=15)
ent_bank.place(x=150, y=200)

# ایجاد و قرار دادن دکمه
btn_natige = Button(win, text='محاسبه', font='arial 20 bold',bg = '#13d362', command=natige)
btn_natige.place(x=135, y=400)

# ایجاد و قرار دادن برچسب نتیجه
lbl_nahi = Label(win, font='arial 15 bold')
lbl_nahi.place(x=50, y=300)

# شروع حلقه رویداد Tkinter
win.mainloop()
 