from datetime import datetime

from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Groups(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    students: Mapped[list["Students"]] = relationship(
        "Students", back_populates="group", cascade="all, delete-orphan")


class Students(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey("groups.id", ondelete="CASCADE"))

    group: Mapped[Groups] = relationship("Groups", back_populates="students")
    grades: Mapped[list["Grades"]] = relationship("Grades", back_populates="student")


class Teachers(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    subject: Mapped[list["Subjects"]] = relationship("Subjects", back_populates="teacher")
    grades: Mapped[list["Grades"]] = relationship("Grades", back_populates="teacher")


class Subjects(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("teachers.id"), nullable=True)

    teacher: Mapped[Teachers] = relationship("Teachers", back_populates="subjects")


class Grades(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    received_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    student: Mapped[Students] = relationship("Students", back_populates="grades")
    teacher: Mapped[Teachers] = relationship("Teachers", back_populates="grades")
