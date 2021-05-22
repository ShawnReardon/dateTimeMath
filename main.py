from random import randint
import datetime
from datetime import timedelta


class dateTimeMath(object):
  #f = open("random.txt", "r")
  dateDict = dict()
 
  num = 1
  def __init__(self):
    self.date = datetime.datetime.now()
    self.futureDate = datetime.date
  
  def promptTime(self, dateObject):
    hour = int(input("Provide the Hour (Ex. 1-12): "))
    minute = int(input("Provide a Mminute (Ex. 0-59): "))
    Time = datetime.time(hour = hour, minute = minute, second = 0)
    return datetime.datetime.combine(dateObject, Time)

  def promptDate(self):
    year = int(input("Provide a Year (Ex. 2002): "))
    month = int(input("Provide a Month (Ex. 12): "))
    day = int(input("Provide a Day (Ex. 05): "))
    self.futureDate = datetime.date(year, month, day)
    addTime = int(input("If you want to add a time enter 1 "))

    if addTime == 1:
       self.futureDate = self.promptTime(self.futureDate)
    
    return self.futureDate
    
    

  def storeDate(self):
    note = input("Enter Reminder Note: ")
    self.dateDict[note] = self.futureDate
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
      self.dateDict[key] = self.futureDate
  
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
    year = 2035 + randint(1, 10)
    month = 1 + randint(1, 10)
    day = 1 + randint(1, 15)
    self.futureDate = datetime.date(year, month, day)
  
  def DEBstoreDate(self):
   
 
    key = {str(randint(0, 50))}
    note = ""
# Strips the newline character
    for line in range(10):
      if not randint(0, 50) in {0, 2, 4, 6, 8, 10}:
        key.add(str(randint(0, 50)))
      else:
        break
    for line in key:
      note += line

    self.dateDict[note] = self.futureDate
        
    
  
  def debug(self):
    numOfDates = 10
    for i in range(numOfDates):
      self.DEBpromptDate()
      self.DEBstoreDate()
    self.displayDates()
    self.demoMath()


date = dateTimeMath()
date.dateGetter()

date.debug()
#date.debug()
#date.editDate()
#date.displayDates()