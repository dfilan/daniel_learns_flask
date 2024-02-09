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
    if market_data is None:
        return render_template('no_market_found.html')
    elif market_data['outcomeType'] == 'BINARY':
        return render_template(
            'binary_market.html',
            question=market_data['question'],
            probability=round(market_data['probability'] * 100, 1),
            market_url=market_data['url'],
        )
    elif market_data['outcomeType'] == 'MULTIPLE_CHOICE':
        answers = map(lambda a: {'text': a['text'],
                                 'probability': round(a['probability'] * 100, 1)},
                      market_data['answers'])
        return render_template(
            'multiple_choice_market.html',
            question=market_data['question'],
            answers=list(answers),
            market_url=market_data['url'],
        )
    else:
        return render_template(
            'cant_handle_this.html',
            question=market_data['question'],
            market_type=market_data['outcomeType'],
            market_url=market_data['url'],
        )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
