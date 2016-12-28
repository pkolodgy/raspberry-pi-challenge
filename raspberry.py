import requests
import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<fruit>/pie')
def get_recipes(fruit):
    data = {'q': fruit+' pie'}
    r = requests.get("http://www.recipepuppy.com/api", params=data)
    # response = app.response_class(r.content, content_type='application/json')
    parsed = r.json()['results']
    return render_template('show_recipes.html', results=parsed)

if __name__ == "__main__":
    app.run(threaded=True)
