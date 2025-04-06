import requests
import json

host = "tiaz.dev"
url_list = [
    "insight/6",
    "Network/3",
    "python/12",
    "ai/3",
    "ai/2",
    "ai/1",
    "insight/5",
    "Celery/2",
    "Network/2",
    "Docker/3",
    "Docker/2",
    "AWS/5",
    "insight/4",
    "insight/3",
    "python/11",
    "book/2",
    "cs/1",
    "insight/2",
    "insight/1",
    "python/10",
    "AWS/4",
    "AWS/3",
    "Network/1",
    "Docker/1",
    "Celery/1",
    "python/9",
    "gRPC/2",
    "gRPC/1",
    "Couchbase/2",
    "Couchbase/1",
    "python/8",
    "python/7",
    "python/6",
    "python/5",
    "python/4-2",
    "python/4",
    "AWS/2",
    "AWS/1",
    "tool/1",
    "GitHub/1",
    "python/3",
    "python/2",
    "python/1",
    "flask/2",
    "book/1",
    "flask/1",
]

NAVER_URL = "https://searchadvisor.naver.com/indexnow"
BING_URL = "https://api.indexnow.org/IndexNow"

headers = {"Content-Type": "application/json; charset=utf-8"}
payload = {
    "host": host,
    "key": "90f828d361c54550931a61cfd003feb0",
    "keyLocation": f"https://{host}/90f828d361c54550931a61cfd003feb0.txt",
    "urlList": list(map(lambda x: f"https://{host}/{x}", url_list)),
}

response = requests.post(BING_URL, headers=headers, data=json.dumps(payload))
print(response.status_code)
print(response.text)
