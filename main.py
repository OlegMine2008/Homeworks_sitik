from flask import Flask


from data.db_session import global_init, create_session
from data.users import User