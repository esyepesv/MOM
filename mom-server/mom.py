from concurrent import futures
import grpc
import sys
sys.path.append('../')
import time
import message_pb2
import message_pb2_grpc

from collections import deque

class MessageServicer(message_pb2_grpc.MessageServiceServicer):

    def __init__(self, colaEntrada):
        self.colaEntrada = colaEntrada

    def Greet(self, request, context):     
        response = message_pb2.MessageResponse()

        self.colaEntrada.append(request.name)

        print(self.colaEntrada)

        response = run_send(self.colaEntrada)

        print("Esta es la respuesta: ",response)

        #response.greeting = "Hello, {}!".format(request.name)

        return response


def run_server():
    colaEntrada = deque()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_MessageServiceServicer_to_server(MessageServicer(colaEntrada), server)
    server.add_insecure_port("[::]:50052")
    print("Hola, Soy El MOM")
    server.start()

    def handle_messages(servicer):
        while True:
            if len(servicer.colaEntrada) > 0:
                mensaje = servicer.colaEntrada.popleft()
                # procesar el mensaje como sea necesario
                # crear una respuesta usando message_pb2.MessageResponse()
                # enviar la respuesta a través del contexto del cliente
            else:
                time.sleep(1)

    handle_messages(MessageServicer(colaEntrada))


def run_send(colaEntrada):
    if len(colaEntrada) > 0:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = message_pb2_grpc.MessageServiceStub(channel)
            mensaje = colaEntrada.pop()
            response = stub.Greet(message_pb2.MessageRequest(name = mensaje))
            return response.greeting
    else:
        run_server() 

if __name__ == "__main__":
    run_server()