from tkinter import *


window = Tk()
window.title("Mile to Km convertor!!")
window.config(padx=20, pady=20)



#answer
answer_label = Label(text=0)
answer_label.grid(column=1, row=1)

def answer():
    answer = float(input.get())
    km = round(answer * 1.609)
    answer_label.config(text=f"{km}")






#title label

title_label = Label(text=" ")
title_label.grid()
title_label.config(padx=10, pady=10)


#input

input = Entry(width=10)
input.grid(column=1, row=0)


#miles label

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

#is_equal Label

sentence_label = Label(text="is equal to")
sentence_label.grid(column=0, row=1)


#km label

km_label = Label(text="km")
km_label.grid(column=2, row=1)


#button 

button = Button(text="Calculate", command=answer)
button.grid(column=1, row=2)





window.mainloop()