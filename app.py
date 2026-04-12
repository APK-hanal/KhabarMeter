from flask import Flask, render_template, jsonify
import json 

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

def load_results(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/results/economy')
def eco_results():
    data = load_results('data/eco_results.json')
    return jsonify(data)

@app.route('/results/politics')
def pol_results():
    data = load_results('data/pol_result.json')
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
