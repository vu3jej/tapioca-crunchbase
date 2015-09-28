# coding: utf-8

RESOURCE_MAPPING = {
    'organizations': {
        'resource': 'organizations',
        'docs': 'http://data.crunchbase.com/docs/organizations'
    },
    'organization': {
        'resource': 'organizations/{permalink}',
        'docs': 'http://data.crunchbase.com/docs/organizationpermalink'
    },
    'organizations_relationships': {
        'resource': 'organizations/{permalink}/{relationship_name}',
        'docs': 'http://data.crunchbase.com/docs/organizationspermalinkrelationship_name'
    },
    'people': {
        'resource': 'people',
        'docs': 'http://data.crunchbase.com/docs/people'
    },
    'person': {
        'resource': 'people/{permalink}',
        'docs': 'http://data.crunchbase.com/docs/personpermalink'
    },
    'people_relationships': {
        'resource': 'people/{permalink}/{relationship_name}',
        'docs': 'http://data.crunchbase.com/docs/peoplepermalinkrelationship-name'
    },
    'products': {
        'resource': 'products',
        'docs': 'http://data.crunchbase.com/docs/products'
    },
    'product': {
        'resource': 'products/{permalink}',
        'docs': 'http://data.crunchbase.com/docs/productpermalink'
    },
    'products_relationships': {
        'resource': 'products/{permalink}/{relationship_name}',
        'docs': 'http://data.crunchbase.com/docs/productspermalinkrelationship-name'
    },
    'categories': {
        'resource': 'categories',
        'docs': 'http://data.crunchbase.com/docs/categories'
    },
    'locations': {
        'resource': 'locations',
        'docs': 'http://data.crunchbase.com/docs/testinput'
    },
    'funding_rounds': {
        'resource': 'funding-rounds/{uuid}',
        'docs': 'http://data.crunchbase.com/docs/testinput-1'
    },
    'funding_rounds_relationships': {
        'resource': 'funding-rounds/{uuid}/{relationship_name}',
        'docs': 'http://data.crunchbase.com/docs/funding_roundsuuidrelationship_name'
    },
    'acquisitions': {
        'resource': 'acquisitions/{uuid}',
        'docs': 'http://data.crunchbase.com/docs/acquisitionuuid'
    },
    'acquisitions_relationships': {
        'resource': 'acquisitions/{uuid}/{relationship_name}',
        'docs': 'http://data.crunchbase.com/docs/acquisitionsuuidrelationship_name'
    },
    'ipos': {
        'resource': 'ipos/{uuid}',
        'docs': 'http://data.crunchbase.com/docs/ipouuid'
    },
    'ipos_relationships': {
        'resource': 'ipos/{uuid}/{relationship_name}',
        'docs': 'http://data.crunchbase.com/docs/iposuuidrelationship_name'
    },
    'funds': {
        'resource': 'funds/{uuid}',
        'docs': 'http://data.crunchbase.com/docs/fund_raiseuuid'
    },
    'funds_relationships': {
        'resource': '/funds/{uuid}/{relationship_name}',
        'docs': 'http://data.crunchbase.com/docs/fundsuuidrelationship_name'
    },
}
