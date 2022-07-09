class jaggi:
    __name= None
    __data=None
    def __init__(self,name,data):
        self.__name=name
        self.__data=data


    def __print_name(self):
       
        print("Your Name is:",self.__name)
        print("Your Sir Name Is:",self.__data)

    def access(self):

        self.__print_name()

k =jaggi("jaggi","shah")
k.access()
        