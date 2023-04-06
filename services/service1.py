from concurrent import futures
import grpc

import sys
sys.path.append('../')

import message_pb2
import message_pb2_grpc

class MessageServicer(message_pb2_grpc.MessageServiceServicer):
    def Greet(self, request, context):

        print(request.name)

        response = message_pb2.MessageResponse()

        response.greeting = "Hello, {}!".format(request.name)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_MessageServiceServicer_to_server(MessageServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("Hola, Soy El Server")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
