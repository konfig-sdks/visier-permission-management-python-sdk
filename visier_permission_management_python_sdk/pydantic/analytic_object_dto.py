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

from visier_permission_management_python_sdk.pydantic.related_analytic_object_dto import RelatedAnalyticObjectDTO
from visier_permission_management_python_sdk.pydantic.securable_dimension_dto import SecurableDimensionDTO
from visier_permission_management_python_sdk.pydantic.securable_property_dto import SecurablePropertyDTO

class AnalyticObjectDTO(BaseModel):
    # The unique ID of the analytic object.
    analytic_object_id: typing.Optional[str] = Field(None, alias='analyticObjectId')

    # An identifiable name to display in Visier, such as \"Employee\".
    display_name: typing.Optional[str] = Field(None, alias='displayName')

    # The analytic object type.
    object_type: typing.Optional[Literal["Event", "Subject", "BusinessOutcomeOverlay", "PlanOrBudgetOverlay", "ExternalBenchmark", "VisierBenchmark", "UsageOverlay", "OtherOverlay", "InternalComparison", "PlanAnalyticObject"]] = Field(None, alias='objectType')

    # The analytic objects related to the data security object.
    related_objects: typing.Optional[typing.List[RelatedAnalyticObjectDTO]] = Field(None, alias='relatedObjects')

    # All available properties from the data security object and its related analytic objects that you can configure data access for.
    securable_properties: typing.Optional[typing.List[SecurablePropertyDTO]] = Field(None, alias='securableProperties')

    # A list of dimensions that are available to define population access filters in the permission.
    securable_dimensions: typing.Optional[typing.List[SecurableDimensionDTO]] = Field(None, alias='securableDimensions')
    class Config:
        arbitrary_types_allowed = True
