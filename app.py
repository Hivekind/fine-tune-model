from flask import Flask, request, jsonify
from sentiment import sentiment_analysis

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.json
    review = data.get('review')
    sentiment = sentiment_analysis(review)
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
