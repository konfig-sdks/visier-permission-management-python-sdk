# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from visier_permission_management_python_sdk.type.permission_error_dto import PermissionErrorDTO

class RequiredPermissionFailureDTO(TypedDict):
    pass

class OptionalPermissionFailureDTO(TypedDict, total=False):
    # The unique identifier associated with the permission.
    permissionId: str

    # An identifiable permission name to display in Visier, such as \"Diversity Access\".
    displayName: str

    # The error associated with the failure.
    error: PermissionErrorDTO

class PermissionFailureDTO(RequiredPermissionFailureDTO, OptionalPermissionFailureDTO):
    pass
