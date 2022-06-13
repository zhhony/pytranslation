import random
import hashlib
import json
import requests
from time import sleep


def translationBaidu(src: str, appid: str, keys: str,  fr: str = 'en', to: str = 'zh') -> str:
    '''
    translationBaidu(翻译内容，源语种=en，目标语种=zh) \n
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

    url_baidu = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'

    salt = random.randint(1000000000, 9999999999)
    sign_s = appid + str(src) + str(salt) + keys
    ha = hashlib.md5()
    ha.update(sign_s.encode('utf8'))
    sign = ha.hexdigest()

    url = url_baidu + 'q=' + str(src) + '&from=' + fr + '&to=' + to + '&appid=' + \
        appid + '&salt=' + str(salt) + '&sign=' + sign

    response = requests.request("get", url)
    cont = response.text.encode('utf-8')
    cont = json.loads(cont)

    sleep(1)

    return cont['trans_result'][0]['dst']
