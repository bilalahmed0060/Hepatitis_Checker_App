from tkinter import *
from PIL import Image,ImageTk
import numpy as np
import pickle


file1 = pickle.load(open('SVC_Classifier.pkl','rb'))
file2 = pickle.load(open('RFT_Regressor.pkl','rb'))

MWindow = Tk()
MWindow.title("MODEL SELECTOR")
MWindow.geometry("550x550+300+200")



global HWindow

def hp():
    global file1
    def pred():
        def home():
            Preds.destroy()
            MWindow.deiconify()
        # Get Concrete Data Variable
        var_CT = [a1.get(), a2.get(), a3.get(), a4.get(), a5.get(), a6.get(), a7.get(), a8.get(), a9.get(), a10.get(), a11.get(), a12.get(), a13.get(), a14.get(), a15.get(), a16.get(), a17.get(), a18.get(), a19.get()]



        if len(a1.get()) == 0 or len(a2.get()) == 0 or len(a3.get()) == 0 or len(a4.get()) == 0 or len(a5.get()) == 0 or len(a6.get()) == 0 or len(a7.get()) == 0 or len(a8.get()) == 0 or len(a9.get()) == 0 or len(a10.get()) == 0 or len(a11.get()) == 0 or len(a12.get()) == 0 or len(a13.get()) == 0 or len(a14.get()) == 0 or len(a15.get()) == 0 or len(a16.get()) == 0 or len(a17.get()) == 0 or len(a18.get()) == 0 or len(a19.get()) == 0:
            pass
        else:
            # Get Concrete Data from Variables
            val_CT = []

            for x in var_CT:
                val_CT.append((x))

            data = np.array([val_CT])
            try:
                sss = file1.predict(data)

                if sss == 1:
                    sss = "Hepatitis"
                else:
                    sss = "Normal"

                HWindow.withdraw()

                Preds = Toplevel()
                Preds.geometry("600x250+200+150")
                Preds.title("Predictions")
                Label(Preds, image=hp).pack()

                Label(Preds, text=sss, highlightthickness=0, fg='white', background='#098da1',
                      font=("Courier", 22)).place(bordermode='inside', x=380, y=66)

                Button(Preds, image=hpt, highlightthickness=0, bd=0, command=home).place(x=150, y=150)

                def Destroying():
                    MWindow.destroy()

                Preds.protocol('WM_DELETE_WINDOW', Destroying)

                Preds.mainloop()

            except:
                pass

    MWindow.withdraw()

    h = ImageTk.PhotoImage(Image.open('static/Hepatitis.png'))
    p = ImageTk.PhotoImage(Image.open('static/PREDICT.png'))
    hp = ImageTk.PhotoImage(Image.open('static/hp.png'))
    hpt = ImageTk.PhotoImage(Image.open('static/home.png'))

    HWindow = Toplevel()
    HWindow.geometry('750x550+200+150')
    HWindow.title("Hepatitis Checker")
    Label(HWindow,image = h).place(x=-2,y=-2)

    a1 = Entry(HWindow, width=20)
    a2 = Entry(HWindow, width=20)
    a3 = Entry(HWindow, width=20)
    a4 = Entry(HWindow, width=20)
    a5 = Entry(HWindow, width=20)
    a6 = Entry(HWindow, width=20)
    a7 = Entry(HWindow, width=20)
    a8 = Entry(HWindow, width=20)
    a9 = Entry(HWindow, width=20)
    a10 = Entry(HWindow, width=20)
    a11 = Entry(HWindow, width=20)
    a12 = Entry(HWindow, width=20)
    a13 = Entry(HWindow, width=20)
    a14 = Entry(HWindow, width=20)
    a15 = Entry(HWindow, width=20)
    a16 = Entry(HWindow, width=20)
    a17 = Entry(HWindow, width=20)
    a18 = Entry(HWindow, width=20)
    a19 = Entry(HWindow, width=20)
    btn_predict = Button(HWindow,image = p,highlightthickness=0,bd=0,command=pred)

    a1.place(x=220,y=152)
    a2.place(x=220,y=182)
    a3.place(x=220,y=212)
    a4.place(x=220,y=242)
    a5.place(x=220,y=272)
    a6.place(x=220,y=302)
    a7.place(x=220,y=332)
    a8.place(x=220,y=362)
    a9.place(x=220,y=392)

    a10.place(x=600,y=152)
    a11.place(x=600,y=182)
    a12.place(x=600,y=212)
    a13.place(x=600,y=242)
    a14.place(x=600,y=272)
    a15.place(x=600,y=302)
    a16.place(x=600,y=332)
    a17.place(x=600,y=362)
    a18.place(x=600,y=392)
    a19.place(x=600,y=422)
    btn_predict.place(x=220,y=460)

    def Destroying():
        MWindow.destroy()

    HWindow.protocol('WM_DELETE_WINDOW', Destroying)

    HWindow.mainloop()

def ct():
    global file2
    def pred():
        def home():
            Preds.destroy()
            MWindow.deiconify()
        # Get Concrete Data Variable
        var_CT = [a1.get(), a2.get(), a3.get(), a4.get(), a5.get(), a6.get(), a7.get(), a8.get()]



        if len(a1.get()) == 0 or len(a2.get()) == 0 or len(a3.get()) == 0 or len(a4.get()) == 0 or len(a5.get()) == 0 or len(a6.get()) == 0 or len(a7.get()) == 0 or len(a8.get()) == 0:
            pass
        else:
            # Get Concrete Data from Variables
            val_CT = []

            for x in var_CT:
                val_CT.append((x))

            data = np.array([val_CT])
            try:
                sss = file2.predict(data)


                CWindow.withdraw()
                Preds = Toplevel()
                Preds.geometry("600x250+200+150")
                Preds.title("Predictions")
                Label(Preds, image=ct).pack()
                Label(Preds, text=sss, highlightthickness=0, fg='white', background='#098da1',
                      font=("Courier", 16)).place(bordermode='inside', x=405, y=68)

                Button(Preds, image=ctp, highlightthickness=0, bd=0, command=home).place(x=150, y=150)

                def Destroying():
                    MWindow.destroy()

                Preds.protocol('WM_DELETE_WINDOW', Destroying)

                Preds.mainloop()

            except:
                pass





    MWindow.withdraw()

    c = ImageTk.PhotoImage(Image.open('static/Concrete.png'))
    p = ImageTk.PhotoImage(Image.open('static/PREDICT.png'))
    ct = ImageTk.PhotoImage(Image.open("static/ct.png"))
    ctp = ImageTk.PhotoImage(Image.open("static/home.png"))

    CWindow = Toplevel()
    CWindow.geometry('750x550+200+150')
    CWindow.title("Concrete Strength Checker")
    Label(CWindow, image=c).place(x=-2, y=-2)

    a1 = Entry(CWindow,width=30)
    # a1.insert(0,"100.0 to 550.0")
    a2 = Entry(CWindow,width=30)
    # a2.insert(0,"0.0 to 360.0")
    a3 = Entry(CWindow,width=30)
    # a3.insert(0,"0.0 to 201.0")
    a4 = Entry(CWindow,width=30)
    # a4.insert(0,"121.0 to 247.0")
    a5 = Entry(CWindow,width=30)
    # a5.insert(0,"0.0 32.2")
    a6 = Entry(CWindow,width=30)
    # a6.insert(0,"800.0 to 1145.0")
    a7 = Entry(CWindow,width=30)
    # a7.insert(0,"590.0 to 993.0")
    a8 = Entry(CWindow,width=30)
    # a8.insert(0,"1 to 365")

    # a1.bind("<Key>",a1.config(a1.delete('0','end')))
    btn_predict = Button(CWindow,image = p,highlightthickness=0,bd=0,command=pred)

    a1.place(x=450,y=152)
    a2.place(x=450,y=182)
    a3.place(x=450,y=212)
    a4.place(x=450,y=242)
    a5.place(x=450,y=272)
    a6.place(x=450,y=302)
    a7.place(x=450,y=332)
    a8.place(x=450,y=362)
    btn_predict.place(x=220,y=400)

    def Destroying():
        MWindow.destroy()

    CWindow.protocol('WM_DELETE_WINDOW', Destroying)

    CWindow.mainloop()

window = Image.open('static/Model Selection Window.png')
btn1 = Image.open('static/BTN1.png')
btn2 = Image.open('static/BTN2.png')


loaded1 = ImageTk.PhotoImage(window)
loaded2 = ImageTk.PhotoImage(btn1)
loaded3 = ImageTk.PhotoImage(btn2)

back= Label(MWindow,image=loaded1)
back.place(x=-2,y=-2)

Button1 = Button(MWindow,image=loaded2,bd=0,highlightthickness=0,command=hp)
Button1.place(x=100,y=200)

Button2 = Button(MWindow,image=loaded3,bd=0,highlightthickness=0,command=ct)
Button2.place(x=100,y=350)
MWindow.mainloop()

