from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', "r") as file:
        items = json.load(file)
    if items.get('items'):
        return render_template('items.html',items=items['items'])
    else:
        return render_template('items.html')

if __name__ == '__main__':
    # app.run(debug=True,host= "0.0.0.0", port=80)
    app.run(debug=True, port=5000)
