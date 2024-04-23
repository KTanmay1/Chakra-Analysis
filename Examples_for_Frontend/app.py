from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_very_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

def analyze_chakras(answers):
    results = {}
    if answers.get('s1', 'No') == 'Yes':
        results['Root Chakra'] = 'Under-active'
    else:
        results['Root Chakra'] = 'Balanced'

    if answers.get('s2', 'No') == 'Yes':
        results['Sacral Chakra'] = 'Over-active'
    else:
        results['Sacral Chakra'] = 'Balanced'
    
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user is None:
            hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            flash('Username already exists')
    return render_template('register.html')

@app.route('/welcome')
def welcome():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('welcome_page.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/submit', methods=['POST'])
def submit():
    answers = request.form.to_dict()
    results = analyze_chakras(answers)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
