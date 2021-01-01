# -*- coding: utf-8 -*-


from sal_conversion import join_data
from sal_conversion import filter_data_set
import unittest


class TestSalCon(unittest.TestCase):

    def  test_join_dataSet(self):
        salData = {"array": [{ "salaryInIDR": 4.001111510555328e6, "id": 1 }]}
        userData = [{"id": 1, "name": "Leanne Graham", "username": "Bret", "email": "Sincere@april.biz"}]
        result = join_data(userData,salData)
        self.assertEqual(result, [{"id": 1, "name": "Leanne Graham", "username": "Bret", "email": "Sincere@april.biz","salaryInIDR": 4.001111510555328e6}]) 

    def  test_filter_data_set(self):
        salData = [{"id": 1,"name": "Leanne Graham","username": "Bret","email": "Sincere@april.biz","address": {"street": "Kulas Light","suite": "Apt. 556","city": "Gwenborough","zipcode": "92998-3874","geo": {"lat": "-37.3159","lng": "81.1496"}},"phone": "1-770-736-8031 x56442","website": "hildegard.org","company": {"name": "Romaguera-Crona","catchPhrase": "Multi-layered client-server neural-net","bs": "harness real-time e-markets"},"salaryInIDR": 4001111.510555328,"salaryInUSD": 283.30656175846497}]
        result = filter_data_set(salData)
        self.assertEqual(result, [{"id": 1,"name": "Leanne Graham","username": "Bret","email": "Sincere@april.biz","address": {"street": "Kulas Light","suite": "Apt. 556","city": "Gwenborough","zipcode": "92998-3874","geo": {"lat": "-37.3159","lng": "81.1496"}},"phone": "1-770-736-8031 x56442","salaryInIDR": 4001111.510555328,"salaryInUSD": 283.30656175846497}]) 

if __name__ == '__main__':
    unittest.main()