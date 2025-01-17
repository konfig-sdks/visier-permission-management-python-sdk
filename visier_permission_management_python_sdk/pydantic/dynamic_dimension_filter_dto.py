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

from visier_permission_management_python_sdk.pydantic.dynamic_dimension_filter_dto_subject_reference_path import DynamicDimensionFilterDTOSubjectReferencePath
from visier_permission_management_python_sdk.pydantic.dynamic_property_mapping_dto import DynamicPropertyMappingDTO

class DynamicDimensionFilterDTO(BaseModel):
    # The dimension ID associated with the dynamic dimension filter.
    dimension_id: typing.Optional[str] = Field(None, alias='dimensionId')

    subject_reference_path: typing.Optional[DynamicDimensionFilterDTOSubjectReferencePath] = Field(None, alias='subjectReferencePath')

    # A list of objects representing the dynamic property mappings associated with the dynamic dimension filter.
    dynamic_property_mappings: typing.Optional[typing.List[DynamicPropertyMappingDTO]] = Field(None, alias='dynamicPropertyMappings')
    class Config:
        arbitrary_types_allowed = True
