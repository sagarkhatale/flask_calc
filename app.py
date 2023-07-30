from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Python-Flask project.'

@app.route('/calc', methods = ["GET"])
def math_operations():
    operator = request.json["operator"]
    num_1 = request.json["num_1"]
    num_2 = request.json["num_2"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

    if operator == "add":
        ans = int(num_1) + int(num_2)
    elif operator ==  "sub":
        ans = int(num_1) - int(num_2)
    elif operator ==  "mult":
        ans = int(num_1) * int(num_2)
    elif operator ==  "div":
        ans = int(num_1) / int(num_2)

    return f'Operation is {operator} and Answer is {ans}'


if __name__ == '__main__':
    app.run(debug=True)

