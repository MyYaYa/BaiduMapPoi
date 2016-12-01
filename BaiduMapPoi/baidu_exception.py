# -*- coding: utf-8 -*-

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class PlaceApiError(Error):

    def __init__(self, status):
        self.status = status

class GeoApiError(Error):

    def __init__(self, status):
        self.status = status
