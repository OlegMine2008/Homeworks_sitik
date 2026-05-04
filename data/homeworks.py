import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase

class Hometask(SqlAlchemyBase):
    __tablename__ = 'homeworks'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    homework = sqlalchemy.Column(sqlalchemy.String)
    teacher = sqlalchemy.Column(sqlalchemy.Integer, 
                                sqlalchemy.ForeignKey('users.id'))
    students = sqlalchemy.Column(sqlalchemy.Integer, 
                                sqlalchemy.ForeignKey('users.id'),
                                nullable=True)
    date = sqlalchemy.Column()
    subject = sqlalchemy.Column(sqlalchemy.Integer, 
                                sqlalchemy.ForeignKey('subjects.id'))
    file = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    teacher_user = orm.relationship('User', foreign_keys=[teacher])
    student_user = orm.relationship('User', foreign_keys=[students])
