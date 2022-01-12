class Grade:
    def __init__(self,intGrade,course):
        self.intGrade=intGrade
        self.course=course

    def getLetterGrade(self):
        self.letterGrade=""
        if self.intGrade<0 and self.intGrade >100:
            print("Grades should be between 0-100!!")
        elif self.intGrade<=44:
            self.letterGrade="FF"
        elif self.intGrade<=49:
            self.letterGrade="FD"
        elif self.intGrade <= 54:
            self.letterGrade = "DD"
        elif self.intGrade <= 64:
            self.letterGrade = "DC"
        elif self.intGrade <= 74:
            self.letterGrade = "CC"
        elif self.intGrade <= 79:
            self.letterGrade = "CB"
        elif self.intGrade <= 84:
            self.letterGrade = "BB"
        elif self.intGrade <= 89:
            self.letterGrade = "BA"

        else:
            self.letterGrade="AA"

        return self.letterGrade

    def getintGrade(self):
        return  self.intGrade
    
'''    def Course getCourse(self):
        return self.course

    def setCourse(Course course):
        self.course=course
'''








