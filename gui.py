import customtkinter as customtkinter
import matplotlib.pyplot as plt
from MovingAverage import MovingAverage as MA
import numpy as np
from config import API_KEY
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

customtkinter.set_default_color_theme("green")

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Tab creation with .add
        self.add("Menu")
        self.add("Simple MA")

        # add widgets on tabs
        self.tabMenu()
        self.tabGraph()
        
    def tabMenu(self): 
        '''
        template for any widget to be added into the 'Menu' tab. 

        '''
        self.label = customtkinter.CTkLabel(master=self.tab("Menu"))
        self.label.configure(text="MAIN MENU", padx=450, fg_color=('#00bb7c'), font=(None,20))
        # on the grid, can pad on x or y direction
        self.label.grid(row=0, column=1, padx=20, pady=10)


    def tabGraph(self): 
        '''
        template for any widget to be added into the 'Graph' tab. Will contain an interactive graph with toggle-able options.
        '''
        
        # selecting a colour theme
        plt.style.use('seaborn-v0_8-pastel')

        # retreives data and prepares it according to MovingAverage.py
        mdf = MA(API_KEY)
        mdf.retrieve_data('2023-01-01', '2023-09-01', 'AAPL')
        mdf.prepare_data()

        windows = [5,20,50,100,200]
        mdf.simple_moving_averages(windows)
        
        # creating a scatterplot of closing prices
        fig, ax = plt.subplots()

        # set x,y points, and show as scatterplot
        x = mdf.data['date']
        y = mdf.data['close']
        ax.scatter(x,y,label='Closing Prices', color='blue', marker='.')

        # plot line graphs for each moving average
        for period in windows: 
            ax.plot(x, mdf.data[f'{period} day ma'])
            ax.legend()

        ax.legend()

        # DOC NEEDED FOR THIS. using old get_tk_widget from Tkinter. 
        canvas = FigureCanvasTkAgg(fig, master=self.tab("Simple MA"))
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=customtkinter.BOTH, expand=True)
        


        





class App(customtkinter.CTk):
    '''
    the main class to initiate and run the actual application. 
    derives functionalities from parent method CTk

    '''
    def __init__(self):
        super().__init__()

        # configure the grid system
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        # setting the size of the app window
        self.geometry("800x800")    # W x H

        # setting the title of the app
        self.title("Trade Analyser Basic")
        
        
        # Create the Tabview WIDGET as the main display of the app. 
        self.tab_view = MyTabView(master=self, width=800, height=700)    # can enter arguments for width/length of tab
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


# running the app
app = App()
app.mainloop()