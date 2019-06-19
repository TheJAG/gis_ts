import unittest

from lib.track_tiles.track_tiles import TrackTiles


class TracksTest(unittest.TestCase):
    def setUp(self):
        track_tiles_dir = "e:\\Games\\Train Simulator NL\\steamapps\\common\\RailWorks\\Content\\Routes\\7977fcaa-b90f-4357-8e61-51aa2f24a13d\\Networks\\Track Tiles"
        self.track_tiles = TrackTiles(track_tiles_dir)

    def test_something(self):
        self.track_tiles.read_xml()
