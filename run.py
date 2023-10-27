from gui import App
import pandas as pd
import customtkinter as ctk
import pandas as pd 


# running the app
app = App('2023-01-01', pd.Timestamp.today().date(), inputsymbol='NVDA')
app.mainloop()