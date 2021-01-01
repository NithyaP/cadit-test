# -*- coding: utf-8 -*-


from sensor_agg import get_agg_data
import unittest
import pandas as pd
from pandas._testing import assert_frame_equal

class TestJoinDataSet(unittest.TestCase):

    def  test_get_agg_data(self):
        senData = [{"temperature": 21.279782079384667,"humidity": 87.2525512400796,"roomArea": "roomArea1","id": 1,"dayDate":"Friday"}]
        senData = pd.DataFrame.from_dict(senData)
        sdType ='humidity'
        agg = 'min'
        result = get_agg_data(senData,sdType,agg)
        requiredDf = pd.DataFrame.from_dict([{"min_humidity": 87.2525512400796,"roomArea": "roomArea1","dayDate":"Friday"}])
        assert_frame_equal(result.sort_index(axis=1),requiredDf.sort_index(axis=1)) 

if __name__ == '__main__':
    unittest.main()