import typing_extensions

from visier_permission_management_python_sdk.paths import PathValues
from visier_permission_management_python_sdk.apis.paths.v1_admin_capabilities import V1AdminCapabilities
from visier_permission_management_python_sdk.apis.paths.v1_admin_capabilities_capability_id import V1AdminCapabilitiesCapabilityId
from visier_permission_management_python_sdk.apis.paths.v1_admin_content_packages import V1AdminContentPackages
from visier_permission_management_python_sdk.apis.paths.v1_admin_content_packages_content_package_id import V1AdminContentPackagesContentPackageId
from visier_permission_management_python_sdk.apis.paths.v1_admin_data_security_objects import V1AdminDataSecurityObjects
from visier_permission_management_python_sdk.apis.paths.v1_admin_permissions import V1AdminPermissions
from visier_permission_management_python_sdk.apis.paths.v1_admin_permissions_permission_id import V1AdminPermissionsPermissionId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ADMIN_CAPABILITIES: V1AdminCapabilities,
        PathValues.V1_ADMIN_CAPABILITIES_CAPABILITY_ID: V1AdminCapabilitiesCapabilityId,
        PathValues.V1_ADMIN_CONTENTPACKAGES: V1AdminContentPackages,
        PathValues.V1_ADMIN_CONTENTPACKAGES_CONTENT_PACKAGE_ID: V1AdminContentPackagesContentPackageId,
        PathValues.V1_ADMIN_DATASECURITYOBJECTS: V1AdminDataSecurityObjects,
        PathValues.V1_ADMIN_PERMISSIONS: V1AdminPermissions,
        PathValues.V1_ADMIN_PERMISSIONS_PERMISSION_ID: V1AdminPermissionsPermissionId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ADMIN_CAPABILITIES: V1AdminCapabilities,
        PathValues.V1_ADMIN_CAPABILITIES_CAPABILITY_ID: V1AdminCapabilitiesCapabilityId,
        PathValues.V1_ADMIN_CONTENTPACKAGES: V1AdminContentPackages,
        PathValues.V1_ADMIN_CONTENTPACKAGES_CONTENT_PACKAGE_ID: V1AdminContentPackagesContentPackageId,
        PathValues.V1_ADMIN_DATASECURITYOBJECTS: V1AdminDataSecurityObjects,
        PathValues.V1_ADMIN_PERMISSIONS: V1AdminPermissions,
        PathValues.V1_ADMIN_PERMISSIONS_PERMISSION_ID: V1AdminPermissionsPermissionId,
    }
)
