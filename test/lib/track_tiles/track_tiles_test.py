import unittest

from lib.track_tiles.track_tiles import TrackTiles


class TracksTest(unittest.TestCase):
    def setUp(self):
        track_tiles_dir = "..\\..\\sample_data\\track_tiles_simple"
        self.track_tiles = TrackTiles(track_tiles_dir)

    def test_something(self):
        self.track_tiles.read_xml()
