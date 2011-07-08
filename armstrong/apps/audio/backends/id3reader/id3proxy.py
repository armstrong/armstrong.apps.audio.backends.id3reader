#wrapper for the id3reader.py
from id3reader import Reader

from armstrong.apps.audio.backends import AudioBackend


class Id3readerBackend(AudioBackend):
    """
        wrapper for the "don't make me regret this licensed"
        id3 reader written by Ned Batchelder
    """
    def filetype(self, file):
        if file.name.lower().rfind('.mp3') == len(file.name) - 4:
            return 'mp3'
        else:
            return 'unsupported'

    def metadata(self, file):
        """ converts the metada to a nice neat dictionary"""
        reader = Reader(file)
        return reader
