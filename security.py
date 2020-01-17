from user import  User

users = { User(1,'sagar','testing')}

username_mapping = { u.name : u for u in users }

userid_mapping = { u.id : u for u in users}

def authenticate(name , passwd ):
    user = username_mapping.get(name,None)
    if user and user.passwd == passwd :
        return user 

def identity(payload):
    _id = payload['identity']
    return userid_mapping.get(_id,None)

