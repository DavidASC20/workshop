# Fabulous Frogs: David Chong (with Fluff), Wen Hao Dong (with Jal Hordan), and Austin Ngan (with Gerald)
# SoftDev
# 2021-10-04

from flask import Flask, render_template
app = Flask(__name__) 

@app.route("/") 
def hello_world():
    return render_template('model_tmplt.html')


if __name__ == "__main__":  
    app.debug = True
    app.run()  

