from concurrent import futures
import grpc
import sys
sys.path.append('../')
import time
import message_pb2
import message_pb2_grpc

from collections import deque

colaEntrada = deque()
colaSalida = deque()

class MessageServicer(message_pb2_grpc.MessageServiceServicer):

    def __init__(self, colaEntrada):
        self.colaEntrada = colaEntrada

    def Greet(self, request, context):     
        response = message_pb2.MessageResponse()

        self.colaEntrada.append(request.name)

        print(self.colaEntrada)

        response = message_pb2.MessageResponse()

        response.greeting = "solicitud guardada en mom"
        if len(colaEntrada) > 0:
            send()
        return response



def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_MessageServiceServicer_to_server(MessageServicer(colaEntrada), server)
    server.add_insecure_port("[::]:50052")
    print("Hola, Soy El MOM")
    server.start()
    server.wait_for_termination()

def send():
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = message_pb2_grpc.MessageServiceStub(channel)
            mensaje = colaEntrada.pop()
            response = stub.Greet(message_pb2.MessageRequest(name = mensaje))
            colaSalida.append(response)
            print(colaSalida)


if __name__ == "__main__":
    run_server()