class RegisterationSystem:
    def __init__(self):
        self.startTheSımulatıon()

    def startTheSımulatıon(self):
        self.readInput()
        self.regenerateCheck()
        self.requestCourses()
        self.printRegistrationProcess()
        self.printStatistics()
        self.registrationProcessOutput()
        self.statisticsOutput()

    def readInput(self):
        print("reading ınput file")
        input_="Json Parsed text"  #input.json

        self.readGeneralInformation(input_)
        self.readMandatoryCourses(input_)
        self.readFinalProjectCourses(input_)
        self.readNonTechs(input_)
        self.readTechElectives(input_)
        self.readFacTechs(input_)


    def regenerateCheck(self):
        pass

    def requestCourses(self):
        pass

    def printRegistrationProcess(self):
        pass

    def printStatistics(self):
        pass

    def registrationProcessOutput(self):
        pass

    def statisticsOutput(self):
        pass

    def readGeneralInformation(self, input_):
        prob=0.5#json read
        self.setPassProbability(prob)
        advisorCount=20 #json read
        self.setAdvisorCount(advisorCount)
        semester=""#json read
        self.setSemester(semester)

        #regeneration checks



    def readMandatoryCourses(self, input_):
        pass

    def readFinalProjectCourses(self, input_):
        pass

    def readNonTechs(self, input_):
        pass

    def readTechElectives(self, input_):
        pass

    def readFacTechs(self, input_):
        pass

    def setPassProbability(self, prob):
        pass

    def setAdvisorCount(self, advisorCount):
        pass

    def setSemester(self, semester):
        pass

