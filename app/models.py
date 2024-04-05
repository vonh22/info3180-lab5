from . import db


class Movie(db.Model):

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    poster = db.Column(db.String(100))  
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())



    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

    
    def serialize(self):
        return {
            "message": "Movie Successfully added",
            "title": self.title,
            "poster": self.poster,
            "description": self.description
        }

    def __repr__(self):
        return '<User %r>' %  self.title
    
