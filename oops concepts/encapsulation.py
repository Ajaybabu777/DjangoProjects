class parent :
    def __init__(self,data,name):
        self.__data=data #private
        self._name=name  #protected

class child(parent):
    def output(self):
        print(self._name)

b=child(33,"ajay")
b.output()