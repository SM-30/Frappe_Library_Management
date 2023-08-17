import random, string
from flask import Flask, render_template, request, redirect

app = Flask(  __name__, template_folder='templates',  static_folder='static')

ok_chars = string.ascii_letters + string.digits


@app.route('/')  
def base_page(): 
  return render_template('base.html')   

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

@app.route('/return_book.html', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        days_issued = int(request.form['days_issued'])
        rent_fee = calculate_rent_fee(days_issued)
        return f"Book returned. Rent Fee: {rent_fee}"
    return render_template('return_book.html')

def calculate_rent_fee(days_issued):
    rent_fee = days_issued * 2
    return rent_fee
  
@app.route('/create_db.html')
def create_db():
  
# Define the SQLAlchemy database model
 Base = declarative_base()

 class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publication_year = Column(Integer)

 api_url = "https://frappe.io/api/method/frappe-library"

 response = requests.get(api_url)
 data = response.json()

 db_url = "sqlite:///library.db"
 engine = create_engine(db_url, echo=True)
 Base.metadata.create_all(engine)
 Session = sessionmaker(bind=engine)
 session = Session()

 for book_data in data.get("message", []):
    book = Book(
        title=book_data.get("title"),
        author=book_data.get("author"),
        publication_year=book_data.get("publication_year")
    )
    session.add(book)

 session.commit()
 session.close()
 return render_template('create_db.html')


if __name__ == "__main__":  
  app.run( host='0.0.0.0',  port=random.randint(2000, 9000))
