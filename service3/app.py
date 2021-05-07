from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Service 3'
    
    
if __name__ == '__main__':
    # app.run(debug=True, port=5001)
    app.run(debug=True, host='0.0.0.0', port=5003)