# Destiny Harris
# 04/20/2026
# 7 insecure design

# Incorrect

@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form['email']
    new_password = request.form['new_password']
    user = User.query.filter_by(email=email).first()
    user.password = new_password
    db.session.commit()
    return 'Password reset'

# Fixed

@app.route('/reset-password', methods=['POST'])
def reset_password():
    token = request.form['token']
    new_password = request.form['new_password']

    user = User.verify_reset_token(token)

    if not user:
        return "Invalid or expired token", 400

    user.set_password(new_password)  # hashed internally
    db.session.commit()

    return "Password reset successful"