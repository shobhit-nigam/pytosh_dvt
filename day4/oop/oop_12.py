# inheritance

class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it secure")

class linux(unix):
    def free(self):
        print("linux is free")




