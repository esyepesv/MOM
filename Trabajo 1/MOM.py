from concurrent import futures
import grpc

import message_pb2
import message_pb2_grpc

from collections import deque

colaEntrada = deque()
colaSalida = deque()

class MessageServicer(message_pb2_grpc.MessageServiceServicer):

    def Greet(self, request, context):     

        response = message_pb2.MessageResponse()

        colaEntrada.append(request.name)

        print(colaEntrada)

        send()


def listen():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_MessageServiceServicer_to_server(MessageServicer(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("Hola, Soy El MOM")

def send():
     with grpc.insecure_channel('localhost:50051') as channel:
            
            stub = message_pb2_grpc.MessageServiceStub(channel)

            response = stub.Greet(message_pb2.MessageRequest(name = colaEntrada.pop()))

            response = message_pb2.MessageResponse()

            colaSalida.append(response.greeting)

            print("esto hay en la cola de salida: ", colaSalida)

            return response


if __name__ == "__main__":
    listen()