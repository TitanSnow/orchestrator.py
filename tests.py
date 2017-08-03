import unittest

def suite():
    return unittest.defaultTestLoader.loadTestsFromNames(['sequencify.test'])

__all__ = ('suite',)
