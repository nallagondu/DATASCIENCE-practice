from flask import FLask
app = Flask(__name__)

@app.route('/')
def home():
    return 'This is my Flask APP'

if __name__ == "__main__":
    app.run(debug=true)