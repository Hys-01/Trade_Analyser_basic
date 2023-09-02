import customtkinter as customtkinter
import matplotlib as plt

customtkinter.set_default_color_theme("green")

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Tab creation with .add
        self.add("Menu")
        self.add("Graph")

        # add widgets on tabs

        # Label widget  
        self.label = customtkinter.CTkLabel(master=self.tab("Menu"))

        # on the grid, can pad on x or y direction; unsure about row/column
        self.label.grid(row=0, column=0, padx=20, pady=10)

    def tabGraph(self): 
        pass
    


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.geometry("800x800")    # W x H
        self.title("Trade Analyser Draft")
        
        
        # Tabview WIDGET 
        self.tab_view = MyTabView(master=self, width=800, height=600)    # can enter arguments for width/length of tab
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()