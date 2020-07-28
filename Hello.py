from flask import Flask, session, redirect, url_for, request, render_template
app = Flask(__name__)
app.secret_key = '007'

@app.route('/clear_session/')
def clear():
	for key, value in session.items():
		session.pop(key, None)
	return redirect(url_for('welcome'))	

@app.route('/initiate_session/')
def initiate():
	for key in ['Name', 'Age', 'Roll No', 'Class']:
		session[key]=[]
	return redirect(url_for('welcome'))	

@app.route('/students')
def index():
	total_records = len(session['Name'])
	return render_template('students/index.html', records = session, total_records = total_records)

@app.route('/students/create', methods=["POST"])
def create():
	data = request.form	
	for key, value in data.items():
   		session[key] = session[key]+[value] 
   	return redirect(url_for('index'))

@app.route('/students/new')
def new():
   return render_template('students/new.html')


@app.route('/')
def welcome():
   return render_template('welcome.html')



if __name__ == '__main__':
   app.run(debug = True)

