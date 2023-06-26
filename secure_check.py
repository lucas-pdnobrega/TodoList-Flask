from user import User
users = [User(1,'natinho','2309'),
         User(2,'lucas','2310')
         ]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and user.check_password(password):
        return user
    else:
        return {'user': None}, 403
    
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)