import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
#   password="yourpassword",
  database="items"
)
cursor = db.cursor()

# Home page
@app.route('/')
def home():
  return render_template('home.html')

# Display items page
@app.route('/items')
def items():
  cursor.execute("SELECT * FROM items")
  items = cursor.fetchall()
  return render_template('items.html', items=items) 

# Add new item  
@app.route('/new_item', methods=['POST'])
def new_item():
  name = request.form['name']
  cursor.execute("INSERT INTO items (name) VALUES (%s)", (name,))
  db.commit()
  return redirect(url_for('items'))

if __name__ == '__main__':
  app.run(debug=True)