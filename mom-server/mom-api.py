from Queue import Queue 
from flask import Flask, jsonify, request
import grpc
import sys
sys.path.append('../')
import message_pb2
import message_pb2_grpc
import asyncio


queues = {}

#test colas:
q1 = Queue("cola1", "user1", "key1")
q2 = Queue("cola2", "user2", "key2")
queues[q1.get_name()] = q1
queues[q2.get_name()] = q2
#queues["cola1"].queue.put("mensaje de prueba")


app = Flask(__name__)

@app.route('/')
def home():
    return "MOM server implementation"

#metos de los servicios --------------------------------------------------------------------------------------------

#solicitar servicio 1
@app.route('/service1', methods=['GET'])
def service1():
    data = request.json
    name = data['queue_name']
    user = data['user']
    key = data['key']
    message = data['message']

    if name not in queues:
        return jsonify({'message': f'Queue {name} does not exist'})
    
    queues[name].queue.put(message)
    send(queues[name])
    return jsonify({'message': f'{message} on queue'})

# respuesta servicio 1
@app.route('/getService1', methods=['GET'])
def getService1():
    data = request.json
    name = data['queue_name']
    user = data['user']
    key = data['key']

    if queues[name].queue.empty():
        return jsonify('not response')
    else:
        response = queues[name].queue.get()
        return jsonify(response)
# -----------------------------------------------------------------------------------------------


#enviar y recibir al servicio
def send(queue):
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = message_pb2_grpc.MessageServiceStub(channel)
            message = queue.queue.get()
            response = stub.Greet(message_pb2.MessageRequest(name=message))
            queues["cola2"].queue.put(response.greeting)



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
    if name in queues:
        del queues[name]
        return jsonify({'message': 'Queue deleted successfully'})
    else:
        return jsonify({'error': 'Queue not found'})

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run()
