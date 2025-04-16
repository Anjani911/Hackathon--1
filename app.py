from flask import Flask, render_template, request
import detector  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    url = request.form['url']
    result = detector.check_url(url)
    return render_template('index.html', input_url=url, result=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

def detect():
    url = request.form['url']
    result = detector.check_url(url)
    return render_template('index.html', input_url=url, result=result)

