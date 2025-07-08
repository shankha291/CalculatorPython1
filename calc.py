from tkinter import*

window=Tk()
window.title("Calculator Mini Project")
window.geometry("500x500")




frame=Frame(window)
for i in range(6):  # You have 6 rows: entry + 5 button rows
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)
frame.place(relx=0.5, rely=0.5, anchor="center")
is_result=False
def press(num):
    global is_result
    if is_result:
        entry.delete(0,END)
        is_result=False
    entry.insert(END,num)
    entry.xview_moveto(1)
    entry.config(fg="black")
def  pressop(op):
    global is_result
    entry.insert(END,op)
    is_result=False
    entry.xview_moveto(1)
    entry.config(fg="black")
def ac():
    entry.delete(0,END)
def backsp():
    entry.delete(len(entry.get())-1,END)
def total():
    global is_result
    try:
        result = str(eval(entry.get()))
        entry.delete(0, END)
        entry.insert(END, result)
        is_result = True
        entry.xview_moveto(1)  # Scrolls to the far right

    except ZeroDivisionError:
        entry.delete(0,END)
        entry.insert(END,"Can't Divide By Zero")
        entry.config(fg="red")
        is_result=True
    except (SyntaxError,TypeError,NameError):
        entry.delete(0,END)
        entry.config(fg="red")
        entry.insert(END,"Invalid Input")
        is_result=True
    except Exception:
        entry.delete(0,END)

        entry.insert(END,"Error!Write correctly")
        entry.config(fg="red")
        is_result=True

btn_style = {
    "font": ("consolas", 16),
    "height": 2,
    "width": 5,
    "relief": "groove",    
    "bd": 3  ,
    "bg":"white"              
}

entry_frame = Frame(frame)
entry_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")

scrollbar = Scrollbar(entry_frame, orient=HORIZONTAL)
scrollbar.pack(side=BOTTOM, fill=X)

entry = Entry(entry_frame, font=("consolas", 18), relief="groove", bd=3, justify="right",
              fg="black", xscrollcommand=scrollbar.set)
entry.pack(fill=BOTH, expand=True)

scrollbar.config(command=entry.xview)

btn1=Button(frame,text="AC",**btn_style,command=ac)
btn1.grid(row=1,column=0, padx=2, pady=2,sticky="nsew")
btn2=Button(frame,text="//",**btn_style,command=lambda:pressop("//"))
btn2.grid(row=1,column=1, padx=2, pady=2,sticky="nsew")
btn3=Button(frame,text="Del",**btn_style,command=backsp)
btn3.grid(row=1,column=2, padx=2, pady=2,sticky="nsew")
btn4=Button(frame,text="/",**btn_style,command=lambda:pressop("/"))
btn4.grid(row=1,column=3, padx=2, pady=2,sticky="nsew")
btn5=Button(frame,text="7",**btn_style,command=lambda:press(7))
btn5.grid(row=2,column=0, padx=2, pady=2,sticky="nsew")
btn6=Button(frame,text="8",**btn_style,command=lambda:press(8))
btn6.grid(row=2,column=1, padx=2, pady=2,sticky="nsew")
btn7=Button(frame,text="9",**btn_style,command=lambda:press(9))
btn7.grid(row=2,column=2, padx=2, pady=2,sticky="nsew")
btn8=Button(frame,text="X",**btn_style,command=lambda:pressop("*"))
btn8.grid(row=2,column=3, padx=2, pady=2,sticky="nsew")
btn9=Button(frame,text="4",**btn_style,command=lambda:press(4))
btn9.grid(row=3,column=0, padx=2, pady=2,sticky="nsew")
btn10=Button(frame,text="5",**btn_style,command=lambda:press(5))
btn10.grid(row=3,column=1, padx=2, pady=2,sticky="nsew")
btn11=Button(frame,text="6",**btn_style,command=lambda:press(6))
btn11.grid(row=3,column=2, padx=2, pady=2,sticky="nsew")
btn12=Button(frame,text="-",**btn_style,command=lambda:pressop("-"))
btn12.grid(row=3,column=3, padx=2, pady=2,sticky="nsew")
btn13=Button(frame,text="1",**btn_style,command=lambda:press(1))
btn13.grid(row=4,column=0, padx=2, pady=2,sticky="nsew")
btn14=Button(frame,text="2",**btn_style,command=lambda:press(2))
btn14.grid(row=4,column=1, padx=2, pady=2,sticky="nsew")
btn15=Button(frame,text="3",**btn_style,command=lambda:press(3))
btn15.grid(row=4,column=2, padx=2, pady=2,sticky="nsew")
btn16=Button(frame,text="+",**btn_style,command=lambda:pressop("+"))
btn16.grid(row=4,column=3, padx=2, pady=2,sticky="nsew")
btn17=Button(frame,text="0",**btn_style,command=lambda:press(0))
btn17.grid(row=5,column=0, padx=2, pady=2,columnspan=2,sticky="nsew")
btn18=Button(frame,text=".",**btn_style,command=lambda:pressop("."))
btn18.grid(row=5,column=2, padx=2, pady=2,sticky="nsew")
btn19=Button(frame,text="=",**btn_style,command=total)
btn19.grid(row=5,column=3, padx=2, pady=2,sticky="nsew")
window.mainloop()