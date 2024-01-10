from tkinter import*
#Start app
root = Tk()
root.title('My first app on python!')
root.geometry('400x200+700+500')
root.resizable(width=False, height=False)

value = StringVar()


#Function
def test():
    get = value.get()
    z["text"] = get

z = Label(text='Тестовый текст')
x = Entry(textvariable=value)
c = Button(command=test, text='Ok')
#c.bind('<Button-1>', test)
#grid(), pack()
z.pack(side=BOTTOM)
x.pack()
c.pack()
#Finish app
root.mainloop()