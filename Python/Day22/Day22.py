
#virtual
class progress1:
    def submark(self):
        print("Passed")
    def obe(self):
        print("Perfect in attitude")
class progress2(progress1):
    def submark(self):
        print("Improved frm before, Above 75% ")

m2=progress2()
m2.submark()
m2.obe()


#abstract

from abc import ABC,abstractmethod

class coursecompletion(ABC):
    
    @abstractmethod
    def techmock(self):
        pass
    
    @abstractmethod
    def aptitudemock(self):
        pass

    @abstractmethod
    def communicationmock(self):
        pass
    
class student(coursecompletion):
    def techmock(self):
        print("Technical mock completed")
    def aptitudemock(self):
        print("Aptitude mock completed")
    def communicationmock(self):
        print("Communication mock completed")
    def eligiblity(self):
        print("Course completed!")
    
r2=student()
r2.techmock()
r2.aptitudemock()
r2.communicationmock()








r2.eligiblity()
