import background as b
import pickle
from datetime import date
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# TestSave = open("assets/TestSave", "wb")
# wow = "wow"
# pickle.dump(wow, TestSave)
# TestSave.close()

try:
    Save = open("assets/Saved", "rb")
    Fin, Events, SavedDay, Times = pickle.load(Save)
    #SavedDay = 20
    #print(Fin, Events, SavedDay, Times)
    print(" \n")
    Save.close()
    # SavedDay = 0 # This would constantly shuffle the list
    Fin, Events, Times = b.DailyPriorityUpdate(Fin, Events, SavedDay, Times)
except FileNotFoundError:
    print("no file found")
    Fin = []
    Events = []
    Times = []

todays_date = date.today()
# Fin.append(b.Card("Montle", "10", "01", "2022", "12:30"))
# Times.append(("12:00", "14:00"))
# Test
while True:  # Main Screen
    if Fin and Times and not Events:
        Events = b.TtGenerate(Fin, Times)
    b.PythonTerminalPrint(Events, Times)
    b.PrintControls("MainMenu", Fin, Events, Times)
    Input = input()
    print("\n" * 2)
    if not Input:
        print("saving..")
        Save = open("assets/Saved", "wb")
        wow = [Fin, Events, todays_date.day, Times]
        pickle.dump(wow, Save)
        Save.close()
        # b.Save(Fin, Events, todays_date.day, Times)
        exit()
    elif Input == "1":
        TempCard = b.PrintControls("CreateCard", Fin, Events, Times)

        if TempCard:
            Fin.append(TempCard)
            Events = b.TtGenerate(Fin, Times)
            if sum(isinstance(x, b.Empty) for x in Events):
                Events = b.TtUpdate(Events, Fin, "Need more cards", Times)
        #Adding a card does not reshuffle the timetable
    elif Input == "2":
        Fin, Events = b.PrintControls("RemoveCard", Fin, Events, Times)
        if sum(isinstance(x, b.Empty) for x in Events):
            Events = b.TtUpdate(Events, Fin, "Need more cards", Times)

    elif Input == "3":
        TempTime = b.PrintControls("Timeframes", Fin, Events, Times)
        if TempTime:
            Times.append(TempTime)
    elif Input == "4":
        TempTime = b.PrintControls("RTimeframes", Fin, Events, Times)
        if TempTime:
            Times = TempTime
    elif Input == "5":
        tempTimes = Times
        Times = b.PrintControls("Default Timeframes", Fin, Events, Times)
        if tempTimes != Times:
            Events = b.TtGenerate(Fin, Times)
    elif Input == "6":
        print("Bug Fixing button")
        print(Fin, Events, SavedDay, Times)
        input()

        """
Input 1) Create card
Input 2) Remove a Card
Input 3) Add Timeframes
Input 4) Remove Timeframes
        """
