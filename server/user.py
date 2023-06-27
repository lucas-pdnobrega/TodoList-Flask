from werkzeug.security import generate_password_hash, check_password_hash

class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password_hash = generate_password_hash(password)

    def __str__(self):
        return f'User id : {self.id}, username : {self.username}'
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)