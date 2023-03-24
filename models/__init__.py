#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


db_type = os.environ.get('HBNB_TYPE_STORAGE')
if db_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
