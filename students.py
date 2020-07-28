from Hello import app

@app.route('/students/new')
def new():
   return render_template('students/new.html')
   #return 'welcome %s' % name
