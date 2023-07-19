from flask import Flask, request, jsonify, send_file
from models.models import Users, Posts, Snippets, engine
from sqlalchemy.orm import sessionmaker
import jwt
import os
from auth.auth import authenticate

from werkzeug.utils import secure_filename

from posts.posts import post_api, post_create_api, posts_detail_api, posts_update_api, post_delete_api, post_search_api, post_images_api
from snippets.snippets import snippets_api, snippet_create_api, snippets_detail_api, snippet_delete_api, snippets_update_api, snippet_images_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')
Session = sessionmaker(bind=engine)
session = Session()

key = '9eZ0fC3OhUaJvFATR7ifw6m2THrfC1dYfoQIWGK66i9JC9osWPKHZTRRY186kiy8'

token = 'CU7e0R8wJ7qVA03496t0VWK9TESOuHBbd78ID57kVbJHg0AITwWzUXxXlKv9q3bF'


@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return jsonify({'message': 'Invalid content type'}), 400

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400
    
    session = Session()
    user = session.query(Users).filter_by(email=email).first()
    if user:
        return jsonify({'message': 'User already exists'}), 400
    
    encoded = jwt.encode({'password': password}, key, algorithm='HS256')
    
    new_user = Users(email=email, password=encoded)
    session.add(new_user)
    session.commit()
    
    return jsonify({'message': 'User created successfully', 'token': token}), 201


authKey = []


@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    print(email, password)
    
    # content_type = request.headers.get('Authorization') # test için gecici yorum satırı yapıldı
    # if content_type != token:
    #     return jsonify({'message': 'Invalid content type'}), 400
    
    session = Session()
    user = session.query(Users).filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'Invalid email or password'}), 401

    decoded = jwt.decode(user.password, key, algorithms=['HS256'])

    if email != user.email or password != decoded['password']:
        return jsonify({'message': 'Invalid email or password'}), 401
    
    auth = authenticate(email, user.password)
    authKey.append(auth)
    print('authKey', authKey[0])
    
    return jsonify({'message': 'User logged in successfully', 'info': True}), 200


app.register_blueprint(post_create_api)

app.register_blueprint(post_api)

app.register_blueprint(posts_detail_api)

app.register_blueprint(posts_update_api)

app.register_blueprint(post_delete_api)

app.register_blueprint(post_search_api)

app.register_blueprint(post_images_api)

##########################################

app.register_blueprint(snippet_create_api)

app.register_blueprint(snippets_api)

app.register_blueprint(snippets_detail_api)

app.register_blueprint(snippets_update_api)

app.register_blueprint(snippet_delete_api)

app.register_blueprint(snippet_images_api)


if __name__ == "__main__":
    app.run(debug=True, host='localhost')