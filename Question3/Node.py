from datetime import datetime

class Node():
    def __init__(self,data=None, next_node=None, previous_node=None):
        self.next_node = next_node
        self.previous_node = previous_node
        self.data = data
        self.timestamp = datetime.now()

    def getdata(self):
        return self.data

    def setdata(self,data):
        self.data = data

    def getPrev(self):
        return self.previous_node

    def setPrev(self,prev):
        self.previous_node = prev

    def getNext(self):
        return self.next_node

    def setNext(self,next):
        self.next_node = next