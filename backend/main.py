from flask import Flask, jsonify, request 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return "helo"

if __name__ == '__main__':
    app.run(debug=True)