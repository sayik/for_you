from flask import Flask, redirect, render_template, session, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
if __name__ == "__main__":
    app.run()