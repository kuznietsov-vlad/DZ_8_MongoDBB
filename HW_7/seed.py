# seed.py
from faker import Faker
import random
import datetime
from db_config import Session, engine
from models import Base, Student, Group, Teacher, Subject, Grade, Discipline


Base.metadata.create_all(engine)

session = Session()
faker = Faker()


session.query(Grade).delete()
session.query(Student).delete()
session.query(Subject).delete()
session.query(Teacher).delete()
session.query(Group).delete()
session.commit()

# --- Групи ---
groups = []
for i in range(1, 4):
    group = Group(name=f"Group {i}")
    session.add(group)
    groups.append(group)
session.commit()

# --- Викладачі ---
teachers = []
num_teachers = random.randint(3, 5)
for _ in range(num_teachers):
    teacher = Teacher(
        full_name=faker.name()
    )
    session.add(teacher)
    teachers.append(teacher)
session.commit()



#__Disciplines___

# --- Дисципліни ---
disciplines = []

for _ in range(5):
    discipline = Discipline(
        name=faker.word().capitalize(),
        teacher_id=random.choice(teachers).id
    )
    session.add(discipline)
    disciplines.append(discipline)

session.commit()
# --- Предмети ---
subjects = []

for _ in range(10):
    subject = Subject(
        name=faker.word().capitalize(),
        discipline_id=random.choice(disciplines).id  # <- беремо id з disciplines
    )
    session.add(subject)
    subjects.append(subject)

session.commit()

# --- Студенти ---
students = []
num_students = random.randint(30, 50)
for _ in range(num_students):
    student = Student(
        full_name=faker.name(),
        group_id=random.choice(groups).id
    )
    session.add(student)
    students.append(student)
session.commit()

# --- Оцінки ---
for student in students:
    for _ in range(random.randint(10, 20)):
        grade = Grade(
            student_id=student.id,
            subject_id=random.choice(subjects).id,
            grade=random.randint(1, 12),
            date_of = datetime.date.today()
        )
        session.add(grade)

session.commit()
session.close()

print("Базу даних успішно заповнено випадковими даними!")