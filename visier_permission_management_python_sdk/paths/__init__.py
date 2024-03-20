# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from visier_permission_management_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_ADMIN_CAPABILITIES = "/v1/admin/capabilities"
    V1_ADMIN_CAPABILITIES_CAPABILITY_ID = "/v1/admin/capabilities/{capabilityId}"
    V1_ADMIN_CONTENTPACKAGES = "/v1/admin/content-packages"
    V1_ADMIN_CONTENTPACKAGES_CONTENT_PACKAGE_ID = "/v1/admin/content-packages/{contentPackageId}"
    V1_ADMIN_DATASECURITYOBJECTS = "/v1/admin/data-security-objects"
    V1_ADMIN_PERMISSIONS = "/v1/admin/permissions"
    V1_ADMIN_PERMISSIONS_PERMISSION_ID = "/v1/admin/permissions/{permissionId}"
