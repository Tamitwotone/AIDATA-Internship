import urllib
import uuid
import json
import socket
import requests
import requests
import time
one_page = 30
total = 30
url = "https://image.baidu.com/search/acjson"

headers = {
    'Referer': 'https://image.baidu.com/search/index',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
while 1:
    params = {
        'tn': 'resultjson_com',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': '马路',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '',
        'z': '',
        'ic': '',
        'word': '马路',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '',
        'istype': '',
        'qc': '',
        'nc': '',
        'fr': '',
        'pn': total,
        'rn': one_page,
    }
    r = requests.get(url, params=params,headers=headers)
    data = json.loads(r.text,encoding="utf8")['data']
    if data:
        for i in data:
            file_name = str(uuid.uuid4())
            if i:
                if 'middleURL' not in i.keys():
                    pass
                img_url = i['middleURL']
                open_url = urllib.request.urlopen(img_url, timeout=5)
                #with open("/home/irlans/三轮车/%s"%(file_name+".jpg"),"wb") as f :

                with open("C:/Users/SEELE/Desktop/AdditionalNEG/%s"%(file_name+".jpg"),"wb") as f :
                    f.write(open_url.read())
        total += one_page
        time.sleep(0.02)
    else:
        break
