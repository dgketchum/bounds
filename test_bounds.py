# ===============================================================================
# Copyright 2018 dgketchum
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
import os
import sys
import unittest

sys.path.append(os.path.dirname(__file__))

from bounds import RasterBounds, GeoBounds


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.image = os.path.join(os.path.dirname(__file__), 'LE07_clip_L1TP_039027_20130726_20160907_01_T1_B3.TIF')

    def test_raster(self):
        bb = RasterBounds(raster=self.image)
        self.assertEqual(bb.get_nwse_tuple(), (47.61118761194992, -111.94851161596767,
                                               47.54916612467683, -111.8361513308256))

    def test_coords_to_geographic(self):
        bb = GeoBounds(west=9085047, south=11971301, east=10104624, north=12228183)
        geo = bb.to_geographic(epsg=3857)
        self.assertAlmostEqual(geo[0], 81.612366, delta=0.01)
        self.assertAlmostEqual(geo[1], 72.595728, delta=0.01)
        self.assertAlmostEqual(geo[2], 90.771382, delta=0.01)
        self.assertAlmostEqual(geo[3], 73.272851, delta=0.01)


if __name__ == '__main__':
    unittest.main()
# ========================= EOF ====================================================================
