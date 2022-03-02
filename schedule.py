import datetime


def add(num1, num2, num3 = 0):
  return num1 + num2 + num3

print(add(2,2, 10))
# implement grades per note and a totaller that totalls all grade != None

d = dict()


class eventNode:
  def __init__(self, note, Date = datetime.date.today(), grade = None, prev = None, next = None):
    self.note = note
    self.date = Date
    self.grade = grade
    self.prev = None
    self.next = None

  
class student:
  def __init__(self):
    self.head = None # Initally there are no elements in the list
    self.tail = None
    self.count = 0
  

  def push_front(self, note, Date): # Adding an element before the first element
    new_node = eventNode(note, Date) # creating a new node with the desired value
    new_node.next = self.head # newly created node's next pointer will refer to the old head
    self.count += 1

    if self.head != None: # Checks whether list is empty or not
        self.head.prev = new_node # old head's previous pointer will refer to newly created node
        self.head = new_node # new node becomes the new head
        new_node.prev = None
    
    else: # If the list is empty, make new node both head and tail
      self.head = new_node
      self.tail = new_node
      new_node.prev = None # There's only one element so both pointers refer to null
    

  def push_back(self, note, time): # Adding an element after the last element
      new_node = eventNode(note, time)
      new_node.prev = self.tail
      self.count += 1
      if self.tail == None: # checks whether the list is empty, if so make both head and tail as new node
        self.head = new_node 
        self.tail = new_node
        new_node.next = None # the first element's previous pointer has to refer to null
              
      else: # If list is not empty, change pointers accordingly
        self.tail.next = new_node
        new_node.next = None
        self.tail = new_node # Make new node the new tail
    

  def peek_front(self): # returns first element
    if self.head == None: # checks whether list is empty or not
      print("List is empty")
    else:
      return self.head.note

  
  def peek_back(self): # returns last element
    if self.tail == None: # checks whether list is empty or not
      print("List is empty")
    else:
      return self.tail.data
  

  def pop_front(self): # removes and returns the first element
    if self.head == None:
      print("List is empty")
    
    else:
      self.count -= 1
      temp = self.head
      temp.next.prev = None # remove previous pointer referring to old head
      self.head = temp.next # make second element the new head
      temp.next = None # remove next pointer referring to new head
      return temp.data
  
  
  def pop_back(self): # removes and returns the last element
    if self.tail == None:
      print("List is empty")

    else:
      self.count -= 1
      temp = self.tail
      temp.prev.next = None # removes next pointer referring to old tail
      self.tail = temp.prev # make second to last element the new tail
      temp.prev = None # remove previous pointer referring to new tail
      return temp.data
  

  def insert_after(self, temp_node, note, time): # Inserting a new node after a given node
    if temp_node == None:
      print("Given node is empty")
    
    if temp_node != None:
      self.count += 1
      new_node = eventNode(note, time)
      new_node.next = temp_node.next
      temp_node.next = new_node
      new_node.prev = temp_node
      if new_node.next != None:
        new_node.next.prev = new_node
      
      if temp_node == self.tail: # checks whether new node is being added to the last element
        self.tail = new_node # makes new node the new tail
    

  
  def insert_before(self, temp_node, note, time): # Inserting a new node before a given node
    if temp_node == None:
      print("Given node is empty")
    
    if temp_node != None:
      self.count += 1
      new_node = eventNode(note, time)
      new_node.prev = temp_node.prev
      temp_node.prev = new_node
      new_node.next = temp_node
      if new_node.prev != None:
        new_node.prev.next = new_node
      
      if temp_node == self.head: # checks whether new node is being added before the first element
        self.head = new_node # makes new node the new head

  def timeInsert(self, note, time):
     new_node = eventNode(note, time)
     
     if self.count == 0:
       self.head = new_node
       self.tail = new_node
       self.count += 1
       return

     tmp = self.head
     for i in range(self.count):
       if new_node.time > tmp.time:
         if tmp.next == None:
           self.insert_after(tmp, note, time)
           return
         else:
          tmp = tmp.next
       else:
         self.insert_before(tmp, note, time)
         return
  def newNote(self, note, Date = None):
    #shouldModifyDate = int(input("Enter 1 if the note is NOT for today's date "))
    if Date == None:
      #newDate = input("Enter date in the format 12/12/2012 ")
      #note = input("Pleae Enter Note: ")
      newNode = eventNode(note)
    else:
      #note = input("Pleae Enter Note: ")
      newNode = eventNode(note, Date)
    
    self.count += 1

    newNode.prev = self.tail
    self.count += 1
    if self.tail == None: # checks whether the list is empty, if so make both head and tail as new node
      self.head = newNode 
      self.tail = newNode
      newNode.next = None # the first element's previous pointer has to refer to null
              
    else: # If list is not empty, change pointers accordingly
      self.tail.next = newNode
      newNode.next = None
      self.tail = newNode # Make new node the new tail



  def removeByDate(self, Date):
     rm = self.head
     for i in range(self.count):
       if Date != rm.date:
         rm = rm.next
       else:
         self.count -= 1
         rm.prev.next = rm.next
         rm.next.prev = rm.prev
         return

  def printStudentInfo(self):
     tmp = self.head
     for i in range(self.count):
       if tmp == None:
         break
       print('**', tmp.note, tmp.date, end = ' ')
       tmp = tmp.next



