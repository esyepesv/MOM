from flask import Flask, jsonify, request
from f1 import shared_list

app = Flask(__name__)

@app.route('/add_person', methods=['POST'])
def add_person():
    data = request.get_json()
    name = data['name']
    age = data['age']
    shared_list.append({'name': name, 'age': age})
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(port=4002, debug=True)
