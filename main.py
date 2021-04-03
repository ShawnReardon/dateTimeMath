from random import randint
import datetime

class dateTimeMath(object):
  dateDict = dict()
  num = 1
  def __init__(self):
    self.date = datetime.datetime.now()
    self.future = datetime.datetime

  def promptDate(self):
    year = int(input("Provide a Year (Ex. 2002): "))
    month = int(input("Provide a Month (Ex. 12): "))
    day = int(input("Provide a Day (Ex. 05): "))
    self.future = datetime.datetime(year, month, day)
    return self.future

  def storeDate(self):
    note = input("Enter Reminder Note: ")
    self.dateDict[note] = self.future
    self.num+=1
  
  def displayDates(self):
    index = 1
    for date in self.dateDict.items():
      print(index, date[0], date[1])
      index+=1
      

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
      self.dateDict[key] = self.future

  
  def DEBpromptDate(self):
    year = 2035 + randint(1, 10)
    month = 1 + randint(1, 10)
    day = 1 + randint(1, 15)
    self.future = datetime.datetime(year, month, day)
  
  def DEBstoreDate(self):
    note = "abcdefghijklompnm"
    note = note[randint(1, 10)]
    self.dateDict[note] = self.future
    self.num+=1
  
  def debug(self):
    self.DEBpromptDate()
    self.DEBstoreDate()
    self.displayDates()


