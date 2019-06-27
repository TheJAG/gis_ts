import xml.etree.ElementTree as _et

from lib.tracks_bin_reader import TracksBinReader


class Tracks:
    def __init__(self, tracks_bin):
        ns = {'t': "http://www.kuju.com/TnT/2003/Delta"}

        self.tracks_xml = TracksBinReader(tracks_bin).read_as_xml()
        tree = _et.parse(self.tracks_xml)
        root = tree.getroot()
        print(root.tag)
        print(root.attrib)
        for record in root:
            for network_c_track_network in record:
                TrackNetwork(network_c_track_network)


class TrackNetwork:
    def __init__(self, xml_node):
        for items in xml_node:
            print(items)

    class NetworkID:
        def __init__(self, xml_node):

