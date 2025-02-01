from flask import Flask,jsonify
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency,out_currency,in_amount):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={in_amount}"
    content = requests.get(url).text #this gives the source code of the entire page
    soup = BeautifulSoup(content, 'html.parser')
    rate=soup.find("span",class_="ccOutputRslt").get_text()
    rate = rate[:-4]
    rate = float(rate.replace(",",""))
    return rate


app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency rate API</h1> <p>Example URL:/api/v1/usd-eur-10</p>'

@app.route('/api/v1/<in_cur>-<out_cur>-<amt>')
def api(in_cur,out_cur,amt):
    rate = get_currency(in_cur,out_cur,amt)
    result_dict = {'input':in_cur,'output':out_cur,'amount':f'{amt} {in_cur}','Exchange':f'{rate} {out_cur}'}
    return jsonify(result_dict)

app.run()