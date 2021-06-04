# inheritance

class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it secure")

class linux(unix):
    def free(self):
        print("linux is free")

    def funcx(self):
        print("x of linux")

class mobileOS:
    def portable(self):
        print("portable across machines")

    def funcx(self):
        print("x of mobileOS")
        
class android(mobileOS, linux):
    def ui(self):
        print("great ui")

