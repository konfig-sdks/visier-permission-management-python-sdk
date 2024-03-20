# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from visier_permission_management_python_sdk import VisierPermissionManagement

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        visierpermissionmanagement = VisierPermissionManagement(
        
                        api_key_auth = 'YOUR_API_KEY',
        
            access_token = 'YOUR_BEARER_TOKEN',
        
                        cookie_auth = 'YOUR_API_KEY',
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',,
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(visierpermissionmanagement)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()