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

from visier_permission_management_python_sdk.pydantic.permission_dto import PermissionDTO

class PermissionsListDTO(BaseModel):
    # The list of permissions that will be created or updated
    permissions: typing.Optional[typing.List[PermissionDTO]] = Field(None, alias='permissions')
    class Config:
        arbitrary_types_allowed = True
