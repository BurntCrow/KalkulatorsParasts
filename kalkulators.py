from tkinter import*
mansLogs=Tk()
mansLogs.title("Kalkulators")
mansLogs.geometry("500x500")

btn0=Button(mansLogs, text="0", padx="40", pady="20").grid(row=8, column=1)
btn1=Button(mansLogs, text="1", padx="40", pady="20").grid(row=7, column=0)
btn2=Button(mansLogs, text="2", padx="40", pady="20").grid(row=7, column=1)
btn3=Button(mansLogs, text="3", padx="40", pady="20").grid(row=7, column=2)
btn4=Button(mansLogs, text="4", padx="40", pady="20").grid(row=6, column=0)
btn5=Button(mansLogs, text="5", padx="40", pady="20").grid(row=6, column=1)
btn6=Button(mansLogs, text="6", padx="40", pady="20").grid(row=6, column=2)
btn7=Button(mansLogs, text="7", padx="40", pady="20").grid(row=5, column=0)
btn8=Button(mansLogs, text="8", padx="40", pady="20").grid(row=5, column=1)
btn9=Button(mansLogs, text="9", padx="40", pady="20").grid(row=5, column=2)
btnp=Button(mansLogs, text=".", padx="40", pady="20").grid(row=8, column=2)
btnpplus=Button(mansLogs, text="+/-", padx="40", pady="20").grid(row=8, column=0)
btnperc=Button(mansLogs, text="%", padx="40", pady="20").grid(row=4, column=2)
btniek=Button(mansLogs, text="()", padx="40", pady="20").grid(row=4, column=1)
btnC=Button(mansLogs, text="C", padx="40", pady="20").grid(row=4, column=0)
btndiv=Button(mansLogs, text="/", padx="40", pady="20").grid(row=4, column=3)
btnmul=Button(mansLogs, text="X", padx="40", pady="20").grid(row=5, column=3)
btnneg=Button(mansLogs, text="-", padx="40", pady="20").grid(row=6, column=3)
btnadd=Button(mansLogs, text="+", padx="40", pady="20").grid(row=7, column=3)
btneq=Button(mansLogs, text="=", padx="40", pady="20").grid(row=8, column=3)
mansLogs.mainloop()