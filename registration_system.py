import json
import random

from advisor import Advisor
from student import Student



class RegistrationSystem(object):

    def __init__(self):
        self.data = {}
        self.total_students = [0] * 4
        self.names = []
        self.surnames = []
        self.advisors = []
        self.students = []
        
    def start_simulation(self):
        self.read_input()
        self.read_names()
        self.init_advisors()
        self.init_students()

    def read_input(self):
        file = open("inputs/input.json", "r")
        self.data = json.load(file)

    def read_names(self):
        names_file = open("inputs/names.json", "r")
        surnames_file = open("inputs/surnames.json", "r")
        names = json.load(names_file)
        surnames = json.load(surnames_file)

        self.names = names.get("names")
        self.surnames = surnames.get("surnames")
        
    def get_rand_name(self):
        name = random.choice(self.names)
        surname = random.choice(self.surnames)
        return name + " " + surname

    def init_advisors(self):
        advisor_count = self.data.get("Advisors")
        
        for i in range(advisor_count):
            name = self.get_rand_name()
            self.advisors.append(Advisor(name))

    def init_students(self):
        first_year = self.data.get("1stYearStudents")
        second_year = self.data.get("2ndYearStudents")
        third_year = self.data.get("3rdYearStudents")
        fourth_year = self.data.get("4thYearStudents")
        
        self.init_students_by_count(1, first_year)
        self.init_students_by_count(2, second_year)
        self.init_students_by_count(3, third_year)
        self.init_students_by_count(4, fourth_year)
        
    def init_students_by_count(self, year, count):
        for i in range(count):
            name = self.get_rand_name()
            student = Student(name, year, self.total_students[year - 1], self)
            self.students.append(student)
            self.total_students[year - 1] += 1
            
            
    
        

sys = RegistrationSystem()
sys.start_simulation()
