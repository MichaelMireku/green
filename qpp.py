from flask import Flask,
render_template, request, redirect,
url_for, session
from flask_sqlalchemy import
flask_sqlalchemy
from werkzeug.security import
generate_password_hash,
check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] =
'your-security-key' #Make secure key
app.config['SQLALCHEMY_DATABASE_URI']
secure key
app.config['SQLALCHEMY_DATABASE_URI']
='sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    username =
    db.Column(db.String(20), unique=True,
              nullable=False)
    password = 
    db.Column(db.String(60),
              nullable=False)
    
    @app.route('/')
    methods=['POST'])
    def register():
        username = 
        request.form.get('')
app= Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username =
    request.form.get('username')
    password = 
    request.form.get('password')

