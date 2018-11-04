from Node import *

class DoublyLinkedList :

    def __init__(self, size) :
        self.size = size
        self.currSize = 0
        self.head = None
        self.tail = None
        self.current = None

    def __iter__(self):
        self.current = self.head
        return self

    def addPageToList(self, data):  # Node
        dataToAdd = Node(data)
        if (self.head == None):
            self.head = dataToAdd
            self.tail = dataToAdd
            self.currSize = 1
            return dataToAdd
        elif (self.currSize < self.size):
            self.currSize = self.currSize + 1
        else:
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)

        dataToAdd.setNext(self.head)
        self.head.setPrev(dataToAdd)
        self.head = dataToAdd
        self.current = self.head
        return dataToAdd

    def movePageToHead(self,  dataFetched ):
        if (dataFetched == None or dataFetched == self.head):
            return

        if (dataFetched == self.tail):
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)

        prev = dataFetched.getPrev()
        next = dataFetched.getNext()
        prev.setNext(next)

        if (next != None):
            next.setPrev(prev)

        dataFetched.setPrev(None)
        dataFetched.setNext(self.head)
        self.head.setPrev(dataFetched)
        self.head = dataFetched
        self.current = self.head

    def getCurrSize(self):
        return self.currSize

    def setCurrSize(self, currSize):
        self.currSize = currSize

    def getHead(self):  # Node
        return self.head

    def setHead(self, head):
        self.head = head

    def getTail(self) :
        return self.tail

    def remove_current(self):
        if self.current == self.getTail() :
            self.tail.getPrev().setNext(None)
            return
        if self.current == self.getHead() :
            self.Head = self.Head.getNext()
            return
        prev = self.current.getPrev()
        next = self.current.getNext()
        prev.setNext(next)
        next.setPrev(prev)

    def getSize(self):
        return self.size

    def __next__(self):
        if  self.current.getNext() == None  :
            raise StopIteration()
        self.current = self.current.getNext()
        return self.current
