from server.app import app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

def seed_data():
    with app.app_context():
        # Clear existing data
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()
        User.query.delete()

        # Create users
        user1 = User(username='admin')
        user1.set_password('password123')
        user2 = User(username='user1')
        user2.set_password('password123')

        db.session.add_all([user1, user2])

        # Create guests
        guest1 = Guest(name='John Doe', occupation='Comedian')
        guest2 = Guest(name='Jane Smith', occupation='Actor')
        guest3 = Guest(name='Bob Johnson', occupation='Musician')

        db.session.add_all([guest1, guest2, guest3])

        # Create episodes
        episode1 = Episode(date=date(2023, 1, 15), number=1)
        episode2 = Episode(date=date(2023, 1, 22), number=2)

        db.session.add_all([episode1, episode2])

        db.session.commit()

        # Create appearances
        appearance1 = Appearance(rating=4, guest_id=guest1.id, episode_id=episode1.id)
        appearance2 = Appearance(rating=5, guest_id=guest2.id, episode_id=episode1.id)
        appearance3 = Appearance(rating=3, guest_id=guest3.id, episode_id=episode2.id)

        db.session.add_all([appearance1, appearance2, appearance3])

        db.session.commit()
        print("Seed data added successfully.")

if __name__ == '__main__':
    seed_data()
