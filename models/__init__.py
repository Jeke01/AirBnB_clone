#!/usr/bin/python3
"""
this module wil  executes wen models package is imported
"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
