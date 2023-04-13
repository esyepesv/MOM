import grpc
from concurrent import futures
import time

import main_pb2
import main_pb2_grpc

from mom.shared_memory import service1_shared_list, service2_shared_list, queues_shared_dict

example_cola = [
    {
        'username': 'jpcortesg',
        'api_key': '1234567890',
        'service': 'twitter',
    },
    {
        'username': 'jpcortesg1',
        'api_key': '1234567891',
        'service': 'twitter',
    },
]

example_cola_response = []


class MessageQueueServicer(main_pb2_grpc.MessageQueueServicer):
    def getMessage(self, request, context):
        response = main_pb2.GetMessageResponse()

        cola = request.queue_name
        print("\n")
        print("From get message")
        print(f"Message from Queue: {cola}")

        # Validate if the queue is empty
        if len(example_cola) == 0:
            response.status = 400
            response.message = 'No exist messages in queue'
            response.username = ''
            response.api_key = ''
            response.service = ''
            return response

        # Logic to get a message from the queue
        message = example_cola.pop(0)

        response.status = 200
        response.message = 'Message found'
        response.username = message['username']
        response.api_key = message['api_key']
        response.service = message['service']

        return response

    def sendMessage(self, request, context):
        print("\n")
        print("From send message")
        response = main_pb2.SendMessageResponse()

        new = {
            'username': request.username,
            'api_key': request.api_key,
            'service': request.service,
            'response': request.response,
        }

        example_cola_response.append(new)

        response.status = 200
        response.message = 'Message sent'

        # completar los valores de response según la lógica de tu aplicación
        return response


def serve():
    print(service1_shared_list)
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
