# inheritance

class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it secure")

class linux(unix):
    def free(self):
        print("linux is free")

class mobileOS:
    def portable(self):
        print("portable across machines")

class android(linux, mobileOS):
    def ui(self):
        print("great ui")
