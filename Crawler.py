# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:15:43 2020

@author: overs
"""

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
def login():
    usr_name = ''
    usr_psw = ''
    
    Input_name = Driver.find_element_by_xpath('//*[@name="username"]')
    Input_name.clear()
    Input_name.send_keys(usr_name)
    time.sleep(2)
    Input_psw = Driver.find_element_by_xpath('//*[@name="password"]')
    Input_psw.clear()
    Input_psw.send_keys(usr_psw)
    time.sleep(2)
    Log = Driver.find_element_by_xpath('//button[@type="submit" and @class = "submit w100"]')
    Log.click()
    Driver.execute_script("arguments[0].click();", Log)
    print('Log success')
    
def checkLogin():
    try:        
        elem = Driver.find_element_by_xpath('//*[@id="masthead"]/div[2]/div/div/div/div[3]/div[2]/button[1]')
        elem.click()
        time.sleep(1)
        login()
    except:
        print('Aleady login')
     
def GetCosSetUrl():
    url = 'https://www.jdlingyu.mobi/tuji/hentai/costt'
    Driver.get(url)
    checkLogin()
    UrlTarget = []
    while True:
        Elems = Driver.find_elements_by_xpath('//body//h2[@class="entry-title"]/a')
        UrlTarget += [i.get_attribute('href') for i in Elems]
        Elem = GetNextPageElem()
        if not Elem:
            break
        time.sleep(random.random() + 2)
        Elem.click()
    return UrlTarget

def GetZipaiSetUrl():
    url = 'https://www.jdlingyu.mobi/collection/zipai'
    Driver.get(url)
    checkLogin()
    UrlTarget = []
    while True:
        Elems = Driver.find_elements_by_xpath('//h2[@class = "entry-title"]/a')
        UrlTarget += [i.get_attribute('href') for i in Elems]
        Elem = GetNextPageElem()
        if not Elem:
            break
        time.sleep(random.random() + 2)
        Elem.click()
    return UrlTarget

def GetTedianSetUrl():
    url = 'https://www.jdlingyu.mobi/collection/trait'
    Driver.get(url)
    checkLogin()
    UrlTarget = []
    while True:
        Elems = Driver.find_elements_by_xpath('//h2[@class = "entry-title"]/a')
        List = []
        for i in Elems:
            try:
                List.append(i.get_attribute('href'))
            except:
                pass
            
        UrlTarget += List


        Elem = GetNextPageElem()
        if not Elem:
            break
        time.sleep(random.random() + 2)
        Elem.click()
    return UrlTarget

def GetNextPageElem():
    try:
        return Driver.find_element_by_xpath('//div[@class="btn-pager fr fs13"]/button[@class = "empty navbtr"]')
        
    except NoSuchElementException :
        return 0

def ExtrackCosData(Url):
    Driver.get(Url)
    checkLogin()
    try:
        Text = Driver.find_element_by_xpath('//*[contains(text(),"pan.baidu")]').text
        yun_url = re.findall('(https:.*) ',Text)[0]
    except:
        try:
            Text = Driver.find_element_by_xpath('//*[contains(@href,"pan.baidu")]')
            yun_url = Text.get_attribute('href')
        except:
            yun_url = ''
    try:
        Text = [i.text for i in Driver.find_elements_by_xpath('//*[contains(text(),"码")]') if i.text]
    except:
        Text = []
    
    
    Dict = {'url':[Url],'Data':[' '.join(Text) + yun_url]} 
    return Dict

def ExtractZipaiData(Url):
    Driver.get(Url)
    checkLogin()
    Dict = {}
    UrlName = Driver.title
    List = []
    Page = 1
    while 1:
        Source = Driver.find_element_by_xpath('//*[@id="content-innerText"]/p')
        S = Source.find_elements_by_tag_name('img')
        List += [i.get_attribute('src') for i in S]
        try:
            Button_current = Driver.find_element_by_xpath('//*[@id="entry-content"]//*[@class = "post-page-numbers current"]/button')
            Current_page = Button_current.text
            Button_next = Driver.find_element_by_xpath('//*[@id="entry-content"]//button[text() = "%s"]'%(int(Current_page)+ 1))
            Button_next.click()
            time.sleep(1)
            Page += 1
        except:
            break
            
    Dict[UrlName] = List
    print('收集到 ' + str(len(List)) + ' 张图片, 共' + str(Page) + '页')
    return Dict
def DownloadPic(ImgSrc,rootpath = 'H:\jdlingyu\zipai'):
    if not os.path.exists(rootpath):
        os.mkdir(rootpath)
    Tarpath = os.path.join(rootpath,CheckNameValid(list(ImgSrc)[0]))

    if not os.path.exists(Tarpath):
        os.mkdir(Tarpath)
    Fail = 0
    for num,i in enumerate(list(ImgSrc.values())[0]):
        try:
            r = requests.get(url = i,timeout = 20,headers = {'user-agent' :"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3"})
            time.sleep(random.random()+0.5)
            if r.status_code == 200:
                with open(os.path.join(Tarpath,str(num)+'.jpg'),'wb') as f:
                    f.write(r.content)
            else:
                Fail += 1
        except:
            Fail += 1
    if Fail != 0 :
         with open(os.path.join(Tarpath,'Result.txt'),'w') as f:
                f.write('Fail :' + str(Fail))
    print('Total: ' + str(len(list(ImgSrc.values())[0])), ', Fail: ' + str(Fail))
def CheckNameValid(name):
    name = name.replace(':','')
    name = name.replace('/','')
    name = name.replace('*','')
    name = name.replace('?','')
    return name




