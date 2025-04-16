from flask import Flask, render_template, request, jsonify
from detector import is_phishing

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    url = data['url']
    result = is_phishing(url)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
