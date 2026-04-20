import datetime
import sqlalchemy

from .db_session import SqlAlchemyBase

class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    status = sqlalchemy.Column(sqlalchemy.String)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              unique=True,
                              index=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    # created_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                  default=datetime.datetime.now)

