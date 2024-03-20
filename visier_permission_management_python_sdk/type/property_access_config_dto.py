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

from visier_permission_management_python_sdk.type.property_access_config_dto_analytic_object_reference_paths import PropertyAccessConfigDTOAnalyticObjectReferencePaths

class RequiredPropertyAccessConfigDTO(TypedDict):
    pass

class OptionalPropertyAccessConfigDTO(TypedDict, total=False):
    # The property ID associated with the property access configuration.
    propertyId: str

    # The analytic object ID of the property.
    analyticObjectId: str

    analyticObjectReferencePaths: PropertyAccessConfigDTOAnalyticObjectReferencePaths

    # The access level of the property. Valid values are: Aggregate, Sensitive
    accessLevel: str

class PropertyAccessConfigDTO(RequiredPropertyAccessConfigDTO, OptionalPropertyAccessConfigDTO):
    pass