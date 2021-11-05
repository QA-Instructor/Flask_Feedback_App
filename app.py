from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/sky_engineer'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bea59ae666dc83:01993356@us-cdbr-east-04.cleardb.com/heroku_08c3e33a78be528'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # without this, get warnings in console
db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    engineer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, engineer, rating, comments):
        self.customer = customer
        self.engineer = engineer
        self.rating = rating
        self.comments = comments



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        engineer = request.form['engineer']
        rating = request.form['rating']
        comments = request.form['comments']
        print(customer, engineer, rating, comments)
        if customer == '' or engineer == '':
            return render_template('index.html', message="Please enter required fields")
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, engineer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, engineer, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message="You have already submitted feedback")


if __name__ == "__main__":
    app.run(debug=True)