from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(120), nullable=False)
    disciplines = relationship("Discipline", back_populates="teacher", cascade="all, delete-orphan")

class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship("Teacher", back_populates="disciplines")
    subjects = relationship("Subject", back_populates="discipline", cascade="all, delete-orphan")

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    students = relationship("Student", back_populates="group", cascade="all, delete-orphan")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(120), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE'))
    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student", cascade="all, delete-orphan")

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    discipline_id = Column(Integer, ForeignKey('disciplines.id', ondelete='CASCADE'))
    discipline = relationship("Discipline", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject", cascade="all, delete-orphan")

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column(Date, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE'))
    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")