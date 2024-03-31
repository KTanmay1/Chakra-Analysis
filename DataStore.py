from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Define your models
class Root(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    
class Sacral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)

class SolarPlexus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)

class Heart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)

class Throat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)

# Add similar models for Sacral, Solar Plexus, Heart, and Throat

@app.route('/store_answers', methods=['POST'])
def store_answers():
    data = request.get_json()  # Get the JSON data sent from the frontend

    # Convert 'yes' to 1 and 'no' to 0
    for key, value in data.items():
        if value.lower() == 'yes':
            data[key] = 1
        elif value.lower() == 'no':
            data[key] = 0

    # Create a new record with the data for each chakra
    root = Root(**data['root'])
    sacral = Sacral(**data['sacral'])
    solar_plexus = SolarPlexus(**data['solar_plexus'])
    heart = Heart(**data['heart'])
    throat = Throat(**data['throat'])

    # Add the new records to the session
    db.session.add(root)
    db.session.add(sacral)
    db.session.add(solar_plexus)
    db.session.add(heart)
    db.session.add(throat)

    # Commit the session and save the changes
    db.session.commit()

    return jsonify({'message': 'Data received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
