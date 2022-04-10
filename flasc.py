
from speak import SpeakText
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from chat import get_response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///chat.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Messages(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(200), nullable=False)
    res = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.date}-{self.msg}-{self.msg}"


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ask = request.form['msg']
        response = get_response(request.form['msg'])
        SpeakText(response)
        conv = Messages(msg=ask, res=response)

        db.session.add(conv)
        db.session.commit()
    
    result = Messages.query.all()
    return render_template("index.html", result=result)


@app.route('/delete', methods=['GET','POST'])
def clear():
    cht = Messages.query.all()
    if request.method == 'POST':
        
        for i in cht:
            db.session.delete(i)
            db.session.commit()
    
    return render_template("index.html", result=cht)


if __name__ == '__main__':
    app.run(debug=True)
