from tkinter import *
from tkinter import ttk as TTk
tk = Tk()
tk.title('Tkinter Widget Testing (for Tkinter Editor)')
tk.geometry('640x480')
c = Canvas(width=640, height=480, highlightthickness=0)
c.pack()
off_var = BooleanVar()
on_var = BooleanVar()
off_var.set(False)
on_var.set(True)
entry_var = StringVar()
dis_entry_var = StringVar()
TTk_entry_var = StringVar()
TTk_dis_entry_var = StringVar()
text_var = 'Text\nbox'
dis_text_var = 'Disabled\ntext\nbox'
entry_var.set('Entry box')
dis_entry_var.set('Disabled entry box')
TTk_entry_var.set('TTk entry box')
TTk_dis_entry_var.set('TTk disabled entry box')
Button(text='Normal button').place(x=15, y=15)
Button(text='Active button', relief='sunken').place(x=15, y=45)
Button(text='Disabled button', state='disabled').place(x=15, y=75)
Button(text='Active+disabled button?', relief='sunken', state='disabled').place(x=15, y=105)
TTk.Button(text='TTk Normal button').place(x=15, y=135)
TTk.Button(text='TTk Disabled button', state='disabled').place(x=15, y=165)
# 165
Checkbutton(text='Off checkbox', variable=off_var).place(x=180, y=15)
Checkbutton(text='On checkbox', variable=on_var).place(x=180, y=45)
Checkbutton(text='Off+disabled checkbox', variable=off_var, state='disabled').place(x=180, y=75)
Checkbutton(text='On+disabled checkbox', variable=on_var, state='disabled').place(x=180, y=105)
TTk.Checkbutton(text='TTk Off checkbox', variable=off_var).place(x=180, y=135)
TTk.Checkbutton(text='TTk On checkbox', variable=on_var).place(x=180, y=165)
TTk.Checkbutton(text='TTk Off+disabled checkbox', variable=off_var, state='disabled').place(x=180, y=195)
TTk.Checkbutton(text='TTk On+disabled checkbox', variable=on_var, state='disabled').place(x=180, y=225)

Entry(textvariable=entry_var, width=27).place(x=180, y=255)
Entry(textvariable=dis_entry_var, state='disabled', width=27).place(x=180, y=285)
TTk.Entry(textvariable=TTk_entry_var, width=27).place(x=180, y=315)
TTk.Entry(textvariable=TTk_dis_entry_var, state='disabled', width=27).place(x=180, y=345)
t1 = Text(width=27, height=11, font=('Segoe UI', 9, 'normal'))
t1.insert(END, text_var)
t1.place(x=350, y=15)
t2 = Text(width=27, height=11, font=('Segoe UI', 9, 'normal'))
t2.insert(END, dis_text_var)
t2.place(x=350, y=197)
t2.configure(state='disabled')

Scale(orient=HORIZONTAL, length=72.5).place(x=15, y=195)
Scale(orient=HORIZONTAL, length=72.5, showvalue=False).place(x=95, y=214)
Scale(orient=HORIZONTAL, length=72.5, state='disabled').place(x=15, y=195+40)
Scale(orient=HORIZONTAL, length=72.5, showvalue=False, state='disabled').place(x=95, y=214+40)
TTk.Scale(orient=HORIZONTAL, length=72.5, to=1).place(x=15, y=195+100)
TTk.Scale(orient=HORIZONTAL, length=72.5, to=1, state='disabled').place(x=15, y=195+140)
Scale(orient=VERTICAL, length=72.5).place(x=520, y=15)
Scale(orient=VERTICAL, length=72.5, showvalue=False).place(x=542, y=35+72.5)
Scale(orient=VERTICAL, length=72.5, state='disabled').place(x=520, y=(35+72.5*2)+15)
Scale(orient=VERTICAL, length=72.5, state='disabled', showvalue=False).place(x=542, y=(35+72.5*3)+35)
TTk.Scale(orient=VERTICAL, length=72.5).place(x=520+45, y=15)
TTk.Scale(orient=VERTICAL, length=72.5, state='disabled').place(x=542+25, y=(35+72.5*3)+35)

sb = Variable()
sb.set(0)
Spinbox(width=3, increment=1, textvariable=sb, from_=-5, to=5).place(x=15+85, y=195+100)
Spinbox(state='disabled', width=3, increment=1, textvariable=sb, from_=-5, to=5).place(x=15+85, y=195+140)
TTk.Spinbox(width=3, increment=1, textvariable=sb, from_=-5, to=5).place(x=15+85+40, y=195+100)
TTk.Spinbox(state='disabled', width=3, increment=1, textvariable=sb, from_=-5, to=5).place(x=15+85+40, y=195+140)


while True:
    try:
        tk.update()
        off_var.set(False); on_var.set(True)
    except TclError:
        break
    except KeyboardInterrupt:
        break
