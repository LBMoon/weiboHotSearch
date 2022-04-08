import requests
from lxml import etree
import json

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class GetPage:
    headers = {
        #"authority": "weibo.com",
        #"method": "GET",
        #"path": "/ajax/side/hotSearch",
        #"scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": "XSRF-TOKEN=ah0pzJm5CL1dKamCFoaMSKSk; login_sid_t=fc61adf336eae304309071acd13ff281; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=5654391276586.375.1649301944792; SINAGLOBAL=5654391276586.375.1649301944792; ULV=1649301944798:1:1:1:5654391276586.375.1649301944792:; wb_view_log=1536*8641.25; WBStorage=f4f1148c|undefined; WBtopGlobal_register_version=2022040715; crossidccode=CODE-tc-1NCmy2-2dwi3v-NnVPUejqUot0Ontc741b8; SSOLoginState=1649316450; SUB=_2A25PSuIODeRhGeNG6loW9y7Fwz-IHXVstI5GrDV8PUJbkNB-LRLskW1NS2wgRI58mrA0Oa2FoD7aLqBULFDtYrbG; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5CH3pfdZbZ3ssf.PaTIW4N5NHD95Qf1h2RS0M71Kn0Ws4Dqc_Fi--ciKnRiK.pi--fi-z7i-zpi--Ni-8hiK.pi--Ni-8hiK.pi--Xi-zRiKy2i--Ri-8si-zXi--Ri-8siKL2eh27; WBPSESS=wTupKIInnaPDToBqD0rz_7Y9CsJZErm77qVyhDBy9TNV5yefKpmUIQsdDDoreRIn2_sNVm_60ma3WuIgFL3IwuXGtNHECrwCacAJJcbDDDYdYAaQWNOvWFOzBj9ehRIy8Ga6jVTwRDHD3-TTqnyYjw==",
        "referer": "https://weibo.com/hot/search",
        "sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "traceparent": "00-8533422eb3feddd98b598f3ad2131503-82435e66fc1f0f8d-00",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "ah0pzJm5CL1dKamCFoaMSKSk" 
    }   
    def __init__(self,url):
        self.url = url
    def get_page(self):
        self.response = requests.get(self.url,headers=GetPage.headers).json()
        return self.response

def parseData(url):
    res = GetPage(url).get_page()
    #data = res["data"]
    hot_info = []
    data = res["data"]["realtime"]
    #print(data)
    for item in data:
        temp = {}
        temp["分类"] = item["category"]
        temp["热门标题"] = item["word"]
        temp["热门等级"] = item["label_name"]
        temp["点击量"] = item["raw_hot"]
        temp["热门排行"] = item["rank"]
        hot_info.append(temp)

    for item1 in hot_info:
        print(item1)

    #print(res)
    

def main():
    url_base = "https://weibo.com/ajax/side/hotSearch"
    parseData(url_base)


if __name__ == "__main__":
    main()

