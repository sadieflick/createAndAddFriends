from flask import Flask, render_template, redirect, session, request
# import the function connectToMySQL from the file mysqlconnection.py
from mySQLconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('createAndReadFriends')
# now, we may invoke the query_db method
#print("all the users", mysql.query_db("SELECT * FROM friends;"))

@app.route('/')
def index():
    all_friends = mysql.query_db("SELECT * FROM friends")
    print("Fetched all friends", all_friends)
    return render_template('index.html', friends = all_friends)

@app.route('/create_friend', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, age, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"
    
    nameList = request.form['name'].split()
    first = nameList[0]
    last = nameList[1]

    data = {
             'first_name': first,
             'last_name':  last,
             'age': request.form['age']
           }

    mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
