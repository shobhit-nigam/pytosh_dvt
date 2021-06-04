# inheritance

class unix:
    def __init__(self, p):
        print("init of unix")
        self.per = p
    
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it secure")
        print("it is", self.per, "percent secure")

class linux(unix):
    def __init__(self, p):
        self.per = p
        print("init of linux")
        
    def free(self):
        print("linux is free")


# obju = unix(80)
objl = linux(80)
