# schedule_manager.py
# The ScheduleManager class will hold all the information regarding who is available at what time for each day.

class ScheduleManager:
    days = []

    def __init__(self):
        days = ((),) * 7

    def add_user_availability(self, user, day, timeframe):
        print('Hello World') # Figure this out...