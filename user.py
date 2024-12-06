class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
class Habit:
    def __init__(self, habit_name,habit_category,habit_frequency):
        self.habit_name=habit_name
        self.habit_category=habit_category
        self.habit_frequency=habit_frequency