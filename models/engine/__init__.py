#!/usr/bin/python3
"""
module will executes wen the  models package is or are  imported
"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
