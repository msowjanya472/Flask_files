#from flask import Flask
#app = Flask(__name__)
#
#@app.route("/")
#def home():
#    return{"message": "Hi from docker Flask."}
#
#
#
#if __name__ == "__main__":
#    app.run(host="0.0.0.0", debug=True)
#

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Docker! from kritiksha....."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
