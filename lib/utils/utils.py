import binascii
import os
import struct


class FileUtils:
    @staticmethod
    def file_exist(full_path_to_file):
        if os.path.exists(full_path_to_file) and os.path.isfile(full_path_to_file):
            return True
        else:
            return False


class XMLUtils:
    TS_XMLNS = "{http://www.kuju.com/TnT/2003/Delta}"

    @staticmethod
    def ts_attrib(node, key):
        lookup = "{}{}".format(XMLUtils.TS_XMLNS, key)
        return node.attrib.get(lookup, None)


class MathUtils:
    @staticmethod
    def double_to_hex(f):
        x = hex(struct.unpack("<Q", struct.pack("<d", f))[0])[2:-1]
        return ("0" + "".join(reversed([x[i : i + 2] for i in range(0, len(x), 2)]))).upper()

    @staticmethod
    def hex_to_double(hx):
        return struct.unpack("d", binascii.unhexlify(hx))[0]
