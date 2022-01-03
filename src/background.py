from datetime import date

todays_date = date.today()  #  todays_date.year, todays_date.month todays_date.day

"""
  Add, Edit, Remove Tasks
  List all added tasks
  Assign your self a study period
  Tick off if you actually did it, if you didn't, input your excuse
"""


class Card:
    def __init__(self, Name, DueDate=None, Priority=None):
        self._Name = Name
        self._Tags = {}
        self._CustomTagList = {}
        # {Tag name: priority} # The highest priority will be used
        
        if DueDate != None:
            self.SetSetDueDate(DueDate)
            if Priority != None:
                self._Priority = Priority
            else:
                self._Priority = self.DatePriorityAllocater()
        else:
            if Priority != None:
                self._Priority = Priority
            else:
                self._Priority = 0
            self._DueDate = None
            self._DueTime = None
            self._Time = None  # Not used in prototype
            self._Day = None
            self._Month = None
            self._Year = None

    # Returns a priority number for "Assigned tasks" depending on how close it is to the due date
    def DatePriorityAllocater(self):

        # Within 3 days, Red, 8
        # Within 1 week, Orange, 7
        # Within 2 weeks, Green, 5

        # Prototype version just looks at month year and day difference
        # Within 2 month, 5
        # Within 1 month, 7
        # Within 1 week, 8
        # Within this year or next year, 3
        # Global todays_date

        YearDifference = self._Year - todays_date.year
        MonthDifference = self._Month - (todays_date.month + 12 * YearDifference)
        DayDifference = self._Day - (todays_date.day + 30.5 * MonthDifference)

        if YearDifference >= 2:
            return 3
        elif MonthDifference >= 3:
            return 4
        elif MonthDifference >= 1:
            return 5
        elif DayDifference >= 14:
            return 7
        elif DayDifference < 14:
            return 8

    # Function that returns the highest priority of this item (for when there was multiple tags and prios to one item)
    def ReturnPriority(self):
        return self._Priority

    # Helper Function for SortByDate only
    def ReturnDateBol(self):
        if self._DueDate != None:
            return True
        else:
            return False

    def ReturnName(self):
        return self._Name

    def RemoveCustomTag(self, CustomTagName):
        if CustomTagName in self._CustomTagList.keys():
            self._CustomTagList.pop("CustomTagName")
        else:
            print('Custom tag "', CustomTagName, '" does not exist')

    # Checks if the inputted date checks out. *(Should they be able to input a date in the past?, should we auto delete events that already happened?)
    def DueDateChecker(self, Time, Day, Month, Year):
        # Checks if the designated inputs actually make sense and returns the error message if it doesn't.
        # You can store dates in the past however, for whatever reason
        # if it works, SetDueDate here too
        pass

    def SetSetDueDate(self, DueDate):
        Day, Month, Year, Time = DueDate.split()
        self.SetDueDate(int(Day), int(Month), int(Year), Time)

    # Make it so any ONE of these isn't actually needed.
    def SetDueDate(self, Day, Month, Year, Time):
        self._DueDate = "{} on {} / {} / {}".format(Time, Day, Month, Year)
        self._Time = Time
        self._Day = Day
        self._Month = Month
        self._Year = Year

    def __str__(self):
        return "Task '{}' at {}".format(self._Name, self._DueDate)

def SortByDate(List):
    DateTrue = []
    DateFalse = []
    for i in List:
        if i.ReturnDateBol():
            DateTrue.append(i)
        else:
            DateFalse.append(i)
    DateTrue.sort(key=lambda x: x.ReturnPriority())
    DateFalse.sort(key=lambda x: x.ReturnName())
    return DateTrue + DateFalse


if __name__ == "__main__":
    #import pickle
    #pickle.dump(LobbyArt, open("MapSaveFile", "wb"))
    #ThePlayer = pickle.load(open("PlayerSaveFile", "rb"))
    
    # Card(Name, DueDate=None, Priority=None)
    Test1 = Card("Test1")
    print (Test1)
    print (Test1.ReturnPriority(), '\n')

    Test2 = Card("Test2", "31 01 2022 12:30")
    print (Test2)
    print (Test2.ReturnPriority(), '\n')

    Test3 = Card("Test3", None, 9)
    print (Test3)
    print (Test3.ReturnPriority(), '\n')

    TestList = [Test1, Test2, Test3]

    #Sort by Prio
    TestList.sort(key=lambda x: x.ReturnPriority())
    for x in TestList:
        print(x)
    print('\n')

    #Sort by DueDate
    for x in SortByDate(TestList):
        print(x)