import multiprocessing

# Create a shared memory of type list that has dictionaries for service1
service1_shared_list = multiprocessing.Manager().list()

# Create a shared memory of type list that has dictionaries for service2
service2_shared_list = multiprocessing.Manager().list()

# Create a shared memory of type dict that has dictionaries and lists for queues
queues_shared_dict = multiprocessing.Manager().dict()

# Define a function that will modify the shared memory for service1
def modify_service1_shared_list(service1_shared_list):
    service1_shared_list.append({'id': 1, 'name': 'John'})
    service1_shared_list.append({'id': 2, 'name': 'Jane'})

# Define a function that will modify the shared memory for service2
def modify_service2_shared_list(service2_shared_list):
    service2_shared_list.append({'id': 1, 'name': 'Bob'})
    service2_shared_list.append({'id': 2, 'name': 'Alice'})

# Define a function that will modify the shared memory for queues
def modify_queues_shared_dict(queues_shared_dict):
    queues_shared_dict['queue1'] = {'key1': 'value1', 'key2': ['value2']}
    queues_shared_dict['queue2'] = {'key3': 'value3', 'key4': ['value4']}


# Create a process that will modify the shared memory for service1
p1 = multiprocessing.Process(
    target=modify_service1_shared_list, args=(service1_shared_list,))
p1.start()
p1.join()

# Create a process that will modify the shared memory for service2
p2 = multiprocessing.Process(
    target=modify_service2_shared_list, args=(service2_shared_list,))
p2.start()
p2.join()

# Create a process that will modify the shared memory for queues
p3 = multiprocessing.Process(
    target=modify_queues_shared_dict, args=(queues_shared_dict,))
p3.start()
p3.join()
