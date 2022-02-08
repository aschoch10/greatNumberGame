from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'super, super secreat'


@app.route('/')
def helloWorld():
    return 'Hello World!'


@app.route('/home')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
