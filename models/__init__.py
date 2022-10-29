#!/usr/bin/python3
"""
Define FileStorage

FileStorage` class is loaded with all objects on the
`__file_path` class attribute of the `FileStorage` class.
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
