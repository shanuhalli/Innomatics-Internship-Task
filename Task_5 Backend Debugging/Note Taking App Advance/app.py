from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///note.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/", methods=['GET', 'POST'])
def home():
        if request.method=='POST':
            title = request.form['title']
            desc = request.form['desc']
            note = Note(title=title, desc=desc)
            db.session.add(note)
            db.session.commit()
        
        allNote = Note.query.all()
        return render_template('index.html', allNote=allNote)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        note = Note.query.filter_by(sno=sno).first()
        note.title = title
        note.desc = desc
        db.session.add(note)
        db.session.commit()
        return redirect("/")
        
    tonote = Note.query.filter_by(sno=sno).first()
    return render_template('update.html', note=tonote)

@app.route('/delete/<int:sno>')
def delete(sno):
    note = Note.query.filter_by(sno=sno).first()
    db.session.delete(note)
    db.session.commit()
    return redirect("/")

@app.route('/about')
def about():
     return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)