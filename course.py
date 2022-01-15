from abc import ABC

class Course(ABC):
    
    def __init__(self, course_code, quota, credit, theoretical, practical):
        self.course_code = course_code
        self.quota = quota
        self.credit = credit
        self.theoretical = theoretical
        self.practical = practical
        self.course_section = None
        self.non_registered_collision = set()
        self.non_registered_quota = set()

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

    def get_section_hours(self):
        return self.theoretical + self.practical

    def get_course_code(self):
        return self.course_code

    def get_quota(self):
        return self.quota

    def get_credits(self):
        return self.credit

    def get_theoretical(self):
        return self.theoretical

    def get_practical(self):
        return self.practical

    def get_registration_system(self):
        pass

    def get_course_section(self):
        return self.course_section

    def get_non_registered_collision(self, nonRegisteredCollision):
        pass

    def get_non_registered_quota(self):
        pass

    def set_non_registered_quota(self, nonRegisteredQuota):
        pass

    def set_course_section(self, courseSection):
        pass

    def to_string(self):
        pass

    def __str__(self):
        return self.course_code
        
    
    