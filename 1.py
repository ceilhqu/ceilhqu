from flask import Flask,render_template
import requests
import re
from bs4 import BeautifulStoneSoup,BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('hdxw.html')









#@app.route("/")
#def index():
#    return render_template('index.html')

#@app.route('/hdxw')
#def hdxw():
#        return render_template('hdxw.html')
#
    