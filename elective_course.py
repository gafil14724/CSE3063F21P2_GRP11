from courseourse import Course
from course_section import CourseSection
from abc import ABC, abstractmethod

class ElectiveCourse(Course, ABC):

    def __init__(self, course_code, quota, credits, theoretical, practical, semesters):
        super().__init__(course_code, quota, credits, theoretical, practical)
        self.__semesters = semesters
        Course.setCourseSection(CourseSection(self))

    def when_requested(self, student):
        if not super().when_requested(student):
            whenRejected(student)
            return False

        if not Course.get_course_section().addStudent(student):
            whenRejected(student)
            return False

    @abstractmethod
    def whenRejected(self, student):
        pass

    @abstractmethod
    def getRandomElective(self):
        pass

    def getSemesters(self):
        return self.__semesters

    def setSemesters(self, semesters):
        self.__semesters = semesters
