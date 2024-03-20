from visier_permission_management_python_sdk.paths.v1_admin_permissions.get import ApiForget
from visier_permission_management_python_sdk.paths.v1_admin_permissions.put import ApiForput
from visier_permission_management_python_sdk.paths.v1_admin_permissions.post import ApiForpost
from visier_permission_management_python_sdk.paths.v1_admin_permissions.delete import ApiFordelete


class V1AdminPermissions(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
