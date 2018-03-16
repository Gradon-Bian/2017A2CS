## Gradon Bian S3C5 Opt1
## Task 27.08

class Assessment:
    def __init__(self, t, m):
        self.__AssessmentTitle = t
        self.__MaxMarks = m
    def OutputAssessmentDetails(self):
        print(self.__AssessmentTitle, " Marks: ",self.__MaxMarks)

class Course:
    def __init__(self, a, b): 
        self.__CourseTitle = a
        self.__MaxStudents = b
        self.__NumberOfLessons = 0
        self.__CourseLesson = []
        self.__CourseAssessment = Assessment
    def AddLesson(self, t, d, r):
        self.__NumberOfLessons = self.__NumberOfLessons + 1
        self.__CourseLesson.append(Lesson(t, d, r)) ##Got it wrong
    def AddAssessment(self, t, m):
        CourseAssessment = Assessment(t, m)
    def OutputCourseDetails(self):
        print(self.__CourseTitle, end=' ')
        print( "Maximum number of students: ",self.__MaxStudents)
        for i in range(self.__NumberOfLessons):
            print(self.__CourseLesson[i].OutputLessonDetails())
class Lesson:
    def __init__(self, t, d, r):
        self.__LessonTitle = t
        self.__DurationMinutes = d
        self.__requiresLab = r
    def OutputLessonDetails(self):
        print(self.__LessonTitle,
        self.__DurationMinutes)

MyCourse = Course("ABC", 110) 
MyCourse.AddAssessment("BCD", 123) 
MyCourse.AddLesson("WAD", 60, False)
MyCourse.AddLesson("ACD", 120, True)
MyCourse.AddLesson("ABG", 60, False)
MyCourse.OutputCourseDetails()
