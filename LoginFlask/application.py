# Requirements
from flask import Flask, redirect, url_for, request, render_template
import helper


app = Flask(__name__)
app.logged_user = None

# Index route
@app.route('/')
# Index route with username defined
@app.route('/<string:name>')
def index(name = None):
  return render_template('index.html', name = name)
  
# Login Route( Post Method )
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if helper.valid_login(
                      request.form['username'],
                      request.form['password']
                      ):
          
          helper.log_the_user_in(request.form['username'])
          return redirect(url_for('index', name = request.form['username']))
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

# Change route ( Put Method )
@app.route('/change', methods=['PUT', 'GET'])
def change():

    error = None

    if request.method == 'PUT':
        app.logged_user = request.form['username']
        return app.logged_user

    return render_template('change.html')

# Delete Route ( Delete Method )
@app.route('/delete', methods=['DELETE', 'GET'])
def delete():
    if request.method == 'DELETE':
        return "Success"
    
    print ('GET req args', request.args.get('username'))
    return render_template('delete.html', username = request.args.get('username'))

# Deleted Route ( After the deletion process )
@app.route('/deleted', methods=['GET'])
def deleted():
    return render_template('deleted.html')
    
    
if __name__ == '__main__':
   app.run(debug = True)