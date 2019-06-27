import os
import unittest

from lib.tracks import Tracks


class TracksTest(unittest.TestCase):
    def setUp(self):
        tracks_bin_file = "../sample_data/tracks_bin - curved.xml"
        self.tracks = Tracks(tracks_bin_file)

    def test_something(self):
        pass
