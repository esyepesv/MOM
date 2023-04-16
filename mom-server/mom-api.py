from Queue import Queue 
from flask import Flask, jsonify, request, make_response
import grpc
import sys
sys.path.append('../')
import message_pb2
import message_pb2_grpc
import asyncio
import jsonpickle


queues = {}

#test colas:
q1 = Queue("cola1", "user1", "key1")
q2 = Queue("cola2", "user2", "key2")
queues[q1.get_name()] = q1
queues[q2.get_name()] = q2
queues["cola1"].queue.put("mensaje de prueba")
queues["cola1"].queue.put("mensaje 2 de prueba")
queues["cola1"].queue.put("mensaje 3 de prueba")

queues["cola2"].queue.put("mensaje de prueba 2")
queues["cola2"].queue.put("mensaje 2 de prueba 2")
queues["cola2"].queue.put("mensaje 3 de prueba 2")


app = Flask(__name__)

@app.route('/')
def home():
    return "MOM server implementation"


#metodos comunicacion con los servicios ----------------------------------------------------------------

@app.route('/getRequest', methods=['GET'])
def getRequest():
    if queues["cola1"].queue.empty():
        return make_response(jsonify({'message: empty'}), 204)
    else:
        queue_contents = []
        while not queues["cola1"].queue.empty():
            
            queue_contents.append(str(queues["cola1"].queue.get()))
        return make_response(jsonify({'queue_contents': queue_contents}), 200)




#metos de los servicios --------------------------------------------------------------------------------------------

#solicitar servicio 1
@app.route('/service/<service_number>', methods=['GET'])
def service(service_number):
    data = request.json
    name = data['queue_name']
    user = data['user']
    key = data['key']
    message = data['message']

    queue = queues[name]

    #verificar que existe la cola y se tiene acceso
    if name not in queues:
        return make_response(jsonify({'message': f'Queue {name} does not exist'}), 404)
    elif user != queue.get_user() or key != queue.get_key():
        return make_response(jsonify({'message': f'you do not have access to Queue {name}'}), 403)

    #encolar mensaje
    queue.queue.put(message)

    port_mappings = {
    '1': 'localhost:50052',
    '2': 'localhost:50053',
    }

    if service_number in port_mappings:
        send(queues[name], port_mappings[service_number])
    else:
        return make_response(jsonify({'message': f'Service {service_number} not found'}), 404)

    return jsonify({'message': f'{message} on queue'})


# respuesta servicios
@app.route('/getService', methods=['GET'])
def getService1():
    data = request.json
    name = data['queue_name']
    user = data['user']
    key = data['key']

    queue = queues[name]
    if user != queue.get_user() or key != queue.get_key():
        return make_response(jsonify({'message': f'you do not have access to Queue {name}'}), 403)

    if queues[name].queue.empty():
        return jsonify('not response')
    else:
        response = queues[name].queue.get()
        return jsonify(response)
# -----------------------------------------------------------------------------------------------


#enviar y recibir al servicio
def send(queue, puerto):

    if not queues[queue.get_name()].queue.empty():
        # 'localhost:50052'
        with grpc.insecure_channel(puerto) as channel:
            stub = message_pb2_grpc.MessageServiceStub(channel)
            message = queue.queue.get()
            response = stub.Greet(message_pb2.MessageRequest(name=message))
            queues[queue.get_name()].queue.put(response.greeting)



#CRUD colas --------------------------------------------------------------------------------------
@app.route('/getQueues', methods=['GET'])
def getQueues():
    response = []
    for q_name in queues.keys():
        response.append(q_name)
    
    return jsonify(response)

@app.route('/createQueue', methods=['POST'])
def createQueue():
    data = request.json
    queue_name = data['name']
    queue_user = data['user']
    queue_key = data['key']
    
    new_queue = Queue(queue_name, queue_user, queue_key)
    queues[queue_name] = new_queue
    
    return jsonify({'message': f'Queue {queue_name} created successfully!'})

@app.route('/updateQueue/<name>', methods=['PUT'])
def updateQueue(name):
    data = request.json
    if name in queues:
        queues[name].user = data['user']
        queues[name].key = data['key']
        return jsonify({'message': 'Queue updated successfully'})
    else:
        return jsonify({'error': 'Queue not found'})

@app.route('/deleteQueue/<name>', methods=['DELETE'])
def deleteQueue(name):
    queue = queues[name]
    if user != queue.get_user() or key != queue.get_key():
        return make_response(jsonify({'message': f'you do not have access to Queue {name}'}), 403)

    if name in queues:
        del queues[name]
        return jsonify({'message': 'Queue deleted successfully'})
    else:
        return jsonify({'error': 'Queue not found'})

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run()
