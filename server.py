from flask import Flask, render_template, request
from waitress import serve

from market_info import get_market_info

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/market_info')
def get_market_info_server():
    search_text = request.args.get('market_search_text')
    market_data = get_market_info(search_text)
    # can have different templates for different market types
    return render_template(
        'market_info.html',
        question=market_data['question'],
        market_type=market_data['outcomeType'],
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
