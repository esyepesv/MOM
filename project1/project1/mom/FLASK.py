from flask import Flask, jsonify, request
import shared_memory as shared_memory
import multiprocessing

app = Flask(__name__)

# definimos los datos compartidos
shared_data = {
    'service1': [],
    'queues': {}
}

# definimos una ruta para obtener los datos compartidos
@app.route('/shared_data', methods=['GET'])
def get_shared_data():
    print("From get shared data")
    print(shared_memory.service1_shared_list)
    shared_memory.service1_shared_list.append({'id': 3, 'name': 'Juan Pablo'})
    p1 = multiprocessing.Process(target=shared_memory.modify_service1_shared_list, args=(shared_memory.service1_shared_list,))
    p1.start()
    p1.join()
    return jsonify(shared_data)

# definimos una ruta para agregar datos a service1
@app.route('/service1', methods=['POST'])
def add_to_service1():
    data = request.json
    shared_data['service1'].append(data)
    return jsonify({'message': 'Data added to service1'})

# definimos una ruta para agregar datos a queues
@app.route('/queues', methods=['POST'])
def add_to_queues():
    data = request.json
    queue_name = data['queue_name']
    if queue_name not in shared_data['queues']:
        shared_data['queues'][queue_name] = []
    shared_data['queues'][queue_name].append(data['data'])
    return jsonify({'message': 'Data added to queue'})

if __name__ == '__main__':
    app.run()
