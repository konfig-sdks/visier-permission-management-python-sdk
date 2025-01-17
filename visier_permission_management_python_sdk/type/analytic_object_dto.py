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

from visier_permission_management_python_sdk.type.related_analytic_object_dto import RelatedAnalyticObjectDTO
from visier_permission_management_python_sdk.type.securable_dimension_dto import SecurableDimensionDTO
from visier_permission_management_python_sdk.type.securable_property_dto import SecurablePropertyDTO

class RequiredAnalyticObjectDTO(TypedDict):
    pass

class OptionalAnalyticObjectDTO(TypedDict, total=False):
    # The unique ID of the analytic object.
    analyticObjectId: str

    # An identifiable name to display in Visier, such as \"Employee\".
    displayName: str

    # The analytic object type.
    objectType: str

    # The analytic objects related to the data security object.
    relatedObjects: typing.List[RelatedAnalyticObjectDTO]

    # All available properties from the data security object and its related analytic objects that you can configure data access for.
    securableProperties: typing.List[SecurablePropertyDTO]

    # A list of dimensions that are available to define population access filters in the permission.
    securableDimensions: typing.List[SecurableDimensionDTO]

class AnalyticObjectDTO(RequiredAnalyticObjectDTO, OptionalAnalyticObjectDTO):
    pass
