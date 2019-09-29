import json

from flask import Flask, render_template, jsonify, url_for, request

# Idk how I need to import the check_class function from "models/img_scav.py"
from models.img_scav import check_class

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', my_string="Hello, world!")

@app.route("/check", methods = ['POST'])
# category_check is a string that can be either "MLH_table", "Courant_paint" or "No_class"
def validate(category_check):
    # You'll need to modify this part for the image (this is the imported function)
    pred = check_class('file')
    if pred == category_check:
        #Write some code for the validation
        return "Yay!"
    else:
        # Script for when it is wrong
        return "Oh, ño! Try again"


if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0", port=5000)