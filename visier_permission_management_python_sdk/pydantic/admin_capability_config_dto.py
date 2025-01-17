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

from visier_permission_management_python_sdk.pydantic.admin_capability_config_dto_capabilities import AdminCapabilityConfigDTOCapabilities

class AdminCapabilityConfigDTO(BaseModel):
    # If true, this capability configuration grant access to all capabilities.
    all_capabilities_access: typing.Optional[bool] = Field(None, alias='allCapabilitiesAccess')

    capabilities: typing.Optional[AdminCapabilityConfigDTOCapabilities] = Field(None, alias='capabilities')
    class Config:
        arbitrary_types_allowed = True
