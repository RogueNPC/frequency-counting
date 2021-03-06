from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def find(self,item):

    current = self.head

    found = False
    counter = 0

    while current != None and not found:

      if current.data[0] == item:
        found = True
      else:
        current = current.next
        counter += 1

    if found:
      return counter
    else:
      return -1

  # custom method to increment node value by 1 when inserting identical key
  def modify(self,index):

    current = self.head

    for i in range(index):
      current = current.next
    data = list(current.data)
    data[1] += 1
    current.data = tuple(data)
    return -1


  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    current = self.head
    
    for i in range(self.length()):
      print(f'{current.data[0]}: {current.data[1]}')
      current = current.next

  def distinct_words(self):
    current = self.head
    counter = 0
    
    for i in range(self.length()):
      counter += 1
      current = current.next
      
    return counter

  def exact_count(self, index):
    
    current = self.head

    for i in range(index):
      current = current.next
    return current.data[1]