#-*- coding:utf-8 -*-

import json
from mitmproxy import http

def response(flow):
    if u"api.douguo.net/recipe/v2/search" in flow.request.url:
        # TODO: store the content
        # print(json.loads(flow.response.content.decode("utf-8")))
        with open("file.json", "a") as file:
            file.write(json.dumps(flow.response.content.decode()) + "\n")