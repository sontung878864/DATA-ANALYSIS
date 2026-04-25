from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/muc1')
def muc1():
    return render_template('muc1.html')

@app.route('/muc2')
def muc2():
    return render_template('muc2.html')

@app.route('/muc3')
def muc3():
    return render_template('muc3.html')

@app.route('/muc4')
def muc4():
    return render_template('muc4.html')

@app.route('/muc5')
def muc5():
    return render_template('muc5.html')

if __name__ == '__main__':
    app.run(debug=True)