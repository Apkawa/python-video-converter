#!/usr/bin/env python

# modify the path so that parent directory is in it
import sys

sys.path.append('../')

import random
import string
import shutil
import unittest
import os
from os.path import join as pjoin

from converter import ffmpeg, formats, avcodecs, Converter, ConverterError




class TestParseOpts(unittest.TestCase):


    @staticmethod
    def ensure_notexist(f):
        if os.path.exists(f):
            os.unlink(f)

    def test_unsharp_parse(self):
        c = Converter()

        self.assertEqual(c.parse_options({
            "format": "avi",
            "video": {
                "codec": "h264",
                "unsharp": 1.0
            }
        }), ['-an', '-vcodec', 'libx264', '-vf',
             'unsharp=luma_amount=1.0:luma_msize_y=5:luma_msize_x=5',
             '-sn', '-f', 'avi'] )



if __name__ == '__main__':
    unittest.main()
