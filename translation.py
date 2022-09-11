import random
import hashlib
import json
import requests
from time import sleep

from . modules import *

config = Config("D:\\WorkData\\pytranslation\\config.json")


def TranslationBaidu(src: str,  fr: str = 'en', to: str = 'zh', flag: int = 0) -> str:
    '''
    translationBaidu(翻译内容，appid，keys，源语种=en，目标语种=zh，flag<>0时会额外输出内置参数) \n
    为保证翻译质量，请将单次请求长度控制在 6000 bytes以内（汉字约为输入参数 2000 个）\n
    语种列表：\n
    名称	        代码	    名称	        代码	    名称	        代码\n
    自动检测	    auto	    中文	        zh	        英语	        en\n
    粤语	        yue	        文言文	        wyw	        日语	        jp\n
    韩语	        kor	        法语	        fra	        西班牙语	    spa\n
    泰语	        th	        阿拉伯语	    ara	        俄语	        ru\n
    葡萄牙语	    pt	        德语	        de	        意大利语	    it\n
    希腊语	        el	        荷兰语	        nl	        波兰语	        pl\n
    保加利亚语	    bul	        爱沙尼亚语	    est	        丹麦语	        dan\n
    芬兰语	        fin	        捷克语	        cs	        罗马尼亚语	    rom\n
    斯洛文尼亚语	slo	        瑞典语	        swe	        匈牙利语	    hu\n
    繁体中文	    cht	        越南语	        vie	 	 \n
    '''

    urlBaidu = config.getHttp
    appid = config.getAppid
    keys = config.getKeys

    salt = random.randint(1000000000, 9999999999)
    signs = appid + str(src) + str(salt) + keys
    ha = hashlib.md5()
    ha.update(signs.encode('utf8'))
    sign = ha.hexdigest()

    https = urlBaidu + 'q=' + str(src) + '&from=' + fr + '&to=' + to + '&appid=' + \
        appid + '&salt=' + str(salt) + '&sign=' + sign

    response = requests.request("get", https)
    cont = response.text.encode('utf-8')
    cont = json.loads(cont)

    sleep(1)

    if flag != 0:
        return [cont['trans_result'][0]['dst'], 'appid = ' + str(appid), 'salt = ' + str(salt), 'sign = ' + str(sign), 'https = ' + https]
    else:
        return cont['trans_result'][0]['dst']
