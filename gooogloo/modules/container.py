from .utils import consts, funcs
import requests
import urllib.parse


class SearchResults(object):
    '''
    Search Results Collection
    '''

    def __init__(self, end_pt, params):
        self.__end_pt = end_pt
        self.__params = params

        # cache results page
        self.__results = requests.get(
            f'{self.__end_pt}&{self.__params}').json()

    def __repr__(self):
        return f'SearchResults({self.__params})'

    # JSON queries hard capped to 100 from customsearch api
    def results_iter(self):
        '''
        Returns an iterator yielding search result as `dict`
        '''

        start_cap = 91  # start cap for json request
        start = 1

        while start <= start_cap and 'nextPage' in self.__results.queries:
            for result in self.__results['items']:
                yield result

            # load next page
            start += consts.NUM_RESULTS_PER_PAGE
            self.__results = requests.get(
                f'{self.__end_pt}&{self.__params}&start={start}').json()


class GoogleSearch(object):
    '''
    Custom Google Search Engine API
    '''

    def __init__(self, api_key: str, cx: str = consts.DEFAULT_CX):
        '''
        Initialize a custom Google Search Engine API


        Arguments:

        `api_key` -> your API key for identifying your application
        see https://developers.google.com/custom-search/v1/introduction#identify_your_application_to_google_with_api_key

        `cx` -> your custom search engine id check https://cse.google.com/all
        '''
        if not (200 <= requests.get(f'{consts.RESURL}key={api_key}&cx={consts.DEFAULT_CX}&q=google').status_code < 300):
            raise ValueError(f'API Key:{api_key} is invalid.')
        if not (200 <= requests.get(f'{consts.RESURL}key={api_key}&cx={cx}&q=google').status_code < 300):
            raise ValueError(f'Search Engine ID:{cx} is invalid.')
        self._api_key = api_key
        self._cx = cx
        self.__end_pt = f'{consts.RESURL}key={api_key}'

    def search(self, q, **kwargs) -> SearchResults:
        '''
        Returns <- `SearchResults` object that queries the API.

        Keyword Arguments:

         `q` -> the search query

        For the rest of optinal parameters refer to: 
        https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
        '''
        paras = {}
        paras['cx'] = self._cx
        paras['q'] = requests.utils.quote(q)
        for k, v in kwargs:
            if k in consts.CSL_Q:
                paras[k] = requests.utils.quote(v)
        return SearchResults(self.__end_pt, urllib.parse.urlencode(paras))

    def __repr__(self):
        return f'GoogleSearch({self._cx})'
