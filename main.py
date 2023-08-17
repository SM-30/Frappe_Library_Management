import random, string
from flask import Flask, render_template

app = Flask(  __name__, template_folder='templates',  static_folder='static')

ok_chars = string.ascii_letters + string.digits


@app.route('/')  
def base_page():
  # random_num = random.randint(1, 100000)  
  return render_template('base.html')   
  # random_number=random_num)

@app.route('/add_book.html')
def add_book():
    return render_template('add_book.html')

@app.route('/search_book.html')
def search_book():
    return render_template('search_book.html')

@app.route('/issue_book.html')
def issue_book():
    return render_template('issue_book.html')

@app.route('/remove_book.html')
def remove_book():
    return render_template('remove_book.html')

if __name__ == "__main__":  
  app.run( host='0.0.0.0',  port=random.randint(2000, 9000))