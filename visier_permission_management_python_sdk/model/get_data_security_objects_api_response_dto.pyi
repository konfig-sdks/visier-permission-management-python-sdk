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


class GetDataSecurityObjectsAPIResponseDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class analyticObjects(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AnalyticObjectDTO']:
                        return AnalyticObjectDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AnalyticObjectDTO'], typing.List['AnalyticObjectDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'analyticObjects':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AnalyticObjectDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "analyticObjects": analyticObjects,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analyticObjects"]) -> MetaOapg.properties.analyticObjects: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["analyticObjects", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analyticObjects"]) -> typing.Union[MetaOapg.properties.analyticObjects, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["analyticObjects", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        analyticObjects: typing.Union[MetaOapg.properties.analyticObjects, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetDataSecurityObjectsAPIResponseDTO':
        return super().__new__(
            cls,
            *args,
            analyticObjects=analyticObjects,
            _configuration=_configuration,
            **kwargs,
        )

from visier_permission_management_python_sdk.model.analytic_object_dto import AnalyticObjectDTO
