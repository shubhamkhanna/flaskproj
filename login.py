from flask import Flask, session, flash, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.secret_key = '9111'


db = SQLAlchemy(app)
class User(db.Model):
	id = db.Column('user_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(50))  
	phone = db.Column(db.Integer)
	password = db.Column(db.String(200))


	def __init__(self, name, email, phone, password):
	   self.name = name
	   self.email = email
	   self.phone = phone
	   self.password = password

@app.route('/users/index', methods = ['GET'])
def index():
   	return render_template('users/index.html', users = User.query.all())


@app.route('/users/new', methods = ['GET'])
def new():
   	return render_template('users/new.html')


@app.route('/users/create', methods = ['POST'])
def create():
	if not request.form['name'] or not request.form['email'] or not request.form['phone']:
		flash('Please enter all the fields', 'error')
	else:
		user = User(request.form['name'], request.form['email'],
		request.form['phone'], request.form['password'])
     
		db.session.add(user)
		db.session.commit()
		flash('Record was successfully added')
	return redirect(url_for('index'))

@app.route('/login', methods=['GET','POST'])
def login():	
	if request.method == 'GET':
   		return render_template('login.html')
   	else:
		if not request.form['email'] or not request.form['password']:
			flash('Please enter valid credentials!')
	   		return render_template('login.html')
	   	else:
	   		q = User.query.filter(User.email == request.form['email'], User.password == request.form['password'])
			if(len(q.all())):
				session['email'] = request.form['email']
				flash('Logged in successfully!')
	   			return redirect(url_for('index'))	 	
	   		else:
	   			flash('Invalid Credentials...', 'error')
	   			return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('email', None)
	return redirect(url_for('home'))
   				
@app.route('/')
def home():
	if(not 'email' in session.keys() or session['email'] == ''):
   		return redirect(url_for('login')) 
   	else:	
   		return render_template('users/index.html', users = User.query.all())	
   		
if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)


