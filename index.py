from flask import Flask, session, request


app = Flask(__name__)

@app.route("/")
def index():
    return "<p> Hello, World!</p>"

@app.route('/hello')
def hello():
    return 'Hello, World'


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