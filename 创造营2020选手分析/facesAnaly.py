# noinspection PyUnresolvedReferences
import requests
# noinspection PyUnresolvedReferences
import base64
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt # plt 用于显示图片

import time

import glob

base_path=r'D:\anaconda\jupyterFiles\chuang3_pics'

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        content=base64.b64encode(fp.read()).decode('utf-8')
        return content

'''
这里介绍了怎么获取token
https://www.cnblogs.com/niejunlei/p/10075258.html
'''

def FaceScore(filepath):
    request_url="https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params={"image":format(get_file_content(filepath)),"image_type":"BASE64","face_field":"age,gender,beauty"}#beauty是必要的
    access_token='24.0810d375a588ebde709eb51a0f995d89.2592000.1594363402.282335-20328145'#token有效期一个月，到期要更换

    request_url=request_url+"?access_token="+access_token
    headers={'content-type':'json'}
    response=requests.post(request_url,data=params,headers=headers)
    if(response):
        result=response.json()
    time.sleep(4)
    return result['result']['face_list'][0]['age'],result['result']['face_list'][0]['beauty'],result['result']['face_list'][0]['gender']['type']

def Get_Face_Score(i):
    path=base_path+'\\{}.png'.format(i)
    age,beauty,gender=FaceScore(path)#gender不需要就用下划线代替
    score=beauty
    return score,age

import pandas as pd
df=pd.read_csv(r'D:\anaconda\jupyterFiles\total_data.csv')
# print(df)



if __name__=='__main__':
    pic_paths=glob.glob('D:\\anaconda\\jupyterFiles\\chuang3_pics\\*.png')
    score={}
    for i in pic_paths:
        name=i.split('\\')[-1].split('.')[0] #从后面把*.jpg切出来，然后又把*也就是姓名切出来
        scores,ages=Get_Face_Score(name)
        score[name]=(scores)
        #print(score)
        time.sleep(3)

    aa=[]
    for nm in df['name'].values:
        aa.append(score[nm])
    df['Facevalue']=aa
    df.to_csv("./total_data_withPoints.csv")

