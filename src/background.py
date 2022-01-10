from datetime import date
from time import time, time_ns
import math
import random


# MONTLE, The slightly more advanced ToDo List
# Every month has 30.42 days, fuck u
todays_date = date.today()  #  todays_date.year, todays_date.month todays_date.day

"""

    #Add, Remove, edit Tasks 
        #Add
            #Check if EVERY INPUT IS VALID
                #Day, Month, Year, Time
            #Make it so it doesn't need ANY OF these but can just have 1
            
        #Remove
        #Edit
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
            Add SPECIFIC SCHEDUALE EVENTS, ROUNTINE TASKS 
                Every Sat 5-6 Tennis. Prio(-inf)
                Separate List from Fin
                ^Not adding because you already have a calender for that, don't need to automate because
            Assign your self a study period
            Tick off if you actually did it, if you didn't, input your excuse
            Sort By Date working off the time as well
            Setting a task to be only be completed on certain days
"""


class Empty:
    def ReturnName(self):
        return "Need more cards"

    def __str__(self):
        return "Need more cards"


class Card:
    # Edit CreateCard() for every change here
    def __init__(self, Name, Day=None, Month=None, Year=None, Time=None, Priority=None):
        self._Name = Name
        self._Tags = {}
        self._CustomTagList = {}
        self._ManualPrio = False
        self.SetDueDate(Day, Month, Year)
        if Priority:  # If a prio is manually given
            self._Priority = int(Priority)
            self._ManualPrio = True
        elif Day or Month or Year:  # unless they are all none
            self._Priority = self.DateAllocatedPriorityer()
        else:
            self._Priority = math.inf

        if Time:
            self._DueTime = Time
        else:
            self._DueTime = "HH:MM"

    # Returns a priority number for "Assigned tasks" depending on how close it is to the due date
    def DateAllocatedPriorityer(self):
        """
        IF PRIO NOT GIVEN, HIGHER THE NUMBER = not important. Returns the day difference
        "2", "01", "2022"
        """
        # IF IN THE PAST
        if self._Year:
            if self._Year < todays_date.year:
                return math.inf
        if self._Month and self._Year:
            if self._Month < todays_date.month and self._Year == todays_date.year:
                return math.inf
        if self._Day and self._Month and self._Year:
            if (
                self._Day < todays_date.day
                and self._Month == todays_date.month
                and self._Year == todays_date.year
            ):
                return math.inf
        # None cases, assumes next possible date
        if (
            not self._Day and not self._Month
        ):  # if self._day and self._Month are None, Year must be something1
            if self._Year > todays_date.year:
                return int(
                    (365 * (self._Year - todays_date.year))
                    - (
                        todays_date.month * 30.42
                        + todays_date.day
                        - (30.42 - todays_date.day)
                    )
                )
            if self._Year == todays_date.year:
                return 15  
        if not self._Day and not self._Year:
            if self._Month > todays_date.month:
                return int((30.42 * self._Month) - (30.42 * todays_date.month))
            if self._Month < todays_date.month:
                return int((30.42 * self._Month) + (365 - 30.42 * todays_date.month))
            if self._Month == todays_date.month:
                return 10
        if not self._Month and not self._Year:
            if self._Day >= todays_date.day:
                return int(self._Day - todays_date.day)
            if self._Day < todays_date.day:
                return int(self._Day + (30.42 - todays_date.day))

        # None Cases if singular
        if not self._Day:
            YearDiff = self._Year - todays_date.year
            MonthDiff = (self._Month + (12 * YearDiff)) - (todays_date.month)
            if MonthDiff == 0:
                return 10
            else:
                return int(MonthDiff * 30.42)
        if not self._Month:
            if self._Day == todays_date.day:
                if self._Year > todays_date.year:
                    return 365 * (self._Year - todays_date.year)
                elif self._Year == todays_date.year:
                    return 0
            if self._Day > todays_date.day:
                if self._Year > todays_date.year:
                    return (
                        self._Day
                        - todays_date.day
                        + 365 * (self._Year - todays_date.year)
                    )
                elif self._Year == todays_date.year:
                    return self._Day - todays_date.day
            if self._Day < todays_date.day:
                if self._Year > todays_date.year:
                    return int(
                        self._Year
                        + 30.42
                        - todays_date.day
                        + 365 * (self._Year - todays_date.year)
                    )
                if self._Year == todays_date.year:
                    return int(self._Year + 30.42 - todays_date.day)
        if not self._Year:
            if self._Year > todays_date.year:
                return (
                    365 * self._Year
                    - todays_date.month * 30.45
                    - 30.45
                    - todays_date.day
                )
            if self._Year == todays_date.year:
                return 15
        # All dates Provided

        else:
            YearDiff = self._Year - todays_date.year  # *365

            if self._Month < todays_date.month:
                MonthDiff = 12 - todays_date.month + self._Month
            else:
                MonthDiff = self._Month - todays_date.month

            if self._Day < todays_date.day:
                DayDiff = self._Day + (30.42 - todays_date.day)
                MonthDiff -= 1
            else:
                DayDiff = self._Day - todays_date.day
            return int(YearDiff * 365 + MonthDiff * 30.42 + DayDiff)

    # All Independant Variables, somewhat a helper for DateAllocatedPriorityer() (DAPer!)
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

    def ReturnManualPrio(self):
        return self._ManualPrio

    # EditCard helpers
    def CgName(self, CgName):
        self._Name = CgName

    def CgDay(self, CgDay):
        self._Day = CgDay
        self.SetDueDate(self._Day, self._Month, self._Year)

    def CgMonth(self, CgMonth):
        self._Month = CgMonth
        self.SetDueDate(self._Day, self._Month, self._Year)

    def CgYear(self, CgYear):
        self._Year = CgYear
        self.SetDueDate(self._Day, self._Month, self._Year)

    def CgTime(self, CgTime):
        self._DueTime = CgTime

    def CgPrio(self, CgPrio):
        self._Priority = CgPrio
        self._ManualPrio = True

    def ResetPrio(self):
        self._Priority = self.DateAllocatedPriorityer()
        self._ManualPrio = False

    def __str__(self):
        Details = "on {} at {} (Prio:{})".format(
            self._DueDate, self._DueTime, self._Priority
        )

        if len(self._Name) < 20:
            c = 20
            whitespaces = " " * (c - len(self._Name))
        else:
            whitespaces = " "
        return "'{}'{}{}".format(self._Name, whitespaces, Details)

    def __repr__(self):
        return self._Name


# External Sorting
def SortByDate(Fin):
    DateTrue = []
    DateFalse = []
    for i in Fin:
        if i.ReturnDateBol():
            DateTrue.append(i)
        else:
            DateFalse.append(i)
    DateTrue.sort(key=lambda x: x.DateAllocatedPriorityer())
    DateFalse.sort(key=lambda x: x.ReturnName(), reverse=False)
    return DateTrue + DateFalse


def RemoveByName(Name, Fin):
    for i in Fin:
        if i.ReturnName() == Name:
            Fin.remove(i)


# Multipurposed Function that will be called separate times for checking every variable
def CreationCheck(Fin=None, Name=None, Day=None, Month=None, Year=None, Time=None):
    try:
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
            if 24 < int(Hours) and int(Hours) < 0:
                print("Get the right hours")
                return False
            if 60 < int(Minutes) and int(Minutes) < 0:
                print("Get the right minutes.")
                return False
        return True
    except ValueError:
        print("numbers go into the number parts please")
        return False


def EditCard(
    Fin,
    Name,
    CgName=None,
    CgDay=None,
    CgMonth=None,
    CgYear=None,
    CgTime=None,
    CgPrio=None,
    ResetPrio=None,
):
    for i in Fin:
        if i.ReturnName() == Name:
            if CgName:
                i.CgName(CgName)
            if CgDay:
                i.CgDay(CgDay)
            if CgMonth:
                i.CgMonth(CgMonth)
            if CgYear:
                i.CgYear(CgYear)
            if CgTime:
                i.CgTime(CgTime)
            if CgPrio:
                i.CgPrio(CgPrio)
            if ResetPrio:
                i.ResetPrio()
            return


def RemoveCard(Fin, RemoveName):
    for i in Fin:
        if i.ReturnName() == RemoveName:
            Fin.remove(i)
    return Fin


def SortByPriority(Fin):
    return sorted(Fin, key=lambda x: x.ReturnPriority(), reverse=False)


def TtGenerate(Fin, Times):  # Returns Timetable str
    Time = TtSetTimes(Times)
    EventProbList = TtProbListGen(Fin, Times)
    Events = TtTimetableImportant(Fin, Time)
    if not EventProbList:
        EventProbList.append(Empty())
    if len(Events) < Time * 3:
        for i in range(Time * 3 - len(Events)):
            Events.append(random.choice(EventProbList))
    return Events


def TtProbListGen(Fin, Times):
    # Generates the list of events that will randomly s
    EventProbList = []
    TempFin = sorted(Fin, key=lambda x: x.ReturnPriority(), reverse=True)
    TempHold = []
    TempPrio = math.inf
    c = 1

    # Creating the list to choose events from
    for i in TempFin:
        try:
            if i.DateAllocatedPriorityer() < 4:
                continue
        except TypeError:
            pass
        if i.ReturnPriority() >= TempPrio - 7:
            TempHold.append(i)
        else:
            TempPrio = i.ReturnPriority()
            EventProbList += TempHold * c
            c += 1
            TempHold = []
            TempHold.append(i)
    EventProbList += TempHold * c
    return EventProbList


def TtTimetableImportant(Fin, Time):
    Events = []
    # Emegency Events # Time complexities hate me
    Prio1 = [x for x in Fin if x.ReturnPriority() == 0]
    Prio2 = [x for x in Fin if x.ReturnPriority() == 1]
    Prio3 = [x for x in Fin if x.ReturnPriority() == 2]
    # Prio4 = [x for x in Fin if x.ReturnPriority() == 3]

    # Day 1
    if Prio1:
        Events += [Prio1[0]] * Time
    elif Prio2:
        Events += [Prio2[0]] * Time
    elif Prio3:
        Events += [Prio3[0]] * Time
    # Day 2
    if Prio2:
        Events += [Prio2[0]] * Time
    elif Prio3:
        Events += [Prio3[0]] * Time
    # Day 3
    if Prio3:
        Events += [Prio3[0]] * Time

    return Events


def TtSetTimes(times):
    # Returns a number of 30 minute subjects needed to fill through the next 3 days
    # Times is possibly a list of tuples [("00:00", "03:00"), ()]
    TotalHours = []
    for TimeFrames in times:
        Hours, Minutes = TimeFrames[0].split(":")
        Hours1, Minutes = TimeFrames[1].split(":")
        TotalHours.append(int(Hours1) - int(Hours))
    return sum(TotalHours) * 2


def TtUpdate(Events, Fin, RemoveName, Times):
    Fin = RemoveCard(Fin, RemoveName)
    # ProbEventList = TtProbListGen(Fin, Time)
    TempEvents = TtGenerate(Fin, Times)
    if TempEvents:
        for i in Events:
            if i.ReturnName() == RemoveName:
                # Events.remove(i)
                index = Events.index(i)
                Events[index] = TempEvents[index]
    return Events


def AddTime(Hr, Min):
    if int(Min) == 30:
        return int(Hr) + 1, "00"
    else:
        return Hr, 30


def PythonTerminalPrint(events, Times):  # Helper function for TtGenerate()
    # 30 lines 120 characters
    if not events or not Times:
        print(" " * 42, "TimeTable Invalid\n")
        print(" " * 34, "Please input cards and timeframes")
        return
    Time = TtSetTimes(Times)

    print(" " * 50, "TimeTable\n")
    # [("00:00", "03:00"), ("14:00", "17:00")]
    c = 0
    Hr, Min = Times[0][0].split(":")
    Hr = int(Hr)

    for i in range(Time):
        if int(Hr) < 10:
            Spaces = 30
        else:
            Spaces = 29
        print(" " * Spaces, "{}:{}".format(Hr, Min), " " * 16, events[i])
        Hr, Min = AddTime(Hr, Min)
        try:
            TempHr, TempMin = map(int, Times[c][1].split(":"))
            if int(Hr) == TempHr and int(Min) == TempMin:
                c += 1
                Hr, Min = Times[c][0].split(":")
        except IndexError:
            continue


# never bug checked but probably works
def DailyPriorityUpdate(Fin, SavedEvents, SavedDay, SavedTimes):

    if SavedDay != todays_date.day:
        for i in Fin:
            if not i.ReturnManualPrio():
                TempPrio = i.ReturnPriority()
                i.ResetPrio()
                if i.ReturnPriority() > TempPrio or i.ReturnPriority() < 0:
                    Fin.remove(i)
    Time = TtSetTimes(SavedTimes)
    if len(SavedEvents) > Time * 2:
        TempEvents = TtGenerate(Fin, SavedTimes)
        while len(SavedEvents) > Time * 2:
            SavedEvents.pop()
        while len(SavedEvents) < Time * 3:
            SavedEvents.append(random.choice(TempEvents))
    return Fin, SavedEvents, SavedTimes


def PrintControls(w, Fin, Events, Times):
    if w == "MainMenu":
        print(
            """
Input 1) Create card
Input 2) Remove a Card
Input 3) Add Timeframes
Input 4) Remove Timeframes
Input  ) Save and Exit
        """
        )
    elif w == "CreateCard":
        Name = False
        while not Name:
            print("Input) Name")
            Name = input()
        print("Input) Day (DueDate) (DD/MM/YYYY) ")
        Day = input()
        print("Input) Month (DueDate) (MM/YYYY) ")
        Month = input()
        print("Input) Year (DueDate) (YYYY) ")
        Year = input()
        print("Input) Time due (HH:MM in 24 hour)")
        Time = input()
        print("Input) Manual Priority")
        Prio = input()

        if CreationCheck(Fin, Name, Day, Month, Year, Time):
            return Card(Name, Day, Month, Year, Time, Prio)
        return
    elif w == "RemoveCard":
        Fin = SortByPriority(Fin)
        for c, i in enumerate(Fin):
            print(f" {c+1}) ", " " * 27, i)
        if len(Fin) != 0:
            Temp = input()
            if Temp:
                if int(Temp) <= len(Fin) and int(Temp) > 0:
                    Events = TtUpdate(
                        Events, Fin, Fin.pop(int(Temp) - 1).ReturnName(), Times
                    )
        return Fin, Events
    elif w == "Timeframes":
        print("Input) Start time (HH:MM) in 24 hours")
        temp = input()

        try:
            hrs, mins = temp.split(":")
            if (
                len(str(int(hrs))) in (1, 2)
                and len(str(int(mins))) in (1, 2)
                and int(mins) in (30, 0)
                and int(hrs) < 24
                and int(hrs) >= 0
            ):
                print("Input) End time (HH:MM) in 24 hours")
                temp1 = input()
                hrs1, mins1 = temp.split(":")
                if (
                    len(str(int(hrs1))) in (1, 2)
                    and len(str(int(mins1))) in (1, 2)
                    and int(mins1) in (30, 0)
                    and int(hrs1) < 24
                    and int(hrs1) >= 0
                    and int(hrs) <= int(hrs1)
                ):
                    if int(hrs) == int(hrs1) and int(mins) > int(mins1):
                        print("Start time isn't stop time")
                        return None
                    return (temp, temp1)
                else:
                    print("Wrong.")
            else:
                print("wrong")
        except ValueError:
            print("Wrong.")
            return None

    elif w == "RTimeframes":
        for c, i in enumerate(Times):
            print(f" {c+1}) ", " " * 27, i)
        if len(Times) != 0:
            Temp = input()
            if Temp:
                if int(Temp) <= len(Times) and int(Temp) > 0:
                    Times.pop(c)
                    print("removing time")
                    return Times
                else:
                    print("Could not")


def Save(Fin, Events, SavedDay, Times):
    import pickle

    Save = open("assets/TestSave", "wb")
    wow = (Fin, Events, SavedDay, Times)
    pickle.dump(wow, Save)
    Save.close()


# Test1 = Card("Montle", "10", "01", "2022", "12:30")
# Test2 = Card("Test2", "010", "03", "2022", "12:30")
# Test3 = Card("Test3", "29", "01", "2022", None)
# Fin = [Test1, Test2, Test3]


if __name__ == "__main__":
    # import pickle
    # pickle.dump(LobbyArt, open("MapSaveFile", "wb"))
    # ThePlayer = pickle.load(open("PlayerSaveFile", "rb"))

    # Card(Name, Day=None, Month=None, Year=None, Time=None, Priority=None):)
    Fin = []
    Test1 = Card("Montle", "09", "01", "2022")
    print(Test1)
    print(Test1.ReturnPriority(), "\n")

    Test2 = Card(
        "Test2",
        "010",
        "03",
        "2022",
        "12:30",
    )
    print(Test2)
    print(Test2.ReturnPriority(), "\n")

    if CreationCheck(Fin, "Test3", None, None, None, "11:34"):
        Test3 = Card("Test3", "29", "01", "2022", None)
        print(Test3)
        print(Test3.ReturnPriority(), "\n")
        Fin = [Test1, Test2, Test3]

    if CreationCheck(Fin, "Test4", "2", "01", "2022", "00:00"):
        Test4 = Card("Test4", "2", "01", "2022", "00:00")
        Fin = [Test1, Test2, Test3, Test4]
    if CreationCheck(Fin, "Test5", None, "08", None, "00:00"):
        Test5 = Card("Test5", None, "08", None, "00:00")
        Fin.append(Test5)
    if CreationCheck(Fin, "Test6", "09", None, None, "00:00"):
        Test6 = Card("Test6", "11", None, None, "00:00", 7)
        Fin.append(Test6)
    # Sort by Prio
    print("Sort by Prio:")
    for x in SortByPriority(Fin):
        print(x)
    print("\n")

    # Sort by DueDate
    print("Sort by DueDate:")
    for x in SortByDate(Fin):
        print(x)

    if CreationCheck(Fin, None, None, None, 2096, None):
        EditCard(Fin, "Test5", None, None, None, 2096, None, None, True)

    # print("Sort by DueDate:")
    # for x in SortByDate(Fin):
    #     print(x)

    # Timetabling! # ONLY READS FOR ONE HOURS TIMEFRAMES
    print("\n")
    Times = [("00:00", "03:00")]
    Events = TtGenerate(Fin, Times)
    for i in Events:
        print(i)

    print("\n")
    Events = TtUpdate(Events, Fin, "Montle", Times)
    Times = [("00:00", "03:00"), ("14:00", "17:00")]
    for i in Events:
        print(i)

    # DailyPriorityUpdate(Events, 3)
    print("\n")
    for i in Events:
        print(i)

    # To python terminal perfection
    Times = [("00:00", "03:00"), ("14:00", "17:00")]
    PythonTerminalPrint(TtGenerate(Fin, Times), Times)

    input()
