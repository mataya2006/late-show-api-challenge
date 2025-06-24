from server.app import db

class Appearance(db.Model):
    __tablename__ = 'appearance'
    id = db.Column(db.Integer, primary_key=True) [cite: 6]
    rating = db.Column(db.Integer, nullable=False) [cite: 6]
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False) [cite: 6]
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False) [cite: 6]

    __table_args__ = (
        db.CheckConstraint('rating >= 1 AND rating <= 5', name='rating_range'),
    )

    def __repr__(self):
        return f'<Appearance Episode: {self.episode_id}, Guest: {self.guest_id}, Rating: {self.rating}>'