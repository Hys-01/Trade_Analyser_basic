from gui import App
import pandas as pd

start_date = '2023-01-01'
current_date = pd.Timestamp.today().date()
inputsymbol = 'NVDA'
# running the app
app = App(start_date, current_date, inputsymbol)

app.mainloop()