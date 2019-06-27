import os
import xml.etree.ElementTree as _et

import pandas as pd
from math import atan2

from lib.utils.bin_xml_converter import BinXmlConverter
from lib.utils.utils import XMLUtils, MathUtils


class TrackTiles:
    TILE_SIZE_METRES = 1024.0

    # rwmapmaker-0.8.2 is used for background help
    def __init__(self, track_tiles_dir):
        self.track_tiles_dir = track_tiles_dir

    def read_xml(self):
        df = pd.DataFrame()
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

    def read_all_track_tiles(self):
        return [
            BinXmlConverter.bin_to_xml(os.path.join(self.track_tiles_dir, file))
            for file in os.listdir(self.track_tiles_dir)
            if file.endswith(".bin")
        ]


class Ribbon:
    # has many curves
    def __init__(self):
        self.ribbon_id = None
        self.ribbon_id_uuid = [0, 0]
        self.ribbon_id_dev_string = ""
        self.network_type_id_uuid = [0, 0]
        self.network_type_id_dev_string = ""
        self.curves = {}  # curve_id to Curve()

    def read_from_xml(self, xml_node):

        for curves_xml in xml_node.findall(".//Curve"):
            for curve_xml in curves_xml:
                curve = Curve().read_from_xml(curve_xml)
                self.curves[curve.curve_id] = curve


class Curve:
    # part of one ribbon
    def __init__(self):
        self.curve_type = None
        self.curve_id = None
        self.length = 0.0
        self.tile_quadrant = [0, 0]
        self.tile_start_x_z = [0.0, 0.0]
        self.start_x_z = [0.0, 0.0]
        self.start_angle = 0.0
        self.curvature = None
        self.curve_sign = None

    def read_from_xml(self, xml_node):
        self.curve_type = xml_node.tag
        self.curve_id = XMLUtils.ts_attrib(xml_node, "id")

        length_node = xml_node.find("Length")
        self.length = MathUtils.hex_to_double(XMLUtils.ts_attrib(length_node, "alt_encoding"))

        start_pos_node = xml_node.find("StartPos")

        start_pos_tile_find = "cFarVector2/{}/cFarCoordinate/RouteCoordinate/cRouteCoordinate/Distance"
        self.tile_quadrant[0] = int(start_pos_node.find(start_pos_tile_find.format("X")).text)
        self.tile_quadrant[1] = int(start_pos_node.find(start_pos_tile_find.format("Z")).text)

        start_pos_find = "cFarVector2/{}/cFarCoordinate/TileCoordinate/cTileCoordinate/Distance"
        start_pos_x = start_pos_node.find(start_pos_find.format("X"))
        start_pos_z = start_pos_node.find(start_pos_find.format("Z"))
        self.tile_start_x_z[0] = MathUtils.hex_to_double(XMLUtils.ts_attrib(start_pos_x, "alt_encoding"))
        self.tile_start_x_z[1] = MathUtils.hex_to_double(XMLUtils.ts_attrib(start_pos_z, "alt_encoding"))

        self.start_x_z[0] = self.tile_start_x_z[0] + TrackTiles.TILE_SIZE_METRES * self.tile_quadrant[0]
        self.start_x_z[1] = self.tile_start_x_z[1] + TrackTiles.TILE_SIZE_METRES * self.tile_quadrant[1]

        tan1, tan2 = map(float, xml_node.find("StartTangent").text.split(" "))
        self.start_angle = atan2(tan2, tan1)

        if self.curve_type == "cCurveArc":
            self.curvature = MathUtils.hex_to_double(XMLUtils.ts_attrib(xml_node.find("Curvature"), "alt_encoding"))
            self.curve_sign = MathUtils.hex_to_double(XMLUtils.ts_attrib(xml_node.find("CurveSign"), "alt_encoding"))

        return self

    def to_s(self):
        print(
            self.curve_type,
            self.curve_id,
            self.length,
            self.tile_quadrant,
            self.tile_start_x_z,
            self.start_x_z,
            self.start_angle,
            self.curvature,
            self.curve_sign,
        )
