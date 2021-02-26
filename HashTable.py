from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.
  def create_arr(self, size):
     
    temp = []
    for i in range(size):
      temp.append(LinkedList())
    return temp


  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 
  def hash_func(self, key):
    
    key_length = len(key)

    index = key_length % self.size

    return index


  # Inserts a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared.
  # When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.
  def insert(self, key, value):

    # First find the index where it should be placed
    key_hash = self.hash_func(key)

    # Access the linked list in the array
    ll = self.arr[key_hash]

    # Check if the index exists in the linked list
    index_in_linkedlist = ll.find(key)
      
    # if not item not in linkedlist
    if index_in_linkedlist == -1:
      tup = (key, value)    # Creates tuple for new word
      ll.append(tup)    # Append it to the linked list
    # if item found in linkedlist
    else:
      ll.modify(index_in_linkedlist)


  # Traverses through every Linked List in the table and print the key value pairs.
  def print_key_values(self):
    for key_hash in range(self.size): 
      self.arr[key_hash].print_nodes()


  # Returns the total number of distinct words
  def count_distinct_words(self):
    counter = 0
    for key_hash in range(self.size):
      num_distinct_words = self.arr[key_hash].distinct_words()
      counter += num_distinct_words
    return counter


  def find_exact(self, key):
    key_hash = self.hash_func(key)
    ll = self.arr[key_hash]
    index_in_linkedlist = ll.find(key)
    if index_in_linkedlist == -1:
      return -1
    else:
      return ll.exact_count(index_in_linkedlist)