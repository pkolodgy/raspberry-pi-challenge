import requests

from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<fruit>/pie')
def get_recipes(fruit):
    data = {'q': fruit+' pie'}
    r = requests.get("http://www.recipepuppy.com/api", params=data)
    recipes = r.json()['results']
    return render_template('show_recipes.html', recipes=recipes)

if __name__ == "__main__":
    app.run(threaded=True)
