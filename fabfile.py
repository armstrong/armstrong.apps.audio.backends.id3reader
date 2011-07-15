import unittest
from fabric.decorators import *
from armstrong.apps.audio.backends.id3reader.tests import Id3ReaderTestCase 

@task 
def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(Id3ReaderTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
