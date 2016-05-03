from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('static/index.html', phrase = "aaa",times=3)

@app.route('/ninjas', methods = ['GET'])
def ninjas():
    return render_template('static/ninjas.html')

@app.route('/dojos/new')
def dojos():
    return render_template('static/dojos.html')

app.run(debug=True)
