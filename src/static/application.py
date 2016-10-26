from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('cwtemplate1.html'), 200

@app.route('/home/')
def home():
  return render_template('cwtemplate1.html'), 200


@app.route('/login/' , methods=['GET' , 'POST'])
def login():
  if request.method == 'POST':
    print request.form
    username = request.form['username']
    password = request.form['password']
    return redirect(url_for('home'))
  else:
    return render_template('login.html')

@app.route('/movies/')
def movies():
  return render_template('movies.html')

@app.route('/about/')
def about():
  return render_template('about.html'), 200

@app.route('/contact/')
def contact():
  return render_template('contact.html'), 200

@app.route('/movies/scarface/')
def scarface():
  return render_template('scarface.html'), 200

@app.route('/movies/The Godfather/')
def thegodfather():
  return render_template('thegodfather.html'), 200

@app.route('/movies/movie3/')
def reservoirdogs():
  return render_template('reservoirdogs.html'), 200

@app.route('/movies/Pulp Fiction/')
def pulpfiction():
  return render_template('pulpfiction.html'), 200

@app.route('/movies/Fight Club/')
def fightclub():
  return render_template('fightclub.html'), 200

@app.route('/force404')
def force404():
  abort(404)
  
@app.errorhandler(404)
def page_not_found(error):
  return "The page you requested doesn't exist.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
