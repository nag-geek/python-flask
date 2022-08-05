from flask import Flask
import os

app = Flask(__name__)

LICENSE = os.environ.get("LICENSE_KEY")

@app.route('/')
def hello_world():
    return LICENSE

if __name__ == '__main__' and LICENSE!=None:
    app.run(host="0.0.0.0", port=8096, debug=True)