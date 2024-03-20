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


class AnalyticObjectDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            analyticObjectId = schemas.StrSchema
            displayName = schemas.StrSchema
            
            
            class objectType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'enum'
                    enum_value_to_name = {
                        "Event": "EVENT",
                        "Subject": "SUBJECT",
                        "BusinessOutcomeOverlay": "BUSINESS_OUTCOME_OVERLAY",
                        "PlanOrBudgetOverlay": "PLAN_OR_BUDGET_OVERLAY",
                        "ExternalBenchmark": "EXTERNAL_BENCHMARK",
                        "VisierBenchmark": "VISIER_BENCHMARK",
                        "UsageOverlay": "USAGE_OVERLAY",
                        "OtherOverlay": "OTHER_OVERLAY",
                        "InternalComparison": "INTERNAL_COMPARISON",
                        "PlanAnalyticObject": "PLAN_ANALYTIC_OBJECT",
                    }
                
                @schemas.classproperty
                def EVENT(cls):
                    return cls("Event")
                
                @schemas.classproperty
                def SUBJECT(cls):
                    return cls("Subject")
                
                @schemas.classproperty
                def BUSINESS_OUTCOME_OVERLAY(cls):
                    return cls("BusinessOutcomeOverlay")
                
                @schemas.classproperty
                def PLAN_OR_BUDGET_OVERLAY(cls):
                    return cls("PlanOrBudgetOverlay")
                
                @schemas.classproperty
                def EXTERNAL_BENCHMARK(cls):
                    return cls("ExternalBenchmark")
                
                @schemas.classproperty
                def VISIER_BENCHMARK(cls):
                    return cls("VisierBenchmark")
                
                @schemas.classproperty
                def USAGE_OVERLAY(cls):
                    return cls("UsageOverlay")
                
                @schemas.classproperty
                def OTHER_OVERLAY(cls):
                    return cls("OtherOverlay")
                
                @schemas.classproperty
                def INTERNAL_COMPARISON(cls):
                    return cls("InternalComparison")
                
                @schemas.classproperty
                def PLAN_ANALYTIC_OBJECT(cls):
                    return cls("PlanAnalyticObject")
            
            
            class relatedObjects(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RelatedAnalyticObjectDTO']:
                        return RelatedAnalyticObjectDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['RelatedAnalyticObjectDTO'], typing.List['RelatedAnalyticObjectDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'relatedObjects':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RelatedAnalyticObjectDTO':
                    return super().__getitem__(i)
            
            
            class securableProperties(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SecurablePropertyDTO']:
                        return SecurablePropertyDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SecurablePropertyDTO'], typing.List['SecurablePropertyDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'securableProperties':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SecurablePropertyDTO':
                    return super().__getitem__(i)
            
            
            class securableDimensions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SecurableDimensionDTO']:
                        return SecurableDimensionDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SecurableDimensionDTO'], typing.List['SecurableDimensionDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'securableDimensions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SecurableDimensionDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "analyticObjectId": analyticObjectId,
                "displayName": displayName,
                "objectType": objectType,
                "relatedObjects": relatedObjects,
                "securableProperties": securableProperties,
                "securableDimensions": securableDimensions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analyticObjectId"]) -> MetaOapg.properties.analyticObjectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectType"]) -> MetaOapg.properties.objectType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relatedObjects"]) -> MetaOapg.properties.relatedObjects: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["securableProperties"]) -> MetaOapg.properties.securableProperties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["securableDimensions"]) -> MetaOapg.properties.securableDimensions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["analyticObjectId", "displayName", "objectType", "relatedObjects", "securableProperties", "securableDimensions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analyticObjectId"]) -> typing.Union[MetaOapg.properties.analyticObjectId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectType"]) -> typing.Union[MetaOapg.properties.objectType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relatedObjects"]) -> typing.Union[MetaOapg.properties.relatedObjects, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["securableProperties"]) -> typing.Union[MetaOapg.properties.securableProperties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["securableDimensions"]) -> typing.Union[MetaOapg.properties.securableDimensions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["analyticObjectId", "displayName", "objectType", "relatedObjects", "securableProperties", "securableDimensions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        analyticObjectId: typing.Union[MetaOapg.properties.analyticObjectId, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        objectType: typing.Union[MetaOapg.properties.objectType, str, schemas.Unset] = schemas.unset,
        relatedObjects: typing.Union[MetaOapg.properties.relatedObjects, list, tuple, schemas.Unset] = schemas.unset,
        securableProperties: typing.Union[MetaOapg.properties.securableProperties, list, tuple, schemas.Unset] = schemas.unset,
        securableDimensions: typing.Union[MetaOapg.properties.securableDimensions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AnalyticObjectDTO':
        return super().__new__(
            cls,
            *args,
            analyticObjectId=analyticObjectId,
            displayName=displayName,
            objectType=objectType,
            relatedObjects=relatedObjects,
            securableProperties=securableProperties,
            securableDimensions=securableDimensions,
            _configuration=_configuration,
            **kwargs,
        )

from visier_permission_management_python_sdk.model.related_analytic_object_dto import RelatedAnalyticObjectDTO
from visier_permission_management_python_sdk.model.securable_dimension_dto import SecurableDimensionDTO
from visier_permission_management_python_sdk.model.securable_property_dto import SecurablePropertyDTO
