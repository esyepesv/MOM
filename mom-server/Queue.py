from queue import Queue

class Queue:

    queue = Queue()

    def __init__(self, name, user, key):
        
        self._name = name
        self._user = user
        self._key = key
        
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
        
    def get_user(self):
        return self._user
    
    def set_user(self, user):
        self._user = user
        
    def get_key(self):
        return self._key
    
    def set_key(self, key):
        self._key = key
