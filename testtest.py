from tkinter import Tk, Listbox, Button

scores=Tk()
def addDate():
    i = 1
    listbox.insert(i, "10-12-12")
    i = i + 1


my_btn = Button(scores, text="add date", fg="white", heigh=2, bg="#000066", command=addDate,
                activebackground="cyan").grid(row=1,column=1)

listbox = Listbox(scores, width=35, height=15, highlightbackground="grey50")
listbox.grid(row=3,column=1)



scores.mainloop()