from student_id import StudentId
from transcript import Transcript
from schedule import Schedule
from advisor import Advisor

class Student(object):
    
    
    def __init__(self, name, current_year, registration_order, registration_system):
        self.name = name
        self.current_year = current_year
        self.registration_order = registration_order
        self.registration_system = registration_system
        self.transcript = Transcript(self)
        self.student_id = StudentId(self)
        self.semester_num = 0
        self.logging = ""
        self.schedule = Schedule(self)
        self.advisor = Advisor(self)
        self.execution_trace = ""

    def get_num_of_past_electives(self, semester_nums):
        count = 0

        for i in range(semester_nums):
            if i < self.get_semester_number():
                count += 1

        return count

    def add_to_current_courses(self, course_seciton):
        self.schedule.add_to_program(course_seciton)
        self.transcript.get_current_courses().append(course_seciton.get_course())

    def request_courses(self):
        self.execution_trace = "Current Semester Courses: \n"
        self.request_mandatory_courses()
        self.request_elective_courses()

    def request_mandatory_courses(self):
        offered_course_sections = self.registration_system.getOfferedMandatories(self)

        for c in offered_course_sections:
            self.execution_trace.__add__(c.getCourse().toString()).__add__(", ")

        self.execution_trace.__add__("\n")
        self.execution_trace.__add__("(").__add__(self.registration_system.offeredNTECount(self)).__add__(" NTE), ")
        self.execution_trace.__add__("(").__add__(self.registration_system.offeredTECount(self)).__add__(" TE), ")
        self.execution_trace.__add__("(").__add__(self.registration_system.offeredFTECount(self)).__add__(" FTE), ")
        self.execution_trace.__add__("\n")

        """
        for c in offered_course_sections:
            request_course_section(c)
        """

    def request_elective_courses(self):
        offered_courses= self.registration_system.getOfferedElectives(self)

        """
        for c in offered_courses:
            request_course_section(c)
        """

    def get_execution_trace(self):
        return self.execution_trace

    def set_execution_trace(self, execution_trace):
        self.execution_trace = execution_trace

    def get_semester_number(self):
        return self.semester_num

    def set_semester_number(self, semester_number):
        if self.registration_system.getSemester() == "FALL":
            self.semester_num = self.current_year*2-1
        elif self.registration_system.getSemester() == "SPRING":
            self.semester_num = self.current_year * 2
        else:
            print("Incorrect Semester for registration System!!")
            exit(-1)

    def get_name(self):
        return self.name

    def get_registration_order(self):
        return self.registration_order

    def get_student_id(self):
        return self.student_id.get_student_id()

    def get_current_year(self):
        return self.current_year

    def get_advisor(self):
        return self.advisor

    def set_advisor(self, advisor):
        self.advisor = advisor

    def get_schedule(self):
        return self.schedule

    def set_schedule(self, schedule):
        self.schedule = schedule

    def get_registration_system(self):
        return self.registration_system

    def get_transcrpit(self):
        return self.transcript

    def to_string(self):
        student_str = "Past Courses: \n" + self.transcript.to_string() + "\n"

        return student_str





        
        
        
        
