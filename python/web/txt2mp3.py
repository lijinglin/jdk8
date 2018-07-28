#coding=utf-8
#程序连接科大讯飞语音，将一段文本转换为一个mp3语音格式存在当前文件夹下：

#科大讯飞语音
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def txt2voice(msg,fname):



    import json

    url = 'http://www.xfyun.cn/herapi/solution/synthesis?vcn=x_xiaolin&vol=7&spd=medium&textType=cn&textPut='+msg

    head = {'Accept': 'application/json, text/javascript, */*; q=0.01',

                       'Accept-Encoding': 'gzip, deflate',

                       'Accept-Language': 'zh-CN',

                       'Connection': 'Keep-Alive',

                       'Cookie': 'token=null; account_id=null; SESSION=8e0116e7-32f0-4d55-96b5-08af593936f4; pgv_pvi=3816536064; Hm_lvt_83a57cc9e205b0add91afc6c4f0babcc=1518569845; pgv_si=s7171897344; Hm_lpvt_83a57cc9e205b0add91afc6c4f0babcc=1518569969',

                       'Host': 'www.xfyun.cn',

                       'Referer': 'http://www.xfyun.cn/services/online_tts',

                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',

                       'X-Requested-With': 'XMLHttpRequest'}

    res = requests.get(url,headers=head)

    data = json.loads(res.text)['data']
    print(data)

    mp3 = res.get(data).content

    with open("%s.mp3"%fname, "wb") as f:

        f.write(mp3)

txt2voice('how','what')