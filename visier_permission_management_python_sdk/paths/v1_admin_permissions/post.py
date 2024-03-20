# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from visier_permission_management_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from visier_permission_management_python_sdk.api_response import AsyncGeneratorResponse
from visier_permission_management_python_sdk import api_client, exceptions
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

from visier_permission_management_python_sdk.model.permission_bulk_operation_response_dto import PermissionBulkOperationResponseDTO as PermissionBulkOperationResponseDTOSchema
from visier_permission_management_python_sdk.model.status import Status as StatusSchema
from visier_permission_management_python_sdk.model.permissions_list_dto import PermissionsListDTO as PermissionsListDTOSchema
from visier_permission_management_python_sdk.model.permission_dto import PermissionDTO as PermissionDTOSchema

from visier_permission_management_python_sdk.type.permission_dto import PermissionDTO
from visier_permission_management_python_sdk.type.permissions_list_dto import PermissionsListDTO
from visier_permission_management_python_sdk.type.permission_bulk_operation_response_dto import PermissionBulkOperationResponseDTO
from visier_permission_management_python_sdk.type.status import Status

from ...api_client import Dictionary
from visier_permission_management_python_sdk.pydantic.status import Status as StatusPydantic
from visier_permission_management_python_sdk.pydantic.permission_dto import PermissionDTO as PermissionDTOPydantic
from visier_permission_management_python_sdk.pydantic.permission_bulk_operation_response_dto import PermissionBulkOperationResponseDTO as PermissionBulkOperationResponseDTOPydantic
from visier_permission_management_python_sdk.pydantic.permissions_list_dto import PermissionsListDTO as PermissionsListDTOPydantic

from . import path

# Query params
TenantCodeSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'tenantCode': typing.Union[TenantCodeSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_tenant_code = api_client.QueryParameter(
    name="tenantCode",
    style=api_client.ParameterStyle.FORM,
    schema=TenantCodeSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = PermissionsListDTOSchema


request_body_permissions_list_dto = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'ApiKeyAuth',
    'BearerAuth',
    'CookieAuth',
    'OAuth2Auth',
    'OAuth2Auth',
]
SchemaFor200ResponseBodyApplicationJson = PermissionBulkOperationResponseDTOSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PermissionBulkOperationResponseDTO


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PermissionBulkOperationResponseDTO


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = StatusSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Status


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Status


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_permissions_mapped_args(
        self,
        permissions: typing.Optional[typing.List[PermissionDTO]] = None,
        tenant_code: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if permissions is not None:
            _body["permissions"] = permissions
        args.body = _body
        if tenant_code is not None:
            _query_params["tenantCode"] = tenant_code
        args.query = _query_params
        return args

    async def _acreate_permissions_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create permissions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_tenant_code,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/admin/permissions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_permissions_list_dto.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_permissions_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create permissions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_tenant_code,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/admin/permissions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_permissions_list_dto.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreatePermissionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_permissions(
        self,
        permissions: typing.Optional[typing.List[PermissionDTO]] = None,
        tenant_code: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_permissions_mapped_args(
            permissions=permissions,
            tenant_code=tenant_code,
        )
        return await self._acreate_permissions_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def create_permissions(
        self,
        permissions: typing.Optional[typing.List[PermissionDTO]] = None,
        tenant_code: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_permissions_mapped_args(
            permissions=permissions,
            tenant_code=tenant_code,
        )
        return self._create_permissions_oapg(
            body=args.body,
            query_params=args.query,
        )

class CreatePermissions(BaseApi):

    async def acreate_permissions(
        self,
        permissions: typing.Optional[typing.List[PermissionDTO]] = None,
        tenant_code: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PermissionBulkOperationResponseDTOPydantic:
        raw_response = await self.raw.acreate_permissions(
            permissions=permissions,
            tenant_code=tenant_code,
            **kwargs,
        )
        if validate:
            return PermissionBulkOperationResponseDTOPydantic(**raw_response.body)
        return api_client.construct_model_instance(PermissionBulkOperationResponseDTOPydantic, raw_response.body)
    
    
    def create_permissions(
        self,
        permissions: typing.Optional[typing.List[PermissionDTO]] = None,
        tenant_code: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PermissionBulkOperationResponseDTOPydantic:
        raw_response = self.raw.create_permissions(
            permissions=permissions,
            tenant_code=tenant_code,
        )
        if validate:
            return PermissionBulkOperationResponseDTOPydantic(**raw_response.body)
        return api_client.construct_model_instance(PermissionBulkOperationResponseDTOPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        permissions: typing.Optional[typing.List[PermissionDTO]] = None,
        tenant_code: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_permissions_mapped_args(
            permissions=permissions,
            tenant_code=tenant_code,
        )
        return await self._acreate_permissions_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        permissions: typing.Optional[typing.List[PermissionDTO]] = None,
        tenant_code: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_permissions_mapped_args(
            permissions=permissions,
            tenant_code=tenant_code,
        )
        return self._create_permissions_oapg(
            body=args.body,
            query_params=args.query,
        )

