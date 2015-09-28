# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)


from resource_mapping import RESOURCE_MAPPING


class CrunchbaseClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.crunchbase.com/v/3/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(CrunchbaseClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        if 'params' in params:
            params['params'].update({'user_key': api_params.get('user_key')})
        else:
            params['params'] = {'user_key': api_params.get('user_key')}

        return params

    def get_iterator_list(self, response_data):
        return response_data['data']['items']

    def get_iterator_next_request_kwargs(self,
            iterator_request_kwargs, response_data, response):
        data = response_data.get('data')
        paging = data.get('paging')
        if not paging:
            return
        next_page_url = paging.get('next_page_url')
        if next_page_url:
            return {'url': next_page_url}


Crunchbase = generate_wrapper_from_adapter(CrunchbaseClientAdapter)
