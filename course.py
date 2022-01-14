from abc import ABC

class Course(ABC):
    
    def __init__(self, course_code, quota, credit, theoretical, practical):
        self.__course_code = course_code
        self.__quota = quota
        self.__credit = credit
        self.__theoretical = theoretical
        self.__practical = practical
        self.__course_section = None
        self.__non_registered_collision = set()
        self.__non_registered_quota = set()

    def is_elligible_past_course(self, student):
        stu_transcript = student.transcript
        return not stu_transcript.has_passed_course(self) ##If student hasn't passed this course yet

    def when_requested(self, student):
        collided_sections = student.schedule.collided_hours(self.course_section)
        if student.schedule.is_collision(self.course_section):
            student.logging += "\nAdvisor didn't approve " + self.__str__() +  " because of more than one hour collision with "
            student.logging += [cs.course.__str__() + " " for cs in collided_sections]
            student.logging += "in schedule"
            self.non_registered_students.add(student)

    def total_hours(self):
        return self.theoretical + self.practical

    def getSectionHours(self):
        return self.__theoretical + self.__practical

    def getCourseCode(self):
        return self.__courseCode

    def getQuota(self):
        return self.__quota

    def getCredits(self):
        return self.__credits

    def getTheoretical(self):
        return self.__theoretical

    def getPractical(self):
        return self.__practical

    def getRegistrationSystem(self):
        """
        registrationSystem tanımlandığında return edilecek
        """

    def getCourseSection(self):
        """
        courseSection tanımlandığında return edilecek
        """

    def getNonRegisteredCollision(self, nonRegisteredCollision):
        """
            nonRegisteredCollision (Student) tanımlandığında return edilecek
        """

    def getNonRegisteredQuota(self):
        """
            nonRegisteredQuota (Student) tanımlandığında return edilecek
        """

    def setNonRegisteredQuota(self, nonRegisteredQuota):
        """
            nonRegisteredQuota (Student) tanımlandığında set edilecek
        """

    def setCourseSection(self, courseSection):
        """
            courseSection tanımlandığında set edilecek
        """

    def toString(self):
        """
            courseSection tanımlandığında return edilecek
        """
    
    def __str__(self):
        return self.course_code
        
    
    