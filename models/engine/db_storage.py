#!/usr/bin/python3
from os import getenv
from sqlalchemy import text


class DBStorage:
    """ New Engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of DBStorage class """
        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(getenv('HBNB_MYSQL_USER'),
                                                    getenv('HBNB_MYSQL_PWD'),
                                                    getenv('HBNB_MYSQL_HOST')
                                                    getenv('HBNB_MYSQL_DB')),
        pool_pre_ping=True)
        if get_env('HBNB_ENV') is 'test':
            Base.metada.drop_all(self.__engine)

    def all(self, cls=None):
        dic = {}
        if cls:
            for obj in self.__session.query(cls).all():
                dic[type(obj).__name__ + "." + obj.id] = obj
        else:
                for obj in self.__session.\
                query(Use0r, State, City, Amenity, Place, Review).\
                all():
                dic[type(obj).__name__ + "." + obj.id] = obj
        return dic
    
    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()
