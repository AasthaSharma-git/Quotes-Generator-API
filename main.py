from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

# Load quotes from CSV file
quotes_df = pd.read_csv('quotes.csv')

# API endpoint to get all quotes or filter by category/author
@app.route('/quotes', methods=['GET'])
def get_quotes():
    category = request.args.get('category')
    author = request.args.get('author')

    filtered_quotes = quotes_df

    if category:
        # Perform case-insensitive filtering while keeping the original case
        filtered_quotes = filtered_quotes[filtered_quotes['category'].str.lower() == category.lower()]

    if author:
        # Perform case-insensitive filtering while keeping the original case
        filtered_quotes = filtered_quotes[filtered_quotes['author'].str.lower() == author.lower()]

    return jsonify(filtered_quotes.to_dict(orient='records'))

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    workers = int(os.getenv('WEB_CONCURRENCY', 1))
    app.run(host=host, port=port, debug=False, threaded=True)
