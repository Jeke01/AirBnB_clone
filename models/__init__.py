#!/usr/bin/python3
"""Dis is the Module for FileStorage autoinit."""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
