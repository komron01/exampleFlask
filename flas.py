from flask import Flask, render_template,request
import psycopg2

app = Flask(__name__)

# Function to fetch data from the PostgreSQL table
def get_data_from_postgres():
    connection = psycopg2.connect(
        user="postgres",
        password="123",
        host="78.141.227.124",
        port="5432",
        database="postgres"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT stud_name, passwords FROM students")  # Replace 'your_table_name' with your actual table name
    data = cursor.fetchall()
    formatted_data = {row[0]: row[1] for row in data}

    cursor.close()
    connection.close()

    return formatted_data

# Route for the Home Page
@app.route('/')
def home():
    # Fetch data from PostgreSQL
    postgres_data = get_data_from_postgres()
    
    # Pass data to the template
    return render_template('home.html', postgres_data=postgres_data)
@app.route('/registration', methods=['GET'])
def registration():
    return render_template('reg.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Add your authorization logic here (e.g., check username and password against database)
    users = get_data_from_postgres()
    print(f"Username or Email: {username}, Password: {password}", flush=True)

    if username in users:
        if users[username] == password:
            return render_template('welcome.html')
        else:
            error_message = "Incorrect password. Please try again."
            return render_template('reg.html', error_message=error_message)
    else:
        error_message = "User not found. Please check your username and try again."
        return render_template('reg.html', error_message=error_message)



# @app.route('/welcome')
# def welcome():
#     return render_template('welcome.html')
if __name__ == '__main__':
    app.run(debug=True)
