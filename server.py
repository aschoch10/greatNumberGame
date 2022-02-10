import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'super, super secret key name'


@app.route('/')
def home():
    if 'targetNumber' not in session:
        session ['targetNumber'] = random.randint(1,100)
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1

    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def guess():
    # print("Succesful post")
    # print("post info: ", request.form)
    if request.form['number'] == '':
        session['number'] = 0
    else:
        session['number'] = int(request.form['number'])
    target = session['targetNumber']
    print("Target number is:", target)
    session['count'] = 0
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
