import grpc
import main_pb2
import main_pb2_grpc
import time

# Connection with server GRPC
channel = grpc.insecure_channel('localhost:50051')

# Create a stub (client)
# Of class MessageQueue
stub = main_pb2_grpc.MessageQueueStub(channel)

def send_message(username, api_key, service, queue_name):
    res = 'Response from service 2'
    # Build a message of request to sendMessage
    message = main_pb2.SendMessageRequest(username=username, api_key=api_key, service=service, response=res, queue_name=queue_name)

    try:
        print("\n")
        print("Sending response to server 2")
        print("\n")
        # Send request to server
        response = stub.sendMessage(message)

        # process response
        print(f"Message: {response.message}")
        
        # Run the program again
        time.sleep(0.5)
        run()
        
    except grpc.RpcError as e:
        print(f"Error: {e.details()}")


def run():
    # Build a message of request to getMessage
    message = main_pb2.Message(queue_name='2')

    try:
        print("\n")
        print("Sending request to server 1")
        print("\n")
        # Send request to server
        response = stub.getMessage(message)

        # process response
        print(f"Message: {response.message}")
        if response.status != 200:
            time.sleep(0.5)
            run()
        
        send_message(response.username, response.api_key, response.service, response.queue_name)

        
    except grpc.RpcError as e:
        print(f"Error: {e.details()}")


if __name__ == '__main__':
    run()
