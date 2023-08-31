import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.title("CTk test")

        # add widgets to app
        self.button = ctk.CTkButton(self, command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)

    # add methods to app
    def button_click(self):
        print("button click")


app = App()
app.mainloop()