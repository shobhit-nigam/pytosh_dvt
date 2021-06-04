# operator overloading

class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(self.hours, "hour and", self.minutes, "minutes")


first = time(1, 35)
second = time(0, 50)


