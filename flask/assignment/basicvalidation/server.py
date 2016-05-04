from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "Killemall"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    # TODO: Tix error ups when Japanese letters input
    ''' do some validations here  '''
    if len(request.form['name']) < 1:
        # display valodation errors
        # just pass a string to the flash function
        flash("Name cannot be empty!")
        pass
    else:
        # display success message
        # just pass a string to the flash function
        flash("Success! Your name is {}".format(
            request.form['name'])
        )
    # either way the application sould return to
    #   the index and display the name
    return redirect('/')


app.run(debug=True)
