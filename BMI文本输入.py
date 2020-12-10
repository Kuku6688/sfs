import tkinter
import tkinter.messagebox
def msgbox():
    tkinter.messagebox.showinfo(title="BMI",message = say_jisuan())
    

root = tkinter.Tk()
button = tkinter.Button(root,text = "计算",command = msgbox)
button.place(x=60,y=75,height=30,width=80)


lab = tkinter.Label(root, text="身高:", width=30, height=10)
lab.place(x=10,y=10,width=30,height=10)

lab = tkinter.Label(root, text="体重:", width=30, height=10)
lab.place(x=10,y=30,width=30,height=10)

hight = tkinter.StringVar(root)
entryHight = tkinter.Entry(root,width = 150, textvariable=hight)
entryHight.place(x=50,y=5,width=100 ,height=20)


weight = tkinter.StringVar(root)
entryWeight = tkinter.Entry(root,width = 150, textvariable=weight)
entryWeight.place(x=50,y=30,width=100 ,height=20)

def say_jisuan():
    hig = float(hight.get())
    wei = float(weight.get())
    bmi = round(wei / (hig * hig),2)
    return bmi


root.mainloop()