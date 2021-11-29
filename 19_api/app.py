from ssl import DefaultVerifyPaths


# Knoteem, David Chong and Shadman Rakib
# Soft Dev 
# k19 - Rest API work
# 2020-11-23

from flask import Flask
from flask import render_template
import json
import urllib.request
app = Flask(__name__)

@app.route("/")
def hello_world():
    try:
        with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=D76sPHfRJGz62GBjoCPa0Vtbogjvk6COr2lVShQS') as response:
            unparsed = response.read()
            data = json.loads(unparsed);
            return render_template('main.html', data = data);
    except:
        return "Error"


if(__name__ == "__main__"):
    app.debug = True
    app.run()
