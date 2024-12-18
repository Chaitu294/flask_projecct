from flask import Flask,render_template, request, redirect, url_for, flash, abort
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

db_config = {
    'host': 'localhost', 
    'user': 'root',      
    'password': 'Chaitanya@1918',  
    'database': 'users'  
}


@app.route('/users')
def users():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)  
        cursor.execute("SELECT * FROM users")
        users_list = cursor.fetchall()  
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return render_template('users.html', users=users_list)


@app.route('/new_user', methods=['GET', 'POST'] )
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']


        if not name or not email:
            flash("Name and Email are required!", "error")
            return render_template('new_user.html')

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
            connection.commit()
            cursor.close()
            connection.close()
            
            flash("User added successfully!", "success")
            return redirect(url_for('users')) 

        except mysql.connector.Error as err:
            flash(f"Error: {err}", "error")
            return render_template('new_user.html')

    return render_template('new_user.html')

@app.route('/users/<int:id>')
def user_details(id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if user is None:
        flash("User not found!", "error")
        return redirect(url_for('users'))

    return render_template('user_details.html', user=user)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def home():
    return "Welcome to the Flask API!"

if __name__ == '__main__':
    app.run(debug=True)
