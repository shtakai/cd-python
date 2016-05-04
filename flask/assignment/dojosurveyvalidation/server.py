from flask import Flask, render_template, request, flash, session
app = Flask(__name__)
app.secret_key = "hgrefjndsj43u32"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=["POST"])
def dojo():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    print name, location, language, comment
    if len(name) < 1:
        #validation error
        flash("Name cannnot be blank")
    if len(comment) < 1:
        #validation error
        flash("Comment canntot be blank")
    if len(comment) > 120:
        flash("Comment is within 120 letters")
        #validation error
    return render_template(
        'result.html',
        name=name,
        location=location,
        language=language,
        comment=comment)


app.run(debug=True)
