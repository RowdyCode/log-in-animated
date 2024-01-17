from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    if len(password) < 16:
        # Password is not long enough, redirect back to signup
        return redirect(url_for('index'))

    # Redirect to welcome with username in the URL
    return redirect(url_for('welcome_page', username=username))

@app.route('/welcome/<username>')
def welcome_page(username):
    return render_template('welcome.html', username=username)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
