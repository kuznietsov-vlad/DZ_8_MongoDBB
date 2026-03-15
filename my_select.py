
from db_config import session
from sqlalchemy import func, desc
from models import Subject, Student, Teacher, Grade, Discipline, Group

if __name__ == '__main__':

    def select_1():
        result = (
            session.query(
                Student.full_name,
                func.round(func.avg(Grade.grade),2).label("avg_grade"),
            )
            .join(Grade, Grade.student_id==Student.id)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .limit(5)
            .all()
        )
        return result

    """"
    Знайти студента із найвищим середнім балом з певного предмета.
    """

    def select_2(subject_id):
        result = (
            session.query(
                Student.full_name,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
                Subject.name
            )
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Grade.subject_id == Subject.id)
            .filter(Subject.id == subject_id)
            .group_by(Student.full_name, Subject.name)
            .order_by(desc("avg_grade"))
            .first()
        )
        return result
    """"
    Знайти середній бал у групах з певного предмета.
    """
    def select_3(subject_id):
        result = (
            session.query(
                Group.name.label("group_name"),
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .join(Student, Student.group_id == Group.id)
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Grade.subject_id == Subject.id)
            .filter(Subject.id == subject_id)
            .group_by(Group.name, )
            .order_by(desc("avg_grade"))
            .all()
        )
        return result

    """"
    Знайти середній бал на потоці (по всій таблиці оцінок).
    """
    def select_4():
        result = (
            session.query(
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            ).one()
        )
        return result.avg_grade

    """"
    Знайти які курси читає певний викладач
    """
    def select_5(teacher_id):
        result=(
            session.query(
            Teacher.full_name.label("teacher_name"),
            Discipline.name.label("course_name"),
            )
        .join(Discipline, Discipline.teacher_id==Teacher.id)
        .filter(Teacher.id == teacher_id)
        .all()
        )
        return result


    """"
    Знайти список студентів у певній групі
    """
    def select_6(group_id):
        result = (
            session.query(
                Group.name.label("group_name"),
                Student.full_name.label("student_name"),
            )
            .join(Student, Student.group_id==Group.id)
            .filter(Group.id == group_id)
            .group_by(Group.name, Student.full_name)
            .all()
        )
        return result

    """"
    Знайти оцінки студентів у окремій групі з певного предметa
    """

    def select_7(subject_id, group_id):
        result = (
            session.query(
                Subject.name.label("subject_name"),
                Grade.grade.label("grade"),
                Group.name.label("group_name"),
                Student.full_name.label("student_name"),
            )
            .join(Group, Student.group_id == Group.id)
            .join(Grade, Grade.student_id ==Student.id)
            .join(Subject, Grade.subject_id == Subject.id)
            .filter(Subject.id==subject_id)
            .filter(Group.id == group_id)
            .all()
        )
        return result


    """"
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    """

    def select_8(teacher_id):
        result = (
            session.query(
                Teacher.full_name.label("teacher_name"),
                func.round(func.avg(Grade.grade), 2).label("avg_grade")
            )
            .join(Discipline, Discipline.teacher_id == Teacher.id)
            .join(Subject, Subject.discipline_id == Discipline.id)
            .join(Grade, Grade.subject_id == Subject.id)
            .filter(Teacher.id == teacher_id)
            .group_by(Teacher.full_name)
            .all()
        )

        return result


    """"
    Знайти список курсів, які відвідує певний студент.
    """
    def select_9(student_id):
        result = (
            session.query(
                Student.full_name.label("student_name"),
                Subject.name.label("subject_name")
            )
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Grade.subject_id == Subject.id)
            .filter(Student.id==student_id)
            .distinct()
            .all()

        )
        return result

    """"
    Список курсів, які певному студенту читає певний викладач.
    """

    def select_10(student_id, teacher_id):
        result = (
            session.query(
                Student.full_name.label("student_name"),
                Teacher.full_name.label("teacher_name"),
                Subject.name.label("subject_name")
            )
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Grade.subject_id == Subject.id)
            .join(Discipline, Subject.discipline_id == Discipline.id)
            .join(Teacher, Discipline.teacher_id == Teacher.id)
            .filter(Student.id == student_id)
            .filter(Teacher.id == teacher_id)
            .distinct()
            .all()

        )





