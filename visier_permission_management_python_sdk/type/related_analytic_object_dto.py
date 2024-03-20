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


class RequiredRelatedAnalyticObjectDTO(TypedDict):
    pass

class OptionalRelatedAnalyticObjectDTO(TypedDict, total=False):
    # The analytic object ID.
    analyticObjectId: str

    # An identifiable analytic object name to display in Visier, such as \"Recognition\".
    displayName: str

class RelatedAnalyticObjectDTO(RequiredRelatedAnalyticObjectDTO, OptionalRelatedAnalyticObjectDTO):
    pass
