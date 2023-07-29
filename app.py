from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Python-Flask project.'

@app.route('/calc', methods = ["GET"])
def math_operations():
    operator = request.json["operator"]
    num_1 = 1
    num_2 = 2

    if operator == "add":
        ans = num_1 + num_2
    elif operator ==  "sub":
        ans = num_1 - num_2
    elif operator ==  "mult":
        ans = num_1 * num_2
    elif operator ==  "div":
        ans = num_1 / num_2

if __name__ == '__main__':
    app.run(debug=True)

