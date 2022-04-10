import requests
from lxml import etree
import json
import time
import pymongo

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
    print("正在爬取数据...")
    res = GetPage(url).get_page()
    data = res["data"]["realtime"]
    print("爬取数据完毕，正在对数据进行保存...")
    # 对_id和集合名称用时间来命名
    year = time.gmtime().tm_year
    month = time.gmtime().tm_mon
    day = time.gmtime().tm_mday

    if month == 1:
        Month = "January"
    elif month == 2:
        Month = "February"
    elif month == 3:
        Month = "March"
    elif month == 4:
        Month = "April"
    elif month == 5:
        Month = "May"
    elif month == 6:
        Month = "June"
    elif month == 7:
        Month = "July"
    elif month == 8:
        Month = "August"
    elif month == 9:
        Month = "September"
    elif month == 10:
        Month = "October"
    elif month == 11:
        Month = "November"
    elif month == 12:
        Month = "December"

    if month < 10:
        if day < 10:
            _id = f"{year}0{month}0{day}"
        else:
            _id = f"{year}0{month}{day}"
    else:
        if day < 10:
            _id = f"{year}{month}0{day}"
        else:
            _id = f"{year}{month}{day}"
    collect_name = Month + "_"  + str(year)

    # 利用MongoDB将数据保存
    client =  pymongo.MongoClient(host="127.0.0.1",port=27017)
    collection = client["weibo_hotSearch"][collect_name]
    collection.insert_one({"_id":_id,"realtime":data})
    print("数据保存完成")
def main():
    url_base = "https://weibo.com/ajax/side/hotSearch"
    parseData(url_base)

if __name__ == "__main__":
    main()

