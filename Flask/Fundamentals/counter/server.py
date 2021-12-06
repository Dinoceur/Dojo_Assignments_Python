from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "deez"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")

@app.post('/count')
def count():
    if request.form['click'] == 'left':
        session['count'] += 0
    elif request.form['click'] == 'right':
        session['count'] = 0
    return redirect('/')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)