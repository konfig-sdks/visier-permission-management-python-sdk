<div align="center">

[![Visit Visier](./header.png)](https://visier.com)

# Visier<a id="visier"></a>

Visier APIs for managing permissions within an organization


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`visierpermissionmanagement.permission_management.create_permissions`](#visierpermissionmanagementpermission_managementcreate_permissions)
  * [`visierpermissionmanagement.permission_management.delete_permissions`](#visierpermissionmanagementpermission_managementdelete_permissions)
  * [`visierpermissionmanagement.permission_management.get_capabilities`](#visierpermissionmanagementpermission_managementget_capabilities)
  * [`visierpermissionmanagement.permission_management.get_capability`](#visierpermissionmanagementpermission_managementget_capability)
  * [`visierpermissionmanagement.permission_management.get_content_package`](#visierpermissionmanagementpermission_managementget_content_package)
  * [`visierpermissionmanagement.permission_management.get_content_packages`](#visierpermissionmanagementpermission_managementget_content_packages)
  * [`visierpermissionmanagement.permission_management.get_data_security_objects`](#visierpermissionmanagementpermission_managementget_data_security_objects)
  * [`visierpermissionmanagement.permission_management.get_permission`](#visierpermissionmanagementpermission_managementget_permission)
  * [`visierpermissionmanagement.permission_management.get_permissions`](#visierpermissionmanagementpermission_managementget_permissions)
  * [`visierpermissionmanagement.permission_management.update_permissions`](#visierpermissionmanagementpermission_managementupdate_permissions)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Visier&serviceName=PermissionManagement&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from visier_permission_management_python_sdk import VisierPermissionManagement, ApiException

visierpermissionmanagement = VisierPermissionManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Create permissions
    create_permissions_response = visierpermissionmanagement.permission_management.create_permissions(
        permissions=[
        {
        }
    ],
        tenant_code="string_example",
    )
    print(create_permissions_response)
except ApiException as e:
    print("Exception when calling PermissionManagementApi.create_permissions: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from visier_permission_management_python_sdk import VisierPermissionManagement, ApiException

visierpermissionmanagement = VisierPermissionManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Create permissions
        create_permissions_response = await visierpermissionmanagement.permission_management.acreate_permissions(
            permissions=[
        {
        }
    ],
            tenant_code="string_example",
        )
        print(create_permissions_response)
    except ApiException as e:
        print("Exception when calling PermissionManagementApi.create_permissions: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from visier_permission_management_python_sdk import VisierPermissionManagement, ApiException

visierpermissionmanagement = VisierPermissionManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Create permissions
    create_permissions_response = visierpermissionmanagement.permission_management.raw.create_permissions(
        permissions=[
        {
        }
    ],
        tenant_code="string_example",
    )
    pprint(create_permissions_response.body)
    pprint(create_permissions_response.body["successes"])
    pprint(create_permissions_response.body["failures"])
    pprint(create_permissions_response.headers)
    pprint(create_permissions_response.status)
    pprint(create_permissions_response.round_trip_time)
except ApiException as e:
    print("Exception when calling PermissionManagementApi.create_permissions: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `visierpermissionmanagement.permission_management.create_permissions`<a id="visierpermissionmanagementpermission_managementcreate_permissions"></a>

This API allows you to create new permissions. Administrating tenant users can specify the tenant in which to add these permissions.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_permissions_response = visierpermissionmanagement.permission_management.create_permissions(
    permissions=[
        {
        }
    ],
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### permissions: List[`PermissionDTO`]<a id="permissions-listpermissiondto"></a>

The list of permissions that will be created or updated

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to create permissions in.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PermissionsListDTO`](./visier_permission_management_python_sdk/type/permissions_list_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PermissionBulkOperationResponseDTO`](./visier_permission_management_python_sdk/pydantic/permission_bulk_operation_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/permissions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierpermissionmanagement.permission_management.delete_permissions`<a id="visierpermissionmanagementpermission_managementdelete_permissions"></a>

This API allows you to delete existing permissions.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_permissions_response = visierpermissionmanagement.permission_management.delete_permissions(
    body="body_example",
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to delete permissions from.

##### requestBody: `str`<a id="requestbody-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PermissionBulkOperationResponseDTO`](./visier_permission_management_python_sdk/pydantic/permission_bulk_operation_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/permissions` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierpermissionmanagement.permission_management.get_capabilities`<a id="visierpermissionmanagementpermission_managementget_capabilities"></a>

This API allows you to retrieve all the permission capabilities in your tenant.
 You can use the returned capabilities in other API calls when creating or updating permissions to assign the capability to the permission.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_capabilities_response = visierpermissionmanagement.permission_management.get_capabilities(
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve the capabilities from.

#### 🔄 Return<a id="🔄-return"></a>

[`GetCapabilitiesAPIResponseDTO`](./visier_permission_management_python_sdk/pydantic/get_capabilities_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/capabilities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierpermissionmanagement.permission_management.get_capability`<a id="visierpermissionmanagementpermission_managementget_capability"></a>

This API allows you to retrieve the details of a specific capability.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_capability_response = visierpermissionmanagement.permission_management.get_capability(
    capability_id="capabilityId_example",
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### capability_id: `str`<a id="capability_id-str"></a>

The unique identifier of the capability you want to retrieve.

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve a capability from.

#### 🔄 Return<a id="🔄-return"></a>

[`CapabilityDTO`](./visier_permission_management_python_sdk/pydantic/capability_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/capabilities/{capabilityId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierpermissionmanagement.permission_management.get_content_package`<a id="visierpermissionmanagementpermission_managementget_content_package"></a>

This API allows you to retrieve the details of a specific content package.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_content_package_response = visierpermissionmanagement.permission_management.get_content_package(
    content_package_id="contentPackageId_example",
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### content_package_id: `str`<a id="content_package_id-str"></a>

The unique identifier of the content package you want to retrieve.

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve a content package from.

#### 🔄 Return<a id="🔄-return"></a>

[`ContentPackageDTO`](./visier_permission_management_python_sdk/pydantic/content_package_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/content-packages/{contentPackageId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierpermissionmanagement.permission_management.get_content_packages`<a id="visierpermissionmanagementpermission_managementget_content_packages"></a>

This API allows you to retrieve the list of available content packages.
 You can use the returned content packages in other API calls when creating or updating permissions to add the content package to the permission.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_content_packages_response = visierpermissionmanagement.permission_management.get_content_packages(
    tenant_code="string_example",
    search_string="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve the content packages from.

##### search_string: `str`<a id="search_string-str"></a>

Optional search string to return only content packages whose display name or description contains that search string.  If searchString is empty or not provided, the response returns a list of all content packages.

#### 🔄 Return<a id="🔄-return"></a>

[`GetContentPackagesAPIResponseDTO`](./visier_permission_management_python_sdk/pydantic/get_content_packages_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/content-packages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierpermissionmanagement.permission_management.get_data_security_objects`<a id="visierpermissionmanagementpermission_managementget_data_security_objects"></a>

This API allows you to retrieve the list of available data security objects.
 Data security objects are analytic objects and their related objects that are available to define
 permissions’ data security profiles.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_security_objects_response = visierpermissionmanagement.permission_management.get_data_security_objects(
    id=[
        "string_example"
    ],
    include_details=True,
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: List[`str`]<a id="id-liststr"></a>

The unique identifiers of the data security objects (analytic objects) to retrieve.  Default is all data security objects.

##### include_details: `bool`<a id="include_details-bool"></a>

If true, the response includes the analytic objects (display name, ID, and object type), related objects,  securable properties, and securable dimensions. If false, the response only includes analytic objects  (display name, ID, and object type). Default is false.

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve data security objects from.

#### 🔄 Return<a id="🔄-return"></a>

[`GetDataSecurityObjectsAPIResponseDTO`](./visier_permission_management_python_sdk/pydantic/get_data_security_objects_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/data-security-objects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierpermissionmanagement.permission_management.get_permission`<a id="visierpermissionmanagementpermission_managementget_permission"></a>

This API allows you to retrieve the details for a specified permission.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_permission_response = visierpermissionmanagement.permission_management.get_permission(
    permission_id="permissionId_example",
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### permission_id: `str`<a id="permission_id-str"></a>

The unique identifier of the permission you want to retrieve.

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve a permission from.

#### 🔄 Return<a id="🔄-return"></a>

[`PermissionDTO`](./visier_permission_management_python_sdk/pydantic/permission_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/permissions/{permissionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierpermissionmanagement.permission_management.get_permissions`<a id="visierpermissionmanagementpermission_managementget_permissions"></a>

This API allows you to retrieve the full list of user permissions in your tenant.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_permissions_response = visierpermissionmanagement.permission_management.get_permissions(
    tenant_code="string_example",
    include_details=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve the permissions from.

##### include_details: `bool`<a id="include_details-bool"></a>

If true, returns the permission's details. If false, only returns the permissions' ID, display name,  and description. Default is false.

#### 🔄 Return<a id="🔄-return"></a>

[`GetPermissionsAPIResponseDTO`](./visier_permission_management_python_sdk/pydantic/get_permissions_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/permissions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierpermissionmanagement.permission_management.update_permissions`<a id="visierpermissionmanagementpermission_managementupdate_permissions"></a>

This API allows you to update existing permissions.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_permissions_response = visierpermissionmanagement.permission_management.update_permissions(
    permissions=[
        {
        }
    ],
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### permissions: List[`PermissionDTO`]<a id="permissions-listpermissiondto"></a>

The list of permissions that will be created or updated

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to update permissions in.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PermissionsListDTO`](./visier_permission_management_python_sdk/type/permissions_list_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PermissionBulkOperationResponseDTO`](./visier_permission_management_python_sdk/pydantic/permission_bulk_operation_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/permissions` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
