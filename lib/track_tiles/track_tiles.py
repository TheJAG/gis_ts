import binascii
import os
import struct
import xml.etree.ElementTree as _et

from lib.utils.bin_xml_converter import BinXmlConverter
from lib.utils.utils import XMLUtils, MathUtils


class TrackTiles:
    def __init__(self, track_tiles_dir):
        self.track_tiles_dir = track_tiles_dir

    def read_xml(self):
        ns = {"d": "http://www.kuju.com/TnT/2003/Delta"}
        track_tiles_xml_list = self.read_all_track_tiles()

        value = "000000C04E62603F"
        double = MathUtils.hex_to_double(value)
        print(double)

        hex_rep = MathUtils.double_to_hex(double)
        print(hex_rep, hex_rep == value)
        print(MathUtils.hex_to_double(hex_rep), MathUtils.hex_to_double(hex_rep) == double)

        for xml_file_name in track_tiles_xml_list:
            print(xml_file_name)
            tree = _et.parse(xml_file_name)
            root = tree.getroot()

            for ribbon_curves_container in root.findall(
                ".//Network-cNetworkRibbonUnstreamed-cCurveContainerUnstreamed"
            ):
                for ribbon in ribbon_curves_container.find("RibbonID"):
                    print(ribbon)

                for curves in ribbon_curves_container.findall(".//Curve"):
                    for curve in curves:
                        curve_type = curve.tag
                        curve_id = XMLUtils.ts_attrib(curve, "id")
                        length_rounded = 3  # rounded to 3 decimals, work with alt_encoding instead
                        length_precise = "alt_encoding equiv"
                        # print(XMLUtils.ts_attrib(ribbon_and_curve, "id"))

    def read_all_track_tiles(self):
        return [
            BinXmlConverter.bin_to_xml(os.path.join(self.track_tiles_dir, file))
            for file in os.listdir(self.track_tiles_dir)
            if file.endswith(".bin")
        ]
