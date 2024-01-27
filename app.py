from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd
from bs4 import BeautifulSoup

app = Flask(__name__)

# Load dark patterns dataset from external CSV file
dark_pattern_dataset = pd.read_csv('dark.csv')['text'].tolist()

def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as errh:
        return None
    except requests.exceptions.ConnectionError as errc:
        return None
    except requests.exceptions.RequestException as err:
        return None

def check_for_dark_patterns(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    found_dark_patterns = []

    for pattern in dark_pattern_dataset:
        if pattern.lower() in soup.get_text().lower():
            found_dark_patterns.append(pattern)

    return found_dark_patterns

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check_dark_patterns():
    url = request.args.get('url')
    html_content = get_html_content(url)

    if html_content:
        detected_patterns = check_for_dark_patterns(html_content)
        return jsonify({'detectedPatterns': detected_patterns, 'error': None})
    else:
        return jsonify({'detectedPatterns': [], 'error': 'Failed to fetch content from the provided URL'})

if __name__ == '__main__':
    app.run(debug=True)
