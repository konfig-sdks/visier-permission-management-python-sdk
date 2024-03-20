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

from visier_permission_management_python_sdk.pydantic.analytic_object_dto import AnalyticObjectDTO

class GetDataSecurityObjectsAPIResponseDTO(BaseModel):
    # A list of analytic objects and their related objects that are available to define data access to.
    analytic_objects: typing.Optional[typing.List[AnalyticObjectDTO]] = Field(None, alias='analyticObjects')
    class Config:
        arbitrary_types_allowed = True