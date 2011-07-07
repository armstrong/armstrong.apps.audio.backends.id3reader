import unittest
from fabric.decorators import task

@task 
def test():
    from armstrong.apps.audio.backends.id3reader.tests import * 
    unittest.main()
