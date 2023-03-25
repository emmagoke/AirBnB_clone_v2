"""This script handle data storage from and to MySQL Database."""
import os
from sqlalchemy import create_engine
import MySQLdb
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage:
    """ This Class handles storage into the MySQL Database. """
    __engine = None
    __session = None

    def __init__(self):
        """ This method is created for every instance of DbStorage. """
        user = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
        database = os.environ.get('HBNB_MYSQL_DB')
        env = os.environ.get('HBNB_ENV')

        DBStorage.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                           .format(user, password, host,
                                                   database),
                                           pool_pre_ping=True)

        # drop all tables if the environment variable HBNB_ENV is equal to test
        Base.metadata.drop_all(DBStorage.__engine)

    def all(self, cls=None):
        """
        This method returns all the rows in the database or
        row based on the Class (cls the argument).
        """
        output = {}
        if cls is not None:
            query = DBStorage.__session.query(cls).all()
            for row in query:
                key = row.__name__ + '.' + row.id
                output[key] = row
        else:
            classes = [State, City]
            for class_ in classes:
                query = DBStorage.__session.query(class_).all()
                for row in query:
                    key = row.__name__ + '.' + row.id
                    output[key] = row

        return output

    def new(self, obj):
        """ This method adds a new instance into the current session. """
        DBStorage.__session.add(obj)

    def save(self):
        """ Saves every unsaved object or changes in the session to the db. """
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the current session. """
        if obj is not None:
            DBStorage.__session.delete(obj)

    def reload(self):
        """ Creates the session to work with the database. """
        Base.metadata.create_all(DBStorage.__engine)
        session_factory = sessionmaker(bind=DBStorage.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()
