class Advisor():
    def __init__(self, name):
        self.__name = name
       
    def Advisor(self,firstName):
        self.__name = firstName;

    def approveCourseSection(self, student, courseSection):
       
        print("CourseSection bittikten sonra ...")

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
