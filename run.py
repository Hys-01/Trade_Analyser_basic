from gui import App
import pandas as pd

start_date = '2023-01-01'
current_date = pd.Timestamp.today().date()

# TODO: make a better input system, like a previous popup that asks for symbol (and) date?
inputsymbol = input("symbol: ")  
# running the app
app = App(start_date, current_date, inputsymbol)

app.mainloop()