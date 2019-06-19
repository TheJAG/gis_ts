import binascii
import os
import struct
import xml.etree.ElementTree as _et

from math import atan2

from lib.utils.bin_xml_converter import BinXmlConverter
from lib.utils.utils import XMLUtils, MathUtils


class TrackTiles:
    TILE_SIZE_METRES = 1024.0

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

                        length_node = curve.find("Length")
                        length_rounded = length_node.text
                        length_precise = MathUtils.hex_to_double(XMLUtils.ts_attrib(length_node, "alt_encoding"))

                        start_pos_node = curve.find("StartPos")
                        start_pos_tile_find = "cFarVector2/{}/cFarCoordinate/RouteCoordinate/cRouteCoordinate/Distance"
                        start_pos_tile_x = int(start_pos_node.find(start_pos_tile_find.format("X")).text)
                        start_pos_tile_z = int(start_pos_node.find(start_pos_tile_find.format("Z")).text)

                        start_pos_find = "cFarVector2/{}/cFarCoordinate/TileCoordinate/cTileCoordinate/Distance"
                        start_pos_x = start_pos_node.find(start_pos_find.format("X"))
                        start_pos_z = start_pos_node.find(start_pos_find.format("Z"))

                        start_pos_x_rounded = float(start_pos_x.text)
                        start_pos_x_precise = MathUtils.hex_to_double(XMLUtils.ts_attrib(start_pos_x, "alt_encoding"))
                        start_pos_z_rounded = float(start_pos_z.text)
                        start_pos_z_precise = MathUtils.hex_to_double(XMLUtils.ts_attrib(start_pos_z, "alt_encoding"))

                        global_start_pos_x = start_pos_x_precise + TrackTiles.TILE_SIZE_METRES * start_pos_tile_x
                        global_start_pos_z = start_pos_z_precise + TrackTiles.TILE_SIZE_METRES * start_pos_tile_z

                        tan1, tan2 = map(float, curve.find("StartTangent").text.split(" "))
                        angle = atan2(tan2, tan1)
                        print(angle)

                        print(
                            " | ".join(
                                map(
                                    str,
                                    [
                                        curve_type,
                                        length_precise,
                                        start_pos_tile_x,
                                        start_pos_tile_z,
                                        start_pos_x_precise,
                                        start_pos_z_precise,
                                        angle,
                                        global_start_pos_x,
                                        global_start_pos_z,
                                    ],
                                )
                            )
                        )

    def read_all_track_tiles(self):
        return [
            BinXmlConverter.bin_to_xml(os.path.join(self.track_tiles_dir, file))
            for file in os.listdir(self.track_tiles_dir)
            if file.endswith(".bin")
        ]
