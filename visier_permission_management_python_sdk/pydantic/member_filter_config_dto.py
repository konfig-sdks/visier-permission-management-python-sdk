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

from visier_permission_management_python_sdk.pydantic.dimension_filter_dto import DimensionFilterDTO

class MemberFilterConfigDTO(BaseModel):
    # A list of objects representing the dimension filters associated with the member filter configuration.  A dimension filter can be either a static or dynamic dimension filter.
    dimension_filters: typing.Optional[typing.List[DimensionFilterDTO]] = Field(None, alias='dimensionFilters')
    class Config:
        arbitrary_types_allowed = True
