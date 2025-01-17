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

from visier_permission_management_python_sdk.pydantic.hierarchy_property_dto import HierarchyPropertyDTO
from visier_permission_management_python_sdk.pydantic.securable_dimension_dto_analytic_object_ids import SecurableDimensionDTOAnalyticObjectIds

class SecurableDimensionDTO(BaseModel):
    # The dimension ID.
    dimension_id: typing.Optional[str] = Field(None, alias='dimensionId')

    # An identifiable dimension name to display in Visier, such as \"Contract Type\".
    display_name: typing.Optional[str] = Field(None, alias='displayName')

    analytic_object_ids: typing.Optional[SecurableDimensionDTOAnalyticObjectIds] = Field(None, alias='analyticObjectIds')

    # The list of hierarchies you can map to a user in a permission's dynamic filter.
    hierarchy_properties: typing.Optional[typing.List[HierarchyPropertyDTO]] = Field(None, alias='hierarchyProperties')
    class Config:
        arbitrary_types_allowed = True
