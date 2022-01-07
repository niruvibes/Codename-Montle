from datetime import date
from time import time
import math

todays_date = date.today()  #  todays_date.year, todays_date.month todays_date.day

"""

    Add, Remove Tasks 
        #Add
            #Check if EVERY INPUT IS VALID
                #Day, Month, Year, Time
            #Make it so it doesn't need ANY OF these but can just have 1
        #Remove
        Edit
    #List all added tasks
        #By prio
        #By Closeness
    Generate a timetable 
        that considerates the average time spent on each item through a given time (each day) over a week

    Prints in neat format in Python Terminal. 
        Timetable
        Calender
            Make it fit perfectly in the terminal and fancy. (Make sure it can print the characters if special)
    Pygame Screen for interable options (buttons)
        BUTTON ANIMATIONS (100% needed no matter what)  
        Add Task
        Scroll button when selecting existing tasks to remove


    Indefinitely delayed
            Assign your self a study period
            Tick off if you actually did it, if you didn't, input your excuse

"""


class Card:
    # Edit CreateCard() for every change here
    def __init__(self, Name, Day=None, Month=None, Year=None, Time=None, Priority=None):
        self._Name = Name
        self._Tags = {}
        self._CustomTagList = {}

        self.SetDueDate(Day, Month, Year)
        if Day or Month or Year:
            if Priority:  # If a prio is manually given
                self._Priority = Priority
            else:
                # Clumsy looking because if Prio is only date reliant if unspecified
                self._Priority = self.DatePriorityAllocater()
        else:
            if Priority:
                self._Priority = Priority
            else:
                self._Priority = math.inf
            self._Day = None
            self._Month = None
            self._Year = None

        if Time:
            self._DueTime = Time
        else:
            self._DueTime = "HH:MM"

    # Returns a priority number for "Assigned tasks" depending on how close it is to the due date
    def DatePriorityAllocater(self):
        """
        IF PRIO NOT GIVEN, RETURN A NUMBER THAT GETS HIGHER
        """

        if self._Year != None:
            if self._Year < todays_date.year:  # In the past
                return math.inf
            YearDifference = self._Year - todays_date.year
        else:
            YearDifference = 0

        if self._Month != None:
            if self._Month < todays_date.month and self._Year == todays_date.year:
                return 0
            MonthDifference = (self._Month + 12 * YearDifference) - (todays_date.month)
        else:
            MonthDifference = 0

        DayDifference = None
        if self._Day != None:
            if MonthDifference > 0:
                DayDifference = (self._Day + 30.5 * MonthDifference) - (todays_date.day)
            else:
                DayDifference = (self._Day) - (todays_date.day)
        else:
            DayDifference = 1

        if self._Day == None and self._Month == None and self._Year:
            return (YearDifference + 1) * (12 * 30)

        if MonthDifference > 0:
            return MonthDifference * 30 + DayDifference
        else:
            return DayDifference

    # Make it so any ONE of these isn't actually needed.
    def SetDueDate(self, Day, Month, Year):
        Temp = None
        if not Day:
            Day, self._Day = "DD", Temp
        else:
            self._Day = int(Day)
        if not Month:
            Month, self._Month = "MM", Temp
        else:
            self._Month = int(Month)
        if not Year:
            Year, self._Year = "YY", Temp
        else:
            self._Year = int(Year)

        self._DueDate = "{} / {} / {}".format(Day, Month, Year)

    def ReturnPriority(self):
        return self._Priority

    # Helper Function for SortByDate only
    def ReturnDateBol(self):
        if self._Day or self._Month or self._Year:
            return True
        else:
            return False

    def ReturnName(self):
        return self._Name

    def RemoveCustomTag(self, CustomTagName):
        if CustomTagName in self._CustomTagList.keys():
            self._CustomTagList.pop(CustomTagName)
        else:
            print('Custom tag "', CustomTagName, '" does not exist')

    def __str__(self):
        return "Task '{}' at {} on {} (Prio:{})".format(
            self._Name, self._DueTime, self._DueDate, self._Priority
        )


# External Sorting
def SortByDate(Fin):
    DateTrue = []
    DateFalse = []
    for i in Fin:
        if i.ReturnDateBol():
            DateTrue.append(i)
        else:
            DateFalse.append(i)
    DateTrue.sort(key=lambda x: x.DatePriorityAllocater())
    DateFalse.sort(key=lambda x: x.ReturnName(), reverse=False)
    return DateTrue + DateFalse


def RemoveByName(Name, Fin):
    for i in Fin:
        if i.ReturnName() == Name:
            Fin.remove(i)


# Multipurposed Function that will be called separate times for checking every variable
def CreationCheck(Fin=None, Name=None, Day=None, Month=None, Year=None, Time=None):
    if Name:
        for i in Fin:
            if Name == i.ReturnName():
                print("Name Taken! Please try again with a different name.")
                return False
        if Name == "":
            print("Name Invalid! Please think of a name.")
            return False

    if Day:
        Day = int(Day)
        if 0 > Day or Day > 32:
            print("Date invalid! Please try again.")
            return False
    if Month:
        Month = int(Month)
        if 0 > Month or Month > 12:
            print("Month invalid! Please try again.")
            return False

    if Time:
        try:
            Hours, Minutes = Time.split(":")
        except ValueError:
            print("Time format doesn't match! HH:MM please.")
            return False

        if not any((Hours.isdigit(), Minutes.isdigit())):
            print("Digits only! Try again.")
            return False
        if len(Hours) != 2 or len(Minutes) != 2:
            print("Time format doesn't match! HH:MM please.")
            return False
        if 11 < int(Hours) or int(Hours) < 0:
            print("Get the right hours")
            return False
        if 60 < int(Minutes) or int(Minutes) < 0:
            print("Get the right minutes.")
            return False
    return True


def EditCard():
    pass


if __name__ == "__main__":
    # import pickle
    # pickle.dump(LobbyArt, open("MapSaveFile", "wb"))
    # ThePlayer = pickle.load(open("PlayerSaveFile", "rb"))

    # Card(Name, Day=None, Month=None, Year=None, Time=None, Priority=None):)
    Fin = []
    Test1 = Card("Test1")
    print(Test1)
    print(Test1.ReturnPriority(), "\n")

    Test2 = Card("Test2", "31", "01", "2022", "12:30")
    print(Test2)
    print(Test2.ReturnPriority(), "\n")

    if CreationCheck(Fin, "Test3", None, None, "2022", "11:34"):
        Test3 = Card("Test3", None, None, "2022", None)
        print(Test3)
        print(Test3.ReturnPriority(), "\n")
        Fin = [Test1, Test2, Test3]

    if CreationCheck(Fin, "Test4", None, "08", None, "00:00"):
        Test4 = Card("Test4", None, "08", None, "00:00")
        Fin = [Test1, Test2, Test3, Test4]
    if CreationCheck(Fin, "Test5", None, "08", None, "00:00"):
        Test5 = Card("Test5", None, "08", None, "00:00")
        Fin.append(Test5)
    if CreationCheck(Fin, "Test6", "10", None, None, "00:00"):
        Test6 = Card("Test6", "10", None, None, "00:00")
        Fin.append(Test6)
    # Sort by Prio
    print("Sort by Prio:")
    Fin.sort(key=lambda x: x.ReturnPriority(), reverse=False)
    for x in Fin:
        print(x)
    print("\n")

    # Sort by DueDate
    print("Sort by DueDate:")
    for x in SortByDate(Fin):
        print(x)
