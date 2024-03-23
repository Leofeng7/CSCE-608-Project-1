from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Dummy function to get user info from database
def get_user_by_id(user_id):
    conn = sqlite3.connect('../database.db')  # Connect to your SQLite DB
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = c.fetchone()
    conn.close()
    if user:
        return {"username": user[1], "email": user[2], "aboutme": user[3], "followers": user[5]}
    return None

@app.route('/get-user', methods=['GET'])
def get_user():
    user_id = request.args.get('userId')
    if not user_id:
        return jsonify({"error": "Missing user ID"}), 400
    
    user_info = get_user_by_id(user_id)
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
