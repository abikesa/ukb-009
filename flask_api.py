
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja2')

@app.route('/simulate')
def simulate():
    donor = request.args.get("donor")
    recipient = request.args.get("recipient")
    fairness_score = 0.85
    return jsonify({
        "donor": donor,
        "recipient": recipient,
        "fairness_score": fairness_score,
        "valid": fairness_score > 0.7
    })

if __name__ == '__main__':
    app.run(debug=True)
