from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route("/")
def home():
    return render_template('test.html')

@app.route("/g-meet")
def red():
    return render_template('index.html')

@app.route("/test")
def blue():
    return render_template('try.html')

if __name__=="__main__":
    app.run(debug=True)