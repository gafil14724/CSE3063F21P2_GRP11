from abc import ABC
from elective_course import ElectiveCourse
from transcript import Transcript


class TechnicalElectiveCourse(ElectiveCourse, ABC):

    def __init__(self, course_code, quota, credits, theoretical, practical, semesters, required_credits,
                 prerequisities):
        super().__init__(course_code, quota, credits, theoretical, practical, semesters)
        self.required_credits = required_credits
        self.pre_requisities = prerequisities
        self.non_registered_students = []

    def is_eligible_past_course(self, student):
        return student.get_transcrpit().has_passed_courses(self.getPreRequisities()) and self.check_credit_condition(
            student) and super.is_elligible_past_course(student)

    def when_rejected(self, student):
        pass

    def get_random_elective(self):
        pass

    def when_requested(self, student):
        if not self.check_credit_condition(student):
            student.get_execution_trace().append("\nThe system didn't allow " + self.to_string() +
                                                 " because Student completed credits is less than " + self.required_credits +
                                                 " -> (" + student.getTranscript().getCompletedCredits() + ")")
            self.non_registered_students.append(student)
            return False
        if not student.get_transcrpit().has_passed_courses(self.pre_requisities):
            student.get_execution_trace().append("\nThe system didn't allow " + self.to_string()() +
                                                 " because student failed prerequisites -> ")
            for c in range(self.pre_requisities):
                if not student.get_transcrpit.has_passed_courses(c):
                    student.getExecutionTrace().append(c.to_string() + " ")

    def check_credit_condition(self, student):
        return student.get_transcrpit().get_complated_credits() >= self.required_credits

    def get_required_credits(self):
        return self.required_credits

    def set_required_credits(self, required_credits):
        self.required_credits = required_credits

    def get_pre_requisities(self):
        return self.preRequisites

    def set_pre_requisites(self, pre_requisites):
        self.pre_requisities = pre_requisites

    def get_non_registeredS_students(self):
        return self.non_registered_students

    def setNonRegisteredStudents(self, non_registered_students):
        self.non_registered_students = non_registered_students
