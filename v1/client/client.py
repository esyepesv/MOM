import grpc
import sys
sys.path.append('../')
import message_pb2
import message_pb2_grpc
from flask import Flask

app = Flask(__name__)

@app.route('/')
def send():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = message_pb2_grpc.MessageServiceStub(channel)
        nombre = "Stiven"
        response = stub.Greet(message_pb2.MessageRequest(name = nombre))

        print(response.greeting)
        return response.greeting
        
if __name__ == '__main__':
    app.run()



