# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from visier_permission_management_python_sdk.paths.v1_admin_permissions.post import CreatePermissionsRaw
from visier_permission_management_python_sdk.paths.v1_admin_permissions.delete import DeletePermissionsRaw
from visier_permission_management_python_sdk.paths.v1_admin_capabilities.get import GetCapabilitiesRaw
from visier_permission_management_python_sdk.paths.v1_admin_capabilities_capability_id.get import GetCapabilityRaw
from visier_permission_management_python_sdk.paths.v1_admin_content_packages_content_package_id.get import GetContentPackageRaw
from visier_permission_management_python_sdk.paths.v1_admin_content_packages.get import GetContentPackagesRaw
from visier_permission_management_python_sdk.paths.v1_admin_data_security_objects.get import GetDataSecurityObjectsRaw
from visier_permission_management_python_sdk.paths.v1_admin_permissions_permission_id.get import GetPermissionRaw
from visier_permission_management_python_sdk.paths.v1_admin_permissions.get import GetPermissionsRaw
from visier_permission_management_python_sdk.paths.v1_admin_permissions.put import UpdatePermissionsRaw


class PermissionManagementApiRaw(
    CreatePermissionsRaw,
    DeletePermissionsRaw,
    GetCapabilitiesRaw,
    GetCapabilityRaw,
    GetContentPackageRaw,
    GetContentPackagesRaw,
    GetDataSecurityObjectsRaw,
    GetPermissionRaw,
    GetPermissionsRaw,
    UpdatePermissionsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass