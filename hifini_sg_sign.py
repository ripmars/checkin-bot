#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        : hifini_sg_sign.py
@Desc        : None
@Time        : 2021/09/04 10:08:55
@Author      : Chaos
@Version     : 1.0
'''
# here put the import lib
import requests
import re
header = {
            'referer': 'https://www.hifini.com/',
            'cookie': 'insert your cookie here',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

# myurl='https://www.hifini.com/my.htm'
sign_url='https://www.hifini.com/sg_sign.htm'
res = requests.get(url=sign_url,headers=header)
print(res.text)
