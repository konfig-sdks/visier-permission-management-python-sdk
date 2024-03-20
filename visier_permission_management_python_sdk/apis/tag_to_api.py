import typing_extensions

from visier_permission_management_python_sdk.apis.tags import TagValues
from visier_permission_management_python_sdk.apis.tags.permission_management_api import PermissionManagementApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PERMISSION_MANAGEMENT: PermissionManagementApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PERMISSION_MANAGEMENT: PermissionManagementApi,
    }
)
