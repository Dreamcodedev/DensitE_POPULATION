# coding : utf-8

import program.download_agents as script
import urllib.request
from io import BytesIO
import json

# get agents 

def test_http_result(monkeypatch):
    results=[{
        "age":84,
        "agreeableness":0.74
    }]

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())
    
    monkeypatch.setattr(urllib.request,'urlopen', mockreturn)

    assert script.get_agents(1) == results