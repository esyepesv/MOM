from flask import Flask, request, jsonify
from file import create_username, create_queue, update_queue, delete_queue, get_queue, add_message, get_messages_user

app = Flask(__name__)

@app.route('/create-user', methods=['POST'])
def create_user():
    # Validate if exists get_json
    if not request.is_json:
        return jsonify({'message': 'Missing JSON in request'}), 400
    data = request.get_json()

    # If username not exists
    if 'username' not in data:
        return jsonify({'message': 'Missing username parameter'}), 400 
    username = data.get('username')

    # Create user
    res = create_username(username)

    # Return res
    return jsonify(res)

@app.route('/create-queue', methods=['POST'])
def create_queue_fl():
    # Validate if exists get_json
    if not request.is_json:
        return jsonify({'message': 'Missing JSON in request'}), 400
    data = request.get_json()

    # If username not exists
    if 'username' not in data:
        return jsonify({'message': 'Missing username parameter'}), 400 
    username = data.get('username')

    # If queue_name not exists
    if 'queue_name' not in data:
        return jsonify({'message': 'Missing queue_name parameter'}), 400 
    queue_name = data.get('queue_name')

    # If api_key not exists
    if 'api_key' not in data:
        return jsonify({'message': 'Missing api_key parameter'}), 400 
    api_key = data.get('api_key')

    # Create queue
    res = create_queue(username, queue_name, api_key)

    # Return res
    return jsonify(res)

@app.route('/update-queue', methods=['PUT'])
def update_queue_fl():
    # Validate if exists get_json
    if not request.is_json:
        return jsonify({'message': 'Missing JSON in request'}), 400
    data = request.get_json()

    # If username not exists
    if 'username' not in data:
        return jsonify({'message': 'Missing username parameter'}), 400 
    username = data.get('username')

    # If queue_name not exists
    if 'queue_name' not in data:
        return jsonify({'message': 'Missing queue_name parameter'}), 400 
    queue_name = data.get('queue_name')

    # If api_key not exists
    if 'api_key' not in data:
        return jsonify({'message': 'Missing api_key parameter'}), 400 
    api_key = data.get('api_key')

    # If new_queue_name or new_api_key not exists
    if 'new_queue_name' not in data and 'new_api_key' not in data:
        return jsonify({'message': 'Missing new_queue_name or new_api_key parameter'}), 400
    
    new_queue_name = data.get('new_queue_name')
    new_api_key = data.get('new_api_key')

    res = update_queue(username, queue_name, new_queue_name, api_key, new_api_key)

    return jsonify(res), 201

@app.route('/delete-queue', methods=['DELETE'])
def delete_queue_fl():
    # Validate if exists get_json
    if not request.is_json:
        return jsonify({'message': 'Missing JSON in request'}), 400
    data = request.get_json()

    # If username not exists
    if 'username' not in data:
        return jsonify({'message': 'Missing username parameter'}), 400 
    username = data.get('username')

    # If queue_name not exists
    if 'queue_name' not in data:
        return jsonify({'message': 'Missing queue_name parameter'}), 400 
    queue_name = data.get('queue_name')

    # If api_key not exists
    if 'api_key' not in data:
        return jsonify({'message': 'Missing api_key parameter'}), 400 
    api_key = data.get('api_key')

    res = delete_queue(username, queue_name, api_key)

    return jsonify(res), 201

@app.route('/get-queues', methods=['GET'])
def get_queue_fl():
    # Validate if exists get_json
    if not request.is_json:
        return jsonify({'message': 'Missing JSON in request'}), 400
    data = request.get_json()

    # If username not exists
    if 'username' not in data:
        return jsonify({'message': 'Missing username parameter'}), 400 
    username = data.get('username')

    res = get_queue(username)

    return jsonify(res), 201

@app.route('/add-message', methods=['POST'])
def add_message_fl():
    # Validate if exists get_json
    if not request.is_json:
        return jsonify({'message': 'Missing JSON in request'}), 400
    data = request.get_json()

    # If username not exists
    if 'username' not in data:
        return jsonify({'message': 'Missing username parameter'}), 400 
    username = data.get('username')

    # If queue_name not exists
    if 'queue_name' not in data:
        return jsonify({'message': 'Missing queue_name parameter'}), 400 
    queue_name = data.get('queue_name')

    # If api_key not exists
    if 'api_key' not in data:
        return jsonify({'message': 'Missing api_key parameter'}), 400 
    api_key = data.get('api_key')

    # If message not exists
    if 'service' not in data:
        return jsonify({'message': 'Missing service parameter'}), 400 
    service = data.get('service')

    res = add_message(username, queue_name, api_key, int(service))

    return jsonify(res), 201

@app.route('/get-messages-user', methods=['GET'])
def get_messages_user_fl():
    # Validate if exists get_json
    if not request.is_json:
        return jsonify({'message': 'Missing JSON in request'}), 400
    data = request.get_json()

    # If username not exists
    if 'username' not in data:
        return jsonify({'message': 'Missing username parameter'}), 400 
    username = data.get('username')

    # If queue_name not exists
    if 'queue_name' not in data:
        return jsonify({'message': 'Missing queue_name parameter'}), 400 
    queue_name = data.get('queue_name')

    # If api_key not exists
    if 'api_key' not in data:
        return jsonify({'message': 'Missing api_key parameter'}), 400 
    api_key = data.get('api_key')

    res = get_messages_user(username, queue_name, api_key)

    return jsonify(res), 201

if __name__ == '__main__':
    app.debug = True
    app.run(port=4000)
