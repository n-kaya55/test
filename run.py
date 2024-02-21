from student import Student
from teacher import Teacher

ogrenciListesi=[]
ogretmenListesi=[]

def addStudent(isim,soyisim,vize,final):
    
    newStudent=Student(isim,soyisim,vize,final)
    ogrenciListesi.append(newStudent)
    
    
def printStudent():
    for student in ogrenciListesi:
        print(student.bilgi())
        print(student.ortalamaHesaplama())

def addTeacher(isim,soyisim,bolum,maas,zamOrani):
    newTeacher=Teacher(isim,soyisim,bolum,maas,zamOrani)
    ogretmenListesi.append(newTeacher)

def printTeacher():
    for teacher in ogretmenListesi:
        print(teacher.bilgi())
        print(f"zamli maas=", teacher.zamliMaas())


    

addStudent("Nesibe","Kaya",70,80)
addStudent("kevser","Yilmaz",100,80)
addTeacher("Ozlem","Akman","matematik",10000,30)
addTeacher("Emir","Yilmaz","fizik",12000,20)

printStudent()
printTeacher()