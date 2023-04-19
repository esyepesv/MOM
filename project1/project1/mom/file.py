import json

def get_service1():
    with open("data.txt", "r") as archivo:
        line1 = json.loads(archivo.readline())
    
    return line1

def get_service2():
    with open("data.txt", "r") as archivo:
        next(archivo)
        line2 = json.loads(archivo.readline())
    
    return line2

def get_queues():
    with open("data.txt", "r") as archivo:
        next(archivo)
        next(archivo)
        
        line3 = json.loads(archivo.readline())
    
    return line3

def update_service1(new_line1):
    with open("data.txt", "r") as archivo:
        lineas = archivo.readlines()

    lineas[0] = json.dumps(new_line1) + '\n'

    with open("data.txt", "w") as archivo:
        archivo.writelines(lineas)

def add_to_service1(message):
    line1 = get_service1()
    line1.append(message)
    update_service1(line1)

def update_service2(new_line2):
    with open("data.txt", "r") as archivo:
        lineas = archivo.readlines()

    lineas[1] = json.dumps(new_line2) + '\n'

    with open("data.txt", "w") as archivo:
        archivo.writelines(lineas)

def add_to_service2(message):
    line2 = get_service2()
    line2.append(message)
    update_service2(line2)

def update_queues(new_queues):
    with open("data.txt", "r") as file:
        lines = file.readlines()

    lines[2] = json.dumps(new_queues) + '\n'

    with open("data.txt", "w") as file:
        file.writelines(lines)

def user_exist(username, queues):
    if username in queues:
        return True
    
    return False

def create_username(username):
    queues = get_queues()
    if username in queues:
        print("Error")
        return None

    queues[username] = {}

    update_queues(queues)
    return None

def queue_exist(queue_name, queue_user):
    if queue_name in queue_user:
        return True
    return False

def create_queue(username, name_queue, api_key):
    queues = get_queues()

    if user_exist(username, queues) == False:
        print("Error")
        return None

    queues_user = queues[username]

    if queue_exist(name_queue, queues_user):
        print("Error")
        return None

    queues_user[name_queue]= {
        'id': 1,
        'api_key': api_key,
        'data_req': [],
        'data_res': []
    }

    update_queues(queues)

def validate_api_key(api_key_queue, api_key_request):
    if api_key_queue == api_key_request:
        return True
    return False

def add_message(username, queue_name, api_key, service):
    queues = get_queues()
    if user_exist(username, queues) == False:
        print("Error")
        return None
    
    queues_user = queues[username]
    if queue_exist(queue_name, queues_user) == False:
        print("Error")
        return None
    
    queue_info = queues_user[queue_name]
    id = queue_info['id']
    api_key_queue = queue_info['api_key']
    queue_data = queue_info['data_req']

    if validate_api_key(api_key_queue, api_key) == False:
        print("Error")
        return None
    
    if service not in [1, 2]:
        print("Error, service")
        return None 
    
    message = {
        'id': id,
        'service': service,
        'queue_name': queue_name,
        'username': username,
        'api_key': api_key
    }
    # queue_data.append(message)
    # queue_info['data_req'] = queue_data
    
    if service == 1:
        add_to_service1(message)
    if service == 2:
        add_to_service2(message)

    id += 1
    queue_info['id'] = id
    update_queues(queues)

def get_next_message_service_1():
    service1 = get_service1()

    if len(service1) < 1:
        print("Error, no data in service 1")
        return None

    message_pop = service1.pop(0)

    update_service1(service1)

    return message_pop

def get_next_message_service_2():
    service2 = get_service2()

    if len(service2) < 1:
        print("Error, no data in service 2")
        return None

    message_pop = service2.pop(0)

    update_service2(service2)

    return message_pop

def save_response(username, queue_name, service, response):
    queues = get_queues()

    queues[username][queue_name]['data_res'].append({
        'queue_name': queue_name,
        'service': service,
        'response': response
    })

    update_queues(queues)

def get_last_messages_user(username, queue_name, api_key):
    queues = get_queues()
    if user_exist(username, queues) == False:
        print("Error")
        return None
    
    queues_user = queues[username]
    if queue_exist(queue_name, queues_user) == False:
        print("Error")
        return None
    
    queue_info = queues_user[queue_name]
    id = queue_info['id']
    api_key_queue = queue_info['api_key']
    queue_res = queue_info['data_res']

    if validate_api_key(api_key_queue, api_key) == False:
        print("Error")
        return None
    
    queue_info['data_res'] = []
    update_queues(queues)
    
    return queue_res