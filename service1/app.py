from flask import Flask, render_template

import requests


app = Flask(__name__)


@app.route('/')
def hello_world():

    service_2_content = requests.get('http://service_a_envoy:8788/').content

    return f'Hello from Service 1; Service 2 said {service_2_content}'
    
    
if __name__ == '__main__':
    # app.run(debug=True, port=5001)
    app.run(debug=True, host='0.0.0.0', port=5001)