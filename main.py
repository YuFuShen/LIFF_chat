from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/first-connect")
def first_connect():
    return render_template('first-connect.html')

@app.route("/test")
def test():
    return render_template('test.html')

if __name__=="__main__":
    app.run(debug=True)