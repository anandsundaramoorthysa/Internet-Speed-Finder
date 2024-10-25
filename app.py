from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def speedtest_route():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    results = st.results.dict()
    return jsonify({
        'download': round(results['download'] / 1_000_000, 2),  
        'upload': round(results['upload'] / 1_000_000, 2),     
        'ping': results['ping']
    })

if __name__ == '__main__':
    app.run(debug=True)
