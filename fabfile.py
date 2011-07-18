import unittest
from armstrong.dev.tasks import *
from armstrong.apps.audio.backends.id3reader.tests import Id3ReaderTestCase 

test_suite = unittest.TestLoader().loadTestsFromTestCase(Id3ReaderTestCase)
