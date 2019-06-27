import os
import subprocess

from pathlib import Path
from lib.utils.utils import FileUtils


class BinXmlConverter:
    def __init__(self, file_name):
        # type (str) -> None
        pass

    @staticmethod
    def bin_to_xml(input_file):
        # type (str) -> str
        return BinXmlConverter._serz_it(input_file, "xml")

    @staticmethod
    def xml_to_bin(input_file):
        # type (str) -> str
        return BinXmlConverter._serz_it(input_file, "bin")

    @staticmethod
    def _serz_it(input_file, to_type):
        # type (str, str) -> str
        serz_exe_path = os.path.abspath("../../../bin/serz.exe")
        if FileUtils.file_exist(input_file):
            output_file = str(Path(input_file).with_suffix(".{}".format(to_type)))
            command = '%s "%s" /%s:"%s"' % (serz_exe_path, input_file, to_type, output_file)
            subprocess.call(command)
            return output_file
        else:
            msg = "Can't find input file '{}'".format(input_file)
            raise (IOError(msg))
