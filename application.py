from flask import Flask, render_template
from werkzeug.utils import redirect



application = Flask(__name__)

@application.route('/')
def main():
    return render_template('index.html')

@application.route('/learnmore', methods=['GET', 'POST'])
def learnmore():  
    return render_template('learnmore.html')

if __name__ == "__main__":
    application.run(debug=True) #turn debug off for prodcution deployment
