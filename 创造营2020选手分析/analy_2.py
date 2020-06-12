# noinspection PyUnresolvedReferences
import requests
# noinspection PyUnresolvedReferences
import pandas as pd
#from langconv import *
# noinspection PyUnresolvedReferences
from bs4 import BeautifulSoup as BS
# noinspection PyUnresolvedReferences
import time
import socket
# noinspection PyUnresolvedReferences
import lxml
# noinspection PyUnresolvedReferences
import urllib.error


socket.setdefaulttimeout(20)
#获取各选手更详细信息

"""
def Tran2Simp(sentence):    #繁化简
    sentence=Converter('zh-hans').convert(sentence)
    return sentence

def Simp2Tran(sentence):
    sentence=Converter('zh-hant').convert(sentence)
    return sentence
"""




data=pd.read_csv("inform_data1.csv")
names=data['name']
# print(names)

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}


url='https://baike.baidu.com/item/%E5%88%9B%E9%80%A0%E8%90%A52020'

response=requests.get(url,headers=headers)
response.encoding='utf-8'
soup=BS(response.text,'lxml')#通过bs解析返回的文本
response.close()

#根据table class="wikitable sortable collapsible"这个唯一节点来定位抓取tr标签，再从tr标签下抓取文本
#明确抓取目标

all_tr=soup.find('table',{'class':"table-view log-set-param"}).find_all('tr') #返回第一次找到的结果
#print(all_tr)
dict1={}

for artist_tr in all_tr[1:]:
    all_tds=artist_tr.find_all('td')
    dict1[all_tds[0].text]=[]
    dict1[all_tds[0].text].append(all_tds[1].text.strip())#初评级
    dict1[all_tds[0].text].append(all_tds[2].text.strip())  # 主题曲评级
    dict1[all_tds[0].text].append(all_tds[3].text.strip())  # 第一次排名
    dict1[all_tds[0].text].append(all_tds[4].text.strip())  # 第二次排名
    dict1[all_tds[0].text].append(all_tds[5].text.strip())  # 第三次排名
    dict1[all_tds[0].text].append(all_tds[6].text.strip())  # 总排名

#print(dict1)
#print(len(dict1))

preJudge=[]
songJudge=[]
firstRank=[]
secondRank=[]
thirdRank=[]
finalRank=[]

for name in names:
    try:
        preJudge.append(dict1[name][0])
        songJudge.append(dict1[name][1])
        firstRank.append(dict1[name][2])
        secondRank.append(dict1[name][3])
        thirdRank.append(dict1[name][4])
        finalRank.append(dict1[name][5])
    except NameError as e:
        print(name)
        break

data['preJudge']=preJudge
data['songJudge']=songJudge
data['firstRank']=firstRank
data['secondRank']=secondRank
data['thirdRank']=thirdRank
data['finalRank']=finalRank

data.to_csv('./total_data.csv',index=False)