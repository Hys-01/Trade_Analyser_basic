from flask import Flask, render_template 

webgui = Flask(__name__, template_folder='.')  # initilalise the flask application

@webgui.route('/')
def load(): 
    return render_template('web.html')
if __name__ == "__main__":
    webgui.run() # run it

