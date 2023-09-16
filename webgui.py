from flask import Flask, render_template 
from MovingAverage import MovingAverage
from gui import App
webgui = Flask(__name__, template_folder='.')  # initilalise the flask application

def load(): 
    return render_template('web.html')
if __name__ == "__main__":
    webgui.run() # run it

