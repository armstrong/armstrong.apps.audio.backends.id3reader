import unittest
from .id3proxy import Id3readerBackend

class Id3ReaderTestCase(unittest.TestCase):
    filetype = 'mp3'
    audio_metadata = {'album': u'from the internet',
                     'title': u'im chargin my laser',
                     'artist': u'armstrong',
                     'genre': u'Satire',
                     'date': u'2011',
                     'tracknumber': u'1'}
    backend=Id3readerBackend()
    def setUp(self):
        self.file = open('test_audio_files/test.mp3','rb+')

    def test_metadata(self):
        """
        confirm that the extracted metadata matches the expected values
        """
        metadata = self.backend.metadata(file=self.file)
        for fieldname, value in self.audio_metadata.items():
            self.assertEqual( value, metadata[fieldname])

    def test_filetype(self):
        """
        confirm expected filetype 
        """
        filetype = self.backend.filetype(file=self.file)
        self.assertEqual(self.filetype, filetype)

    def runTest(self):
        self.test_metadata()
        self.test_filetype()
