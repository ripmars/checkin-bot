#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        : smzdm_checkin.py
@Desc        : None
@Time        : 2021/09/04 10:08:55
@Author      : Chaos
@Version     : 1.0
'''
# here put the import lib
import requests
import re

from random import choice
import string
import time

def GenPassword_Num(length=8,chars=string.digits):
    return ''.join([choice(chars) for i in range(length)])




header = {
            'referer': 'https://www.smzdm.com/',
            'cookie': 'insert your cookie here',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/527.36 (KHTML, like Gecko) Chrome/92.0.3515.151 Safari/527.36'
        }



if __name__=="__main__":
    magic_random = str(GenPassword_Num(16))
#     print(magic_random)
    t = time.time()
    t = int(round(t * 1000))
    t2 = t+2
    sign_url=f'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin?callback=jQuery11240{magic_random}_{t}&_={t2}'
#     print(sign_url)
    res = requests.get(url=sign_url,headers=header,timeout=5)
    print(res.text)
