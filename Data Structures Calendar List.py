import tkinter as tk
import unittest
from tkinter import messagebox, simpledialog
from datetime import datetime
from plyer import notification

#Establishing Classes
class Event:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

class Calendar:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event_name, rank):
        new_event = Event(event_name, rank)
        self.events.append(new_event)

    def insertion_sort(self):
        for i in range(1, len(self.events)):
            key = self.events[i]
            j = i - 1
            while j >= 0 and key.rank < self.events[j].rank:
                self.events[j + 1] = self.events[j]
                j -= 1
            self.events[j + 1] = key

    def display_events(self):
        for event in self.events:
            print(f"Event: {event.name}, Rank: {event.rank}")

class CalendarApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.business_calendar = Calendar("Business")
        self.academic_calendar = Calendar("Academic")
        self.personal_calendar = Calendar("Personal")

        self.title("Calendar App")

        # Create buttons for adding events and displaying notifications
        business_button = tk.Button(self, text="Add Business Event", command=lambda: self.add_event("Business"))
        academic_button = tk.Button(self, text="Add Academic Event", command=lambda: self.add_event("Academic"))
        personal_button = tk.Button(self, text="Add Personal Event", command=lambda: self.add_event("Personal"))
        display_button = tk.Button(self, text="Display Notifications", command=lambda:self.display_notifications)

        # Pack widgets
        business_button.pack(pady=5)
        academic_button.pack(pady=5)
        personal_button.pack(pady=5)
        display_button.pack(pady=10)

    def add_event(self, calendar_name):
        event = self.get_event_from_user(f"Enter {calendar_name} event:")
        if event:
            rank = self.get_rank_from_user(f"Enter rank for {event} (1 to 5):")
            if rank:
                getattr(self, f"{calendar_name.lower()}_calendar").add_event(event, rank)
                messagebox.showinfo("Event Added", f"Event '{event}' added to {calendar_name} calendar.")

    def get_event_from_user(self, prompt):
        event = simpledialog.askstring("Event", prompt)
        return event

    def get_rank_from_user(self, prompt):
        rank = simpledialog.askinteger("Rank", prompt, minvalue=1, maxvalue=5)
        return rank

    def display_notifications(self):
        self.sort_calendars()
        self.show_notifications(self.business_calendar, "Business")
        self.show_notifications(self.academic_calendar, "Academic")
        self.show_notifications(self.personal_calendar, "Personal")

    def sort_calendars(self):
        self.business_calendar.insertion_sort()
        self.academic_calendar.insertion_sort()
        self.personal_calendar.insertion_sort()

    def show_notifications(self, calendar, calendar_name):
        for event in calendar.events:
            self.show_notification(event.name, calendar_name, event.rank)

    def show_notification(self, event, calendar_name, rank):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        message = f"Notification for {calendar_name} Calendar:\nEvent: {event}\nRank: {rank}\nTime: {current_time}"
        notification.notify(
            title=f"{calendar_name} Calendar Notification",
            message=message,
            app_name="Calendar App"
        )
class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.business_calendar = Calendar("Business")
        self.personal_calendar = Calendar("Personal")
        self.personal_calendar = Calendar("Academic")

        self.title("Calendar App")

        # Add events to calendars
        #self.business_calendar.add_event("Meeting A", 1, "10:00 AM")
        #self.business_calendar.add_event("Conference B", 2, "02:00 PM")
        #self.business_calendar.add_event("Project C", 3, "04:30 PM")

        #self.personal_calendar.add_event("Gym Session X", 1, "08:00 AM")
        #self.personal_calendar.add_event("Dinner Y", 2, "07:00 PM")
        #self.personal_calendar.add_event("Movie Night Z", 3, "09:00 PM")

        # Display buttons for each calendar
        business_button = tk.Button(self, text="Business Calendar", command=self.show_business_notification)
        personal_button = tk.Button(self, text="Personal Calendar", command=self.show_personal_notification)
        academic_button = tk.Button(self, text="Academic Calendar", command=self.show_academic_notification)

        business_button.pack(pady=10)
        personal_button.pack(pady=10)
        academic_button.pack(pady=10)

    def show_business_notification(self):
        events = self.business_calendar.get_sorted_events()
        for event, details in events:
            show_notification(event, "Business")

    def show_personal_notification(self):
        events = self.personal_calendar.get_sorted_events()
        for event, details in events:
            show_notification(event, "Personal")

if __name__ == "__main__":
    app = CalendarApp()
    app.mainloop()


# Unit test clas
import unittest
class TestCalendarApp(unittest.TestCase):
    def setUp(self):
        self.app = CalendarApp()
        self.business_calendar = self.app.business_calendar
        self.academic_calendar = self.app.academic_calendar
        self.personal_calendar = self.app.personal_calendar

    def test_add_event(self):
        self.business_calendar.add_event("Meeting", 3)
        self.academic_calendar.add_event("Study Session", 4)
        self.personal_calendar.add_event("Gym", 2)

        self.assertEqual(len(self.business_calendar.events), 1)
        self.assertEqual(len(self.academic_calendar.events), 1)
        self.assertEqual(len(self.personal_calendar.events), 1)

    def test_sort_calendars(self):
        self.business_calendar.add_event("Meeting", 3)
        self.business_calendar.add_event("Presentation", 2)
        self.business_calendar.add_event("Lunch", 5)
        self.business_calendar.add_event("Conference", 1)

        self.academic_calendar.add_event("Study Session", 4)
        self.academic_calendar.add_event("Exam", 2)
        self.academic_calendar.add_event("Research", 5)
        self.academic_calendar.add_event("Project", 1)

        self.personal_calendar.add_event("Gym", 2)
        self.personal_calendar.add_event("Dinner", 5)
        self.personal_calendar.add_event("Movie Night", 3)
        self.personal_calendar.add_event("Travel", 1)

        self.app.sort_calendars()

        self.assertEqual(self.business_calendar.events[0].rank, 1)
        self.assertEqual(self.business_calendar.events[1].rank, 2)
        self.assertEqual(self.business_calendar.events[2].rank, 3)
        self.assertEqual(self.business_calendar.events[3].rank, 5)

        self.assertEqual(self.academic_calendar.events[0].rank, 1)
        self.assertEqual(self.academic_calendar.events[1].rank, 2)
        self.assertEqual(self.academic_calendar.events[2].rank, 4)
        self.assertEqual(self.academic_calendar.events[3].rank, 5)

        self.assertEqual(self.personal_calendar.events[0].rank, 1)
        self.assertEqual(self.personal_calendar.events[1].rank, 2)
        self.assertEqual(self.personal_calendar.events[2].rank, 3)
        self.assertEqual(self.personal_calendar.events[3].rank, 5)

if __name__ == "__main__":
    unittest.main()


