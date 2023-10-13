import customtkinter as ctk
import matplotlib.pyplot as plt
from MovingAverage import MovingAverage as MA
import numpy as np
from config import API_KEY
import pandas as pd 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

ctk.set_default_color_theme("green")

class App(ctk.CTk):
    '''
    the main class to initiate and run the actual application. 
    derives functionalities from parent method CTk

    '''
    def __init__(self, sd, td):
        super().__init__()

        # configure the grid system
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)
 

        # setting the size of the app window
        self.geometry("1000x900")    # W x H

        # setting the title of the app
        self.title("Trade Analyser Basic")
        
        
        # Create the Tabview WIDGET as the main display of the app. 
        self.tab_view = MyTabView(master=self, width=1000, height=850, startD=sd, todayD=td)    # can enter arguments for width/length of tab
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, startD, todayD, **kwargs):
        '''
        initializes and sets up the tabs for the tabview widget

        inputs: 
            master: 
            kwargs: 
        '''
        super().__init__(master, **kwargs)
        self.startD = startD
        self.todayD = todayD
        # Tab creation with .add
        self.add("Menu")
        self.add("Graphs")
        self.add('Summary')
        self.add('SummaryS')

        # add widgets on tabs
        self.tabMenu()
        self.tabGraph()
        self.tabSummary() 
        self.tabSummaryS()
        
    def tabMenu(self): 
        '''
        template for any widget to be added into the 'Menu' tab. 

        '''
        self.label = ctk.CTkLabel(master=self.tab("Menu"))
        self.label.configure(text="MAIN MENU", padx = "550", fg_color=('#00bb7c'), font=(None,20))
        # on the grid, can pad on x or y direction
        self.label.grid(row=0, column=1, padx=20, pady=10)

        datetext = f"start point: {self.startD} \n end point: {self.todayD}"
        
        self.labeldates = ctk.CTkLabel(master=self.tab("Menu"))
        self.labeldates.configure(text=datetext, padx = "100", font=(None,20))
        # on the grid, can pad on x or y direction
        self.labeldates.grid(row=2, column=0, padx=20, pady=10)



        




    def tabGraph(self): 
        '''
        template for any widget to be added into the 'Graph' tab. Will plot closing prices and moving averages. 

        creates a MovingAverage Class, creates columns for simple and exponential moving averages. 
        '''
        
        # selecting a colour theme
        plt.style.use('seaborn-v0_8-pastel')

        # retreives data and prepares it according to MovingAverage.py
        mdf = MA(API_KEY)
        mdf.retrieve_data(self.startD, self.todayD, 'NVDA')
        mdf.prepare_data()

        windows_simple = [20,50,100]   # 100 and 200 are options as well idk
        mdf.simple_moving_averages(windows_simple)
        windows_exp = [5,8,13]
        mdf.exp_moving_averages(windows_exp)
        
        # creating a scatterplot of closing prices
        fig, ax = plt.subplots(figsize=(10,6))

        cmap_simple = plt.get_cmap('GnBu')  
        cmap_exp = plt.get_cmap('YlOrRd')
        colours_simple = [cmap_simple(0.1*x) for x in range(1,5)] 
        colours_exp =[cmap_exp(0.1*x) for x in range(1,5)]

        # set x,y points, and show as scatterplot
        x = mdf.data['date']
        y = mdf.data['close']
        ax.scatter(x,y,label='Closing Prices', color='blue', marker='.')

        # plot line graphs for each moving average and their label/legends
        for colour, period in enumerate(windows_simple): 
            ax.plot(x, mdf.data[f'{period} day SMA'], label = f'{period} day SMA', color = colours_simple[colour])
        for colour, period in enumerate(windows_exp): 
            ax.plot(x, mdf.data[f'{period} day EMA'], label = f'{period} day EMA', color = colours_exp[colour])

        fig.tight_layout()
        ax.legend(loc='upper left')  # Position the legend outside the plot for clarity

        # DOC NEEDED FOR THIS. using old get_tk_widget from Tkinter. 
        canvas = FigureCanvasTkAgg(fig, master=self.tab("Graphs"))
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=ctk.BOTH, expand=True)
    
    def tabSummary(self): 
        pass 

    def tabSummaryS(self): 
        '''
        serves as an informative explanation for the outcome in the Summary tab. 

        Specifically explains golden crosses and death crosses based on several example MAs. 
        '''


        txt = '''
        Comparisons:
Short-Term Analysis (Intra-day or few days):

5-day SMA vs. 5-day EMA: Since both have the same period, comparing these will give you an idea of short-term price momentum. 
The EMA will react more quickly to price changes, so when the EMA crosses above the SMA, it can indicate increasing upward momentum, and vice versa.

5-day EMA vs. 8-day EMA: Comparing these two EMAs can provide insights into very short-term momentum shifts.

Medium-Term Analysis:

**20-day SMA vs. 13-day EMA: Comparing a medium-term SMA with a slightly faster EMA can indicate potential trend changes. 
For instance, if the 13-day EMA crosses above the 20-day SMA, it could signify a bullish trend**

50-day SMA vs. 13-day EMA: When the faster 13-day EMA crosses the 50-day SMA, it can also indicate a change in the medium-term trend.

Confirmation:

20-day SMA vs. 50-day SMA: This is a classic comparison for trend confirmation. 
A "Golden Cross" occurs when the 20-day SMA (shorter-term) crosses above the 50-day SMA (longer-term), signaling a potential bullish trend. 
Conversely, a "Death Cross" occurs when the 20-day SMA crosses below the 50-day SMA, signaling a potential bearish trend.

General Guidelines:
Short-Term Crosses Long-Term: When a shorter-period moving average (whether SMA or EMA) crosses above a longer-period average, 
it's typically considered a bullish signal. When it crosses below, it's a bearish signal.

Multiple Crossovers: If you observe multiple crossovers around the same time 
(e.g., 5-day EMA crossing both the 20-day SMA and 50-day SMA), it can serve as a stronger confirmation of a trend change.

Price vs. Moving Averages: The position of the price concerning its moving averages can also provide insights. 
If the price is consistently above both the SMAs and EMAs, it's a strong bullish indicator and vice versa.

        '''
        self.label = ctk.CTkLabel(master=self.tab("SummaryS"))
        self.label.configure(text=txt)
        # on the grid, can pad on x or y direction
        self.label.grid(row=0, column=1, padx=20, pady=10)

        
        


# running the app
app = App('2021-01-01', pd.Timestamp.today().date())
app.mainloop()