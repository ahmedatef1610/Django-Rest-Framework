from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client


def get_index(index_name='drf_Product'):
    # drf_Article
    client = get_client()
    index = client.init_index(index_name)
    return index


def perform_search(query, *args, **kwargs):
    """
    perform_search("hello", tags=["electronics"], public=True)
    """
    index = get_index()
    params = {}
    tags = ""

    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params['tagFilters'] = tags

    index_filters = [f"{k}:{v}" for k, v in kwargs.items() if v]

    if len(index_filters) != 0:
        params['facetFilters'] = index_filters

    print(params)  # {'tagFilters': 'cars', 'facetFilters': ['user:ahmed', 'public:True']}

    # results = index.search(query)
    results = index.search(query, params)
    return results
