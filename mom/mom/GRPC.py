import grpc
from concurrent import futures
import time

import main_pb2
import main_pb2_grpc
from file import get_next_message_service_1, get_next_message_service_2, save_response


class MessageQueueServicer(main_pb2_grpc.MessageQueueServicer):
    def getMessage(self, request, context):
        response = main_pb2.GetMessageResponse()

        #  Get service that do the request
        cola = request.queue_name
        message = None

        print("\n")
        print("Request from service: " + cola)
        print("\n")

        if int(cola) == 1:
            message = get_next_message_service_1()
        elif int(cola) == 2:
            message = get_next_message_service_2()

        # Validate if the queue is empty
        if message is None:
            response.status = 400
            response.message = 'No exist messages in queue'
            response.username = ''
            response.api_key = ''
            response.service = ''
            response.queue_name = ''
            return response

        response.status = 200
        response.message = 'Message found'
        response.username = message['username']
        response.api_key = message['api_key']
        response.service = str(message['service'])
        response.queue_name = message['queue_name']

        return response

    def sendMessage(self, request, context):
        print("\n")
        print("Save response to: " + request.service)
        print("\n")
        response = main_pb2.SendMessageResponse()


        save_response(request.username, request.queue_name, request.service, request.response)

        response.status = 200
        response.message = 'Message sent'

        # completar los valores de response según la lógica de tu aplicación
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    main_pb2_grpc.add_MessageQueueServicer_to_server(
        MessageQueueServicer(), server)
    server.add_insecure_port('[::]:50051')
    print('Server started')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
