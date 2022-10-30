#!/usr/bin/python3
"""
Define FileStorage, FileStorage` class is loaded with all objects on the
`__file_path` class attribute of the `FileStorage` class.

"""


from models.engine.file_storage  import FileStorage

storage = FileStorage()
storage.reload()
