# operator overloading

class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(self.hours, "hour and", self.minutes, "minutes")

    def __add__(self, other):
        m1 = self.hours*60 + self.minutes
        m2 = other.hours*60 + other.minutes
        mtotal = m1+m2

        temp = time()
        temp.hours = mtotal//60
        temp.minutes = mtotal%60
        return temp

    def __lt__(self, other):
        m1 = self.hours*60 + self.minutes
        m2 = other.hours*60 + other.minutes
        return m1 < m2

first = time(1, 35)
second = time(0, 50)


