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


class RequiredContentPackageDTO(TypedDict):
    pass

class OptionalContentPackageDTO(TypedDict, total=False):
    # A description of the content package.
    description: str

    # The unique ID of the content package.
    contentPackageId: str

    # An identifiable content package name to display in Visier, such as \"Talent Acquisition Core Content\".
    displayName: str

class ContentPackageDTO(RequiredContentPackageDTO, OptionalContentPackageDTO):
    pass