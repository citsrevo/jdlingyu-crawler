# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:16:24 2020

@author: overs
"""
from Crawler import *
import time
import re
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import pandas as pd 
import copy
import re
import os
if __name__ == '__main__':
    '''
    COS套图存储
    '''
    
    Driver = webdriver.Chrome()
    List = GetCosSetUrl()
    Used_List = []
    df = pd.DataFrame({'url':[],'Data':[]} )
    
    for i in List:
        if i in Used_List:
            continue
        time.sleep(random.random()+3)
        Dict = ExtrackCosData(i)
        df = df.append(pd.DataFrame(Dict))
        Used_List.append(i)
        print(Dict['Data'])
        
    Saved_df = copy.deepcopy(df)
    
    df_result = pd.DataFrame({'url':[],'Extract':[]})
    for data in df['Data']:
        Dict = {}
        
        url_target = re.findall('(https\S*)',data)
        if url_target:
            Dict['url'] = [url_target[0]]
        else:
            continue
        Ext = re.findall('：(.{4})' ,data)
        Ext = [i for i in Ext if i not in ['http','jdli','登录可见',' 二维码']]
        print(Ext)
        if Ext:
            Dict['Extract'] = [Ext[0]]
    
        df_result = df_result.append(pd.DataFrame(Dict))
    df_result.to_csv('COS套图地址.csv')
    
    
    '''
    自拍
    '''
    List = GetZipaiSetUrl()
    df = pd.DataFrame(List)
    df.to_csv('Zipai.csv')
    df = pd.read_csv('Zipai.csv')
    
    rootpath = 'H:\jdlingyu\zipai'
    Existed_NameList = set(os.listdir(rootpath))
    for i in range(321,df.shape[0]):
        print(i)
        time.sleep(1)
        ImgSrc = ExtractZipaiData(df.iloc[i,1])
        if list(ImgSrc)[0] in Existed_NameList:
            continue
        DownloadPic(ImgSrc,rootpath)
        Existed_NameList.add(list(ImgSrc)[0])
    
    df = df[['0']]
    df.to_csv('H:\jdlingyu\zipai\Index.csv')
                                                  
                
    '''
    特点
    '''        
    List = GetTedianSetUrl()
    df = pd.DataFrame(List)
    df.to_csv('Tedian.csv')
    df = pd.read_csv('Tedian.csv')
    
    rootpath = r'H:\jdlingyu\tedian'
    if os.path.exists(rootpath):    
        Existed_NameList = set(os.listdir(rootpath))
    else:
        Existed_NameList = set()
    for i in range(115,df.shape[0]):
        print(i)
        time.sleep(1)
        ImgSrc = ExtractZipaiData(df.iloc[i,1])
        if list(ImgSrc)[0] in Existed_NameList:
            continue
        DownloadPic(ImgSrc,rootpath)
        Existed_NameList.add(list(ImgSrc)[0])
    
    df = df[['0']]
    df.to_csv('H:\jdlingyu\zipai\Index.csv')
