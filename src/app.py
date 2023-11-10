from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Cargar los datos desde el archivo JSON
    with open('./data/gpli.json', 'r') as f:
        data = json.load(f)
        
    return  render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

