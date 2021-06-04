class A:
    dataa = 30
    _datab = 34
    __datac = 36         # private
    __datad__ = 38

    def funca(self):
        print("dataa = ", self.dataa)
        print("_datab = ", self._datab)
        print("__datac = ", self.__datac)
        print("__datad__ = ", self.__datad__)

    def __funcb(self):
        print("hey")

    def funcc(self):
        print("in c")
        self.__funcb()

        
