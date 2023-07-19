import jwt
import datetime
from models.models import Users
from models.models import Users, engine
from sqlalchemy.orm import sessionmaker

SECRET = "mUyBEcr5PMBXVe0JPDV7I3Exmxx8Yzwh0Gl650mH3vUoIS0k8zDrgPwVpF0XaRXZ"

Session = sessionmaker(bind=engine)

def authenticate(email, password):
    print(email, password)
    session = Session()
    user = session.query(Users).filter_by(email=email).first()
    
    if email == user.email and password == user.password:
        encoded = {'email': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
        token = jwt.encode(encoded, SECRET, algorithm='HS256')
        print(token)
        return token
    else:
        return None