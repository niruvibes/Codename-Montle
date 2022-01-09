import background as b
import pickle
from datetime import date

# TestSave = open("assets/TestSave", "wb")
# wow = "wow"
# pickle.dump(wow, TestSave)
# TestSave.close()
try:
    Save = open("assets/SavedDates", "rb")
    wow = "wow"
    Fin, Events, SavedDay, Times = pickle.load(Save)
    Save.close()
    b.DailyPriorityUpdate(Fin, Events, SavedDay, Times)
except FileNotFoundError:
    Fin = []
    Events = []
    Times = []
todays_date = date.today()

# Test
while True:  # Main Screen
    b.PythonTerminalPrint(Events, Times)
    b.PrintControls("MainMenu", Fin, Events, Times)
    b.Save(Fin, Events, todays_date.day, Times)
    Input = input()
    print("\n" * 2)
    if not Input:
        b.Save(Fin, Events, todays_date.day, Times)
        exit()
    if Input == "1":
        TempCard = b.PrintControls("CreateCard", Fin, Events, Times)

        if TempCard:
            Fin.append(TempCard)
            if Times:
                Events = b.TtGenerate(Fin, Times)
    if Input == "2":
        Fin, Events = b.PrintControls("RemoveCard", Fin, Events, Times)
    if Input == "3":
        TempTime = b.PrintControls("Timeframes", Fin, Events, Times)
        if TempTime:
            Times.append(TempTime)
    if Input == "4":
        TempTime = b.PrintControls("RTimeframes", Fin, Events, Times)

        """
Input 1) Create card
Input 2) Remove a Card
Input 3) Add Timeframes
Input 4) Remove Timeframes
        """
