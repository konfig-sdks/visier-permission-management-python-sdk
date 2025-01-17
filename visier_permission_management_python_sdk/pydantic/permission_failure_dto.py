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
from pydantic import BaseModel, Field, RootModel

from visier_permission_management_python_sdk.pydantic.permission_error_dto import PermissionErrorDTO

class PermissionFailureDTO(BaseModel):
    # The unique identifier associated with the permission.
    permission_id: typing.Optional[str] = Field(None, alias='permissionId')

    # An identifiable permission name to display in Visier, such as \"Diversity Access\".
    display_name: typing.Optional[str] = Field(None, alias='displayName')

    # The error associated with the failure.
    error: typing.Optional[PermissionErrorDTO] = Field(None, alias='error')
    class Config:
        arbitrary_types_allowed = True
