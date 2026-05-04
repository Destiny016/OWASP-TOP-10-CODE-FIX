#Destiny Harris
# 04/20/2026
# 1-2 broken access control

#Incorrect 

@app.route('/account/<user_id>')
def get_account(user_id):
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict()) 

# Fixed

@app.route('/account/<user_id>')
@login_required
def get_account(user_id):
    if str(current_user.id) != user_id:
        return jsonify({"error": "Forbidden"}), 403

    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())   