from datetime import date

todays_date = date.today()  #  todays_date.year, todays_date.month todays_date.day


class Card:
    def __init__(self, Name):
        self._Name = Name
        self._Tags = {}
        self._CustomTagList = {}
        # {Tag name: priority} # The highest priority will be used
        self._DueDate = None
        self._DueTime = None
        self._Time = None  # Not used in prototype
        self._Day = None
        self._Month = None
        self._Year = None

    # Assigns Tag
    def TagAssign(self, Tag):
        if Tag.lower() in self._CustomTagList.keys():  # Custom Tags are used first
            self._Tags.append(Tag)
        elif Tag.lower() in ("hobby", "h", "fun"):
            self._Tags["Hobby"] = 6
        elif Tag.lower() in ("assigned", "homework", "work", "a"):
            self._Tags["Assigned"] = "DatePriority"
        elif Tag.lower() in ("regular", "chore", "tutor"):
            self._Tags["Regular"] = 0
        else:
            print(
                "{} not set. Please select an existing Tag ({})".format(
                    Tag,
                    " ".join(
                        ["Hobby", "Assigned", "Repeatively"] + self._CustomTagList
                    ),
                )
            )

    # Returns a priority number for "Assigned tasks" depending on how close it is to the due date
    def DatePriorityAllocater(self):

        # Within 3 days, Red, 8
        # Within 1 week, Orange, 7
        # Within 2 weeks, Green, 5

        # Prototype version just looks at month year and day difference
        # Within 2 month, 5
        # Within 1 month, 7
        # Within 1 week, 8
        # Not within this year or next year, 3
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

    # Function that returns the highest priority
    def HighestPriority(self):
        highest = float("-inf")
        for Tag in self._Tags.values:
            if Tag == "DatePriority":
                if self._DueDate == None:
                    continue
                DatePrio = self.DatePriorityAllocater()
                if highest < DatePrio():
                    highest = DatePrio
            elif highest < Tag:
                highest = Tag
        return highest

    # Overrides existing tag prios
    def SeyCustomTag(self, CustomTagName, CustomTagPrio):
        self._CustomTagList[CustomTagName] = CustomTagPrio

    def RemoveCustomTag(self, CustomTagName):
        if CustomTagName in self._CustomTagList.keys():
            self._CustomTagList.pop("CustomTagName")
        else:
            print('Custom tag "', CustomTagName, '" does not exist')

    # Checks if the inputted date checks out. *(Should they be able to input a date in the past?, should we auto delete events that already happened?)
    def DueDateChecker(self, Time, Day, Month, Year):
        # Checks if the designated inputs actually make sense and returns the error message if it doesn't.
        # You can store dates in the past however, for whatever reason
        # if it works, AddDueDate here too

        self.AddDueDate(Time, Day, Month, Year)

    def SetDueDate(self, Time, Day, Month, Year):
        self._DueDate = "{} on {} / {} / {}".format(Time, Day, Month, Year)
        self._Time = Time
        self._Day = Day
        self._Month = Month
        self._Year = Year

    def __str__(self):
        return "Task {} at {}".format(self._Name, self._DueDate)


if __name__ == "__main__":
    import pickle

    while True:
        break
