from customtkinter import *

def click():
    global count_click
    count_click += 1
    clicks.configure(text=f'Count clicks: {count_click}')

window = CTk()
window.title('My window')
window.geometry('400x300')

window.grid_columnconfigure(index=0, weight=1)
window.grid_rowconfigure(index=(0, 1, 2, 3), weight=1)

label = CTkLabel(window, text='Example text in CustomTkinter')
label.grid(row=0, column=0)
label.cget('font').configure(size=20)

count_click = 0
clicks = CTkLabel(window, text=f'Count clicks: {count_click}')
clicks.grid(row=1, column=0)

button = CTkButton(window, text='Click', command=click)
button.grid(row=2, column=0)

checkbox_frame = CTkFrame(window)
checkbox_frame.grid(row=3, column=0)
checkbox_frame.grid_columnconfigure(0, weight=1)
checkbox_frame.grid_rowconfigure((0, 1), weight=1)

checkbox_1 = CTkCheckBox(checkbox_frame, text='Variable 1')
checkbox_1.grid(row=0, column=0)
checkbox_2 = CTkCheckBox(checkbox_frame, text='Variable 2')
checkbox_2.grid(row=1, column=0)

window.mainloop()