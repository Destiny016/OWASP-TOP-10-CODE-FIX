#Destiny Harris
# 04/20/2026
# 3-4 cryptographic failures


#Incorrect

return hashlib.sha1(password.encode()).hexdigest()

#Fixed

import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)