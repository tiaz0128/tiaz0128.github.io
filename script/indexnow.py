import requests
import json

host = "tiaz.dev"
url_list = [
    "Network/4",
    "Network/5",
]

headers = {"Content-Type": "application/json; charset=utf-8"}
payload = {
    "host": host,
    "key": "90f828d361c54550931a61cfd003feb0",
    "keyLocation": f"https://{host}/90f828d361c54550931a61cfd003feb0.txt",
    "urlList": list(map(lambda x: f"https://{host}/{x}", url_list)),
}

BING_URL = "https://api.indexnow.org/IndexNow"
NAVER_URL = "https://searchadvisor.naver.com/indexnow"

platform_urls = [BING_URL, NAVER_URL]

for url in platform_urls:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.status_code)
    print(response.text)
