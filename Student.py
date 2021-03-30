class Student:

      def __init__(self, name, major, gpa, is_on_probation):
            self.name = name
            self.major = major
            self.gpa = gpa
            self.is_on_probation = is_on_probation

student1 = Student("Vikas", "Python", 9.8, False)
student2 = Student("Sarthak", "Python", 9.9, False)

print("The name of student is : " + student1.name + "\n"
      +"The major of " + student1.name + " is : "+ student1.major + "\n" +
      "gpa: " + str(student1.gpa) + " " + "\n" +
      "Is student on probation: " + str(student1.is_on_probation)
      )

print("*****************************************************************8")

print("The name of student is : " + student2.name + "\n"
      +"The major of " + student2.name + " is : "+ student2.major + "\n" +
      "gpa: " + str(student2.gpa) + " " + "\n" +
      "Is student on probation: " + str(student2.is_on_probation)
      )

