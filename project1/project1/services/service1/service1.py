import grpc
import main_pb2
import main_pb2_grpc
import time

# Connection with server GRPC
channel = grpc.insecure_channel('localhost:50051')

# Create a stub (client)
# Of class MessageQueue
stub = main_pb2_grpc.MessageQueueStub(channel)

def send_message(username, api_key, service):
    print("\n")
    print("From send_message")
    print(f"Username: {username}")
    print(f"API Key: {api_key}")
    print(f"Service: {service}")
    res = 'Perfecto'
    # Build a message of request to sendMessage
    message = main_pb2.SendMessageRequest(username=username, api_key=api_key, service=service, response=res)

    try:
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
    print("\n")
    print("From get message")
    # Build a message of request to getMessage
    message = main_pb2.Message(queue_name='service1')

    try:
        # Send request to server
        response = stub.getMessage(message)

        # process response
        print(f"Message: {response.message}")
        if response.status != 200:
            time.sleep(0.5)
            run()
        
        send_message(response.username, response.api_key, response.service)

        
    except grpc.RpcError as e:
        print(f"Error: {e.details()}")


if __name__ == '__main__':
    run()
