class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class List(object):
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,n,x):
        #Not actually perfect: how do we prepend to an existing list?
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x

    def delete(self,i):
        #print('HEAD: ' + str(self.head))
        #print('X: ' + str(i))
        
        if i == 0:
            # If deleting first item we have to set a new head.
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                # If there is only 1 item in the list we set head and tail to none.
                self.head = None
                self.tail = None

        elif i < 0:
            # For deleting items using the tail as reference.
            j = -1
            node = self.tail

            while j > i:
                node = node.prev
                j = j - 1
                if node == None:
                    raise IndexError('list index out of range. Index: ' + str(i))
            
            if node.prev and node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
            elif node.prev and not node.next:
                node.prev.next = None
                self.tail = node.prev
            elif node.next and not node.prev:
                node.next.prev = None
                self.head = node.next
            else:
                self.head = None
                self.tail = None

        elif i > 0:
            # If given an index bigger than 0 we loop through to the node at that index.
            j = 0
            node = self.head
            while j < i:
                node = node.next
                j = j + 1
                if node == None:
                    raise IndexError('list index out of range. Index: ' + str(i))

            prevNode = node.prev

            # We have to check if it's the last item in the list, if it is we set the tail.
            if node.next != None:
                prevNode.next = node.next
                node.next.prev = prevNode
            else:
                prevNode.next = None
                self.tail = prevNode

    def append(self,x):
        if self.tail:
            self.tail.next = x
            x.prev = self.tail
            self.tail = x
        else:
            self.tail = x
            self.head = x

    def len(self):
        length = 0
        node = self.head

        if node == None:
            return 0
            
        while node.next != None:
            print(node.value)
            node = node.next
            length = length + 1

        return length

    def __add__(l1,l2):

        x = l1
        y = l2

        if y.head == None:
            return x
        elif x.tail == None:
            return y
        
        x.tail.next = y.head
        y.head.prev = x.tail
        x.tail = y.tail
        y.head = x.head

        return x
        
    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print ("List: ",",".join(values))
	 
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.tail,Node(6))
    l.insert(l.tail,Node(8))
    l.insert(l.tail,Node(12))
    l.insert(l.tail,Node(7))
    l.insert(l.tail,Node(-5))
    l.append(Node(5))
    l.display()
    l.delete(5)
    l.display()

    j=List()
    j.append(Node(1))
    j.append(Node(2))
    j.append(Node(3))
    j.display()
    j.delete(2)
    j.display()

    #h=List()

    #k = j+l
    #k.display()
    #k.delete(-6)
    #k.display()

    print('Length of l is: ' + str(l.len()))
    #print(j.len())
