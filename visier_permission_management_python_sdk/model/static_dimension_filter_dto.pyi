# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from visier_permission_management_python_sdk import schemas  # noqa: F401


class StaticDimensionFilterDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            dimensionId = schemas.StrSchema
        
            @staticmethod
            def subjectReferencePath() -> typing.Type['StaticDimensionFilterDTOSubjectReferencePath']:
                return StaticDimensionFilterDTOSubjectReferencePath
            
            
            class memberSelections(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MemberSelectionDTO']:
                        return MemberSelectionDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MemberSelectionDTO'], typing.List['MemberSelectionDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'memberSelections':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MemberSelectionDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "dimensionId": dimensionId,
                "subjectReferencePath": subjectReferencePath,
                "memberSelections": memberSelections,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dimensionId"]) -> MetaOapg.properties.dimensionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subjectReferencePath"]) -> 'StaticDimensionFilterDTOSubjectReferencePath': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memberSelections"]) -> MetaOapg.properties.memberSelections: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dimensionId", "subjectReferencePath", "memberSelections", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dimensionId"]) -> typing.Union[MetaOapg.properties.dimensionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subjectReferencePath"]) -> typing.Union['StaticDimensionFilterDTOSubjectReferencePath', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memberSelections"]) -> typing.Union[MetaOapg.properties.memberSelections, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dimensionId", "subjectReferencePath", "memberSelections", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dimensionId: typing.Union[MetaOapg.properties.dimensionId, str, schemas.Unset] = schemas.unset,
        subjectReferencePath: typing.Union['StaticDimensionFilterDTOSubjectReferencePath', schemas.Unset] = schemas.unset,
        memberSelections: typing.Union[MetaOapg.properties.memberSelections, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StaticDimensionFilterDTO':
        return super().__new__(
            cls,
            *args,
            dimensionId=dimensionId,
            subjectReferencePath=subjectReferencePath,
            memberSelections=memberSelections,
            _configuration=_configuration,
            **kwargs,
        )

from visier_permission_management_python_sdk.model.member_selection_dto import MemberSelectionDTO
from visier_permission_management_python_sdk.model.static_dimension_filter_dto_subject_reference_path import StaticDimensionFilterDTOSubjectReferencePath
