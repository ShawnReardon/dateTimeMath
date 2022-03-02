from random import randint
import datetime
from datetime import timedelta
from schedule import student


class dateTimeMath(object):
  #f = open("random.txt", "r")
  dateDict = dict()
 
  num = 1
  def __init__(self):
    self.date = datetime.date.today()
    self.studentName = None
  
  def promptTime(self, dateObject):
    hour = int(input("Provide the Hour (Ex. 1-12): "))
    minute = int(input("Provide a Mminute (Ex. 0-59): "))
    Time = datetime.time(hour = hour, minute = minute, second = 0)
    return datetime.datetime.combine(dateObject, Time)

  def promptDate(self):
    name = input("Please enter the students name: ")
    self.studentName = name
    changeDate = int(input("Enter 1 if the note is NOT for today's date "))

    if changeDate == 1:
       self.date = input("Enter date in the format 12/12/2012 ")
    
    return self.studentName
    
    

  def storeDate(self):
    if self.studentName in self.dateDict:
      self.note = input("Enter Note: ")
      self.dateDict[self.studentName].newNote(self.note, self.date)
      print(self.dateDict[self.studentName].head.next.note)
    else:
      print("ADD")
      self.note = input("Enter Reminder Note: ")
      self.dateDict[self.studentName] = student()
      self.dateDict[self.studentName].newNote(self.note, self.date)
  
  def displayDates(self):
    print()
    index = 1
    for key in self.dateDict.keys():
      print('Student:', key, end = ' ')
      self.dateDict[key].printStudentInfo()
      index+=1
      if index % 3 == 0:
        print("\n")
      

  def dateGetter(self):
    self.promptDate()
    self.storeDate()

  def editDate(self):
    key_list = list(self.dateDict.keys())
    
    val_list = list(self.dateDict.values())
    
    dateSelection = int(input("Enter Number to Select: "))
    
    value = val_list[dateSelection - 1]
    
    key = key_list[dateSelection - 1]
    
    selection = int(input("What would you like to edit? \n Note: 1 \n Date: 2"))
    
    if selection == 1:
      note = input("Enter NEW Reminder Note: ")
      self.dateDict[note] = value
      del self.dateDict[key]
    elif selection == 2:
      self.promptDate()
      self.dateDict[key] = self.studentName
  
  def shawnIsConfused(self, val):
    isString = True
    temp = ''
    if isinstance(val, int):
      temp = int(val)
      isString = False
      
    return isString, temp
  
  def demoMath(self):
    key_list = list(self.dateDict.keys())
    val_list = list(self.dateDict.values())
    
    print("\nFirst Date - Second Date\n")
    pickdate1 = self.shawnIsConfused(input("Pick First Date: "))
    pickdate2 = self.shawnIsConfused(input("Pick Second Date: "))
    if not pickdate1[0]:
      int(pickdate1)
      int(pickdate2)
      value1 = val_list[pickdate1[1]]
      value2 = val_list[5]
    else:
      value1 = self.dateDict[pickdate1]
      value2 = self.dateDict[pickdate2]
    
    
    
    difference = (value1 - value2)
    
    print("Diff:", difference)
    print(difference + timedelta(days=1))

  
  def DEBpromptDate(self):
    names = ['Shawn', 'Rivet', 'Clank', 'Ratchet', 'Tim']
    name = names[randint(0, 4)]
    note = randint(0, 1000)
    self.DEBstoreDate(name, note)

  def DEBpromptDate2(self):
    year = 2035 #+ randint(1, 10)
    month = 2 #+ randint(1, 10)
    day = 2 #+ randint(1, 15)
    dateObject = datetime.datetime(year, month, day)
    hour = randint(1,12)
    minute = randint(0, 59)
    Time = datetime.time(hour = hour, minute = minute, second = 0)
    self.studentName = datetime.datetime.combine(dateObject, Time)

  def DEBstoreDate(self, name, note):
    if name in self.dateDict:
      self.dateDict[name].newNote(note, self.date)
    else:
      self.dateDict[name] = student()
      self.dateDict[name].newNote(note, self.date)

  
        
    
  
  def debug(self):
    numOfDates = 10
    for i in range(numOfDates):
      self.DEBpromptDate()
     
      

    self.displayDates()
    #self.demoMath()


date = dateTimeMath()
#date.dateGetter()


date.debug()
#date.debug()
#date.editDate()
#date.displayDates()
