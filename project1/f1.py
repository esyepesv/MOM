from flask import Flask, jsonify, request
import multiprocessing as mp

app = Flask(__name__)
manager = mp.Manager()
shared_list = manager.list()  # creamos una lista compartida

@app.route('/get_people', methods=['GET'])
def get_people():
    return jsonify({'people': list(shared_list)})


if __name__ == '__main__':
    app.run(port=4001, debug=True)
