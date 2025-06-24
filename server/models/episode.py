from server.app import db

class Episode(db.Model):
    __tablename__ = 'episode'
    id = db.Column(db.Integer, primary_key=True) [cite: 5]
    date = db.Column(db.Date, nullable=False) [cite: 5]
    number = db.Column(db.Integer, nullable=False) [cite: 5]

    appearances = db.relationship('Appearance', backref='episode', lazy=True, cascade='all, delete-orphan') [cite: 6]

    def __repr__(self):
        return f'<Episode {self.number} - {self.date}>'