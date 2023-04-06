import grpc
import sys
sys.path.append('../')
import message_pb2
import message_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = message_pb2_grpc.MessageServiceStub(channel)
        nombre = input("Ingresa un mensaje: ")
        response = stub.Greet(message_pb2.MessageRequest(name = nombre))
        print(response.greeting)
        
if __name__ == '__main__':
    run()

