import os

students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_students(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could Not Save File")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_students(student)
        f.close()

    except Exception:
        print("Could Not Read File")

<<<<<<< HEAD
read_file()
print_students_titlecase()


flag= True
while flag:
    print("Ingresar Datos del Estudiante")
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    add_students(student_name,student_id)
    save_file(student_name)
    
    continuarIngresandoEstudiantes = input("Deseda seguir ingresando estudiantes (S) ó (N) :")

    if (continuarIngresandoEstudiantes=="S"):
        flag=True
        os.system("cls")
        
    else:
        flag=False
        print("Lista de Estudiantes")
        print_students_titlecase()
=======

>>>>>>> a86e64df88f1af1753b73a8eaa5bf07755825974

if __name__ == "__main__":
    read_file()
    print_students_titlecase()

    bandera = True
    while bandera:
        print("Ingresar Datos del Estudiante")
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        add_students(student_name, student_id)
        save_file(student_name)

        continuarIngresandoEstudiantes = input("Deseda seguir ingresando estudiantes (S) ó (N) :")

        if (continuarIngresandoEstudiantes == "S"):
            bandera = True
            os.system("cls")

        else:
            bandera = False
            print("Lista de Estudiantes")
            print_students_titlecase()
