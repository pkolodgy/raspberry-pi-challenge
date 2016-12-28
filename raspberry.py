import json, requests

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<fruit>/pie')
def get_recipe(fruit):
    data = {'q': fruit+' pie'}
    r = requests.get("http://www.recipepuppy.com/api", params=data)
    return app.response_class(r.content, content_type='application/json')

if __name__ == "__main__":
    app.run(threaded=True)
