# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import visier_permission_management_python_sdk
from visier_permission_management_python_sdk.paths.v1_admin_permissions import get
from visier_permission_management_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1AdminPermissions(ApiTestMixin, unittest.TestCase):
    """
    V1AdminPermissions unit test stubs
        Retrieve a list of all permissions
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
