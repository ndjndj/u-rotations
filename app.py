from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = "Hello World"

    return message

if __name__ == '__main__':
    app.run(debug=True)
