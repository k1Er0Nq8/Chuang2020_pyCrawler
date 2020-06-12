import requests
# noinspection PyUnresolvedReferences
import json
# noinspection PyUnresolvedReferences
import pandas as pd

import re

#去掉人名里的点
def validateTitle(title):
    rstr = r"[\·]"  # '·'
    new_title = re.sub(rstr, "", title)  # 替换为空
    return new_title

url1="https://zbaccess.video.qq.com/fcgi/getVoteActityRankList?raw=1&vappid=51902973&vsecret=14816bd3d3bb7c03d6fd123b47541a77d0c7ff859fb85f21&actityId=107015&pageSize=20&vplatform=3&listFlag=0&pageContext=&ver=1&_t=1591636791482&_=1591636791484"
url2="https://zbaccess.video.qq.com/fcgi/getVoteActityRankList?raw=1&vappid=51902973&vsecret=14816bd3d3bb7c03d6fd123b47541a77d0c7ff859fb85f21&actityId=107015&pageSize=20&vplatform=3&listFlag=0&pageContext=lastrealrank%3D20%26sc%3D0%26lastcnt%3D0%26lastrank%3D20%26lastid%3D8284569%26key%3Dactity_currank_list_107015_1591636786&ver=1&_t=1591636791729&_=1591636791730"
url3="https://zbaccess.video.qq.com/fcgi/getVoteActityRankList?raw=1&vappid=51902973&vsecret=14816bd3d3bb7c03d6fd123b47541a77d0c7ff859fb85f21&actityId=107015&pageSize=20&vplatform=3&listFlag=0&pageContext=lastrealrank%3D40%26sc%3D0%26lastcnt%3D0%26lastrank%3D40%26lastid%3D8284674%26key%3Dactity_currank_list_107015_1591636786&ver=1&_t=1591636791916&_=1591636791916"
url4="https://zbaccess.video.qq.com/fcgi/getVoteActityRankList?raw=1&vappid=51902973&vsecret=14816bd3d3bb7c03d6fd123b47541a77d0c7ff859fb85f21&actityId=107015&pageSize=20&vplatform=3&listFlag=0&pageContext=lastrealrank%3D60%26sc%3D0%26lastcnt%3D0%26lastrank%3D60%26lastid%3D8284574%26key%3Dactity_currank_list_107015_1591636786&ver=1&_t=1591636792498&_=1591636792499"
url5="https://zbaccess.video.qq.com/fcgi/getVoteActityRankList?raw=1&vappid=51902973&vsecret=14816bd3d3bb7c03d6fd123b47541a77d0c7ff859fb85f21&actityId=107015&pageSize=20&vplatform=3&listFlag=0&pageContext=lastrealrank%3D80%26sc%3D0%26lastcnt%3D0%26lastrank%3D80%26lastid%3D8284645%26key%3Dactity_currank_list_107015_1591636786&ver=1&_t=1591636804484&_=1591636804485"
url6="https://zbaccess.video.qq.com/fcgi/getVoteActityRankList?raw=1&vappid=51902973&vsecret=14816bd3d3bb7c03d6fd123b47541a77d0c7ff859fb85f21&actityId=107015&pageSize=20&vplatform=3&listFlag=0&pageContext=lastrealrank%3D100%26sc%3D0%26lastcnt%3D0%26lastrank%3D100%26lastid%3D8284636%26key%3Dactity_currank_list_107015_1591636786&ver=1&_t=1591636804767&_=1591636804768"


def getPicSort(url1,url2,url3,url4,url5,url6):
    response1=requests.get(url1)#请求url
    response2 = requests.get(url2)  # 请求url
    response3 = requests.get(url3)  # 请求url
    response4 = requests.get(url4)  # 请求url
    response5 = requests.get(url5)  # 请求url
    response6 = requests.get(url6)  # 请求url

    name=[]
    pic_url=[]
    sort=[]

    response1.encoding='utf-8'#规定编码形式
    response2.encoding = 'utf-8'  # 规定编码形式
    response3.encoding = 'utf-8'  # 规定编码形式
    response4.encoding = 'utf-8'  # 规定编码形式
    response5.encoding = 'utf-8'  # 规定编码形式
    response6.encoding = 'utf-8'  # 规定编码形式

    #print(response1.text)#输出json文件

    jd1=json.loads(response1.text)#通过json库加载文件
    jd2 = json.loads(response2.text)  # 通过json库加载文件
    jd3 = json.loads(response3.text)  # 通过json库加载文件
    jd4 = json.loads(response4.text)  # 通过json库加载文件
    jd5 = json.loads(response5.text)  # 通过json库加载文件
    jd6 = json.loads(response6.text)  # 通过json库加载文件

    for i,j in enumerate(jd1["data"]["itemList"]):
        sort.append(i+1);
        name.append(validateTitle(j['itemInfo']['name']));
        pic_url.append(j['itemInfo']['mapData']['poster_pic'])
    for i,j in enumerate(jd2["data"]["itemList"]):
        sort.append(20+i+1);
        name.append(j['itemInfo']['name']);
        pic_url.append(j['itemInfo']['mapData']['poster_pic'])
    for i,j in enumerate(jd3["data"]["itemList"]):
        sort.append(40+i+1);
        name.append(j['itemInfo']['name']);
        pic_url.append(j['itemInfo']['mapData']['poster_pic'])
    for i,j in enumerate(jd4["data"]["itemList"]):
        sort.append(60+i+1);
        name.append(j['itemInfo']['name']);
        pic_url.append(j['itemInfo']['mapData']['poster_pic'])
    for i,j in enumerate(jd5["data"]["itemList"]):
        sort.append(80+i+1);
        name.append(j['itemInfo']['name']);
        pic_url.append(j['itemInfo']['mapData']['poster_pic'])
    for i,j in enumerate(jd6["data"]["itemList"]):
        sort.append(100+i+1);
        name.append(j['itemInfo']['name']);
        pic_url.append(j['itemInfo']['mapData']['poster_pic'])

    dataframe=pd.DataFrame({'name':name,"sort":sort,"pic_url":pic_url})
    dataframe.to_csv('./inform_data1.csv',index=False)

getPicSort(url1,url2,url3,url4,url5,url6);
