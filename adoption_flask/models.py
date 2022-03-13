import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
db = SQLAlchemy(app)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('Name', db.String())
    age = db.Column('Age', db.String())
    breed = db.Column('Bread', db.String())
    color = db.Column('Color', db.String())
    size = db.Column('Size', db.String())
    weight = db.Column('Weight', db.String())
    url = db.Column('URL', db.String())
    url_tag = db.Column('Alt Tag', db.String())
    pet_type = db.Column('Type', db.String())
    gender = db.Column('Gender', db.String())
    spay = db.Column('Spay', db.String())
    house_train = db.Column('Housetrained', db.String())
    description = db.Column('Description', db.Text)

    def __repr__(self):
        return f'''<Pet (Name: {self.name}
                Age: {self.age}
                Breed: {self.breed}
                Color: {self.color}
                Size: {self.size}
                Weight: {self.weight}
                URL: {self.url}
                Tag: {self.url_tag}
                Pet Type: {self.pet_type}
                Gender: {self.gender}
                Spay/Neuter: {self.spay}
                Housetrained: {self.house_train}
                Description: {self.description})>'''
