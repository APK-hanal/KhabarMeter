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
def eco_results(file):
    data = load_results(file)
    return jsonify(data)

@app.route('/results/politics')
def pol_results(file):
    data = load_results(file)
    return jsonify(data)

if __name__ == "__main__":
    eco_results('data/eco_results.json')
    pol_results('data/pol_result.json')
    app.run(debug=True)
