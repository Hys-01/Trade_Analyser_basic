from flask import Flask, render_template 
from MovingAverage import MovingAverage
from gui import App
webgui = Flask(__name__)  # initilalise the flask application


if __name__ == "__main__":
    webgui.run() # run it

