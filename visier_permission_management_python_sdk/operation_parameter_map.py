operation_parameter_map = {
    '/v1/admin/permissions-POST': {
        'parameters': [
            {
                'name': 'permissions'
            },
            {
                'name': 'tenantCode'
            },
        ]
    },
    '/v1/admin/permissions-DELETE': {
        'parameters': [
            {
                'name': 'tenantCode'
            },
        ]
    },
    '/v1/admin/capabilities-GET': {
        'parameters': [
            {
                'name': 'tenantCode'
            },
        ]
    },
    '/v1/admin/capabilities/{capabilityId}-GET': {
        'parameters': [
            {
                'name': 'capabilityId'
            },
            {
                'name': 'tenantCode'
            },
        ]
    },
    '/v1/admin/content-packages/{contentPackageId}-GET': {
        'parameters': [
            {
                'name': 'contentPackageId'
            },
            {
                'name': 'tenantCode'
            },
        ]
    },
    '/v1/admin/content-packages-GET': {
        'parameters': [
            {
                'name': 'tenantCode'
            },
            {
                'name': 'searchString'
            },
        ]
    },
    '/v1/admin/data-security-objects-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'includeDetails'
            },
            {
                'name': 'tenantCode'
            },
        ]
    },
    '/v1/admin/permissions/{permissionId}-GET': {
        'parameters': [
            {
                'name': 'permissionId'
            },
            {
                'name': 'tenantCode'
            },
        ]
    },
    '/v1/admin/permissions-GET': {
        'parameters': [
            {
                'name': 'tenantCode'
            },
            {
                'name': 'includeDetails'
            },
        ]
    },
    '/v1/admin/permissions-PUT': {
        'parameters': [
            {
                'name': 'permissions'
            },
            {
                'name': 'tenantCode'
            },
        ]
    },
};