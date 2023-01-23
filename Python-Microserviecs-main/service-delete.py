from flask import Flask, request, jsonify
import datetime
import data_user as us

app = Flask(__name__)


@app.route('/detele', methods=['DELETE'])
def delete():
    # Get the user's login information from the request
    user = request.form.get('username')
    _user = us.find_username(user)
    if _user:
        us.delete_user(user)
        return jsonify({'message': 'User deleted successfully.'}), 200
    else:
        return jsonify({'message': 'User not found.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1