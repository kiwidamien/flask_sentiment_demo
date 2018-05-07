from flask import Flask, make_response, request, abort, jsonify, render_template
from api import make_soft_prediction

app = Flask(__name__)
app.debug = True

@app.route('/sentiment_score', methods=['POST'])
def get_sentiment_score():
    if not request.json or ('review' not in request.json):
        abort(400)

    review = request.json['review']

    score = make_soft_prediction(review)

    response = {
        'review': review,
        'score': score
    }

    return jsonify(response), 201

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fancy')
def styled_page():
    return render_template('home_with_styling.html')
    
if __name__ == '__main__':
    app.run()
