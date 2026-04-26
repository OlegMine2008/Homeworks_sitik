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
                                sqlalchemy.ForeignKey('user.id'))
    students = sqlalchemy.Column(sqlalchemy.Integer, 
                                sqlalchemy.ForeignKey('user.id'),
                                nullable=True)
    dayofweek = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey('week.id'))

    user = orm.relationship('User')
    week = orm.relationship('WeekDay')