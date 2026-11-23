from flask import Flask, render_template_string
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql-db"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "root123"),
        database=os.getenv("MYSQL_DATABASE", "twotierdb")
    )

@app.route('/')
def home():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()

    cursor.close()
    connection.close()

    html = """
    <h1>Two-Tier Web Application</h1>
    <h2>Messages from MySQL Database</h2>

    {% for message in messages %}
        <p>{{ message[0] }} - {{ message[1] }}</p>
    {% endfor %}
    """

    return render_template_string(html, messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)