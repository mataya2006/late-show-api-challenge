from server.app import db

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True) [cite: 5]
    name = db.Column(db.String(100), nullable=False) [cite: 5]
    occupation = db.Column(db.String(100), nullable=False) [cite: 5]


    appearances = db.relationship('Appearance', backref='guest', lazy=True) [cite: 5]

    def __repr__(self):
        return f'<Guest {self.name}>'