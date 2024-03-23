from customtkinter import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Click count app")
        self.geometry("300x300")
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.count_click = 0

        self.label = CTkLabel(self, text="Welcome")
        self.label.cget('font').configure(size=20)
        self.label.grid(row=0, column=1, )

        self.label_count_click = CTkLabel(self, text=f"Count click: {self.count_click}")
        self.label_count_click.grid(row=1, column=1, sticky='n')

        self.button = CTkButton(self, text="Click Me", command=self.click_count)
        self.button.grid(row=1, column=1)

        self.advanced_settings_frame = AdvancedSettingFrame(self)
        self.advanced_settings_frame.grid(row=2, column=0, columnspan=3, padx=20)

    def click_count(self):
        self.count_click += self.advanced_settings_frame.selected.get()
        self.label_count_click.configure(self, text=f'Count click: {self.count_click}')


class AdvancedSettingFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.selected = IntVar()
        self.selected.set(1)
        self.rad_1 = CTkRadioButton(self, text='+1', value=1, variable=self.selected)
        self.rad_1.grid(row=0, column=0)
        self.rad_2 = CTkRadioButton(self, text='+10', value=10, variable=self.selected)
        self.rad_2.grid(row=0, column=1)

        self.reset_button = CTkButton(self, text="Reset",
                                      width=100,
                                      command=self.reset_count_click)
        self.reset_button.grid(row=0, column=2)

    def reset_count_click(self):
        self.master.count_click = 0
        self.master.label_count_click.configure(self, text=f'Count click: {self.master.count_click}')


window = MainWindow()
window.mainloop()
