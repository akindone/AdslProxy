# coding=utf-8
import re
import time
import requests
from requests.exceptions import ConnectionError, ReadTimeout
from adslproxy.db import RedisClient
from adslproxy.config import *
import platform

if platform.python_version().startswith('2.'):
    import commands as subprocess
elif platform.python_version().startswith('3.'):
    import subprocess
else:
    raise ValueError('python version must be 2 or 3')


class Sender():
    def get_ip(self, ifname=ADSL_IFNAME):
        """
        获取本机IP
        :param ifname: 网卡名称
        :return:
        """
        (status, output) = subprocess.getstatusoutput('ifconfig')
        if status == 0:
            pattern = re.compile(ifname + '.*?inet.*?(\d+\.\d+\.\d+\.\d+).*?netmask', re.S)
            result = re.search(pattern, output)
            if result:
                ip = result.group(1)
                return ip

    def test_proxy(self, proxy):
        """
        测试代理
        :param proxy: 代理
        :return: 测试结果
        """
        try:
            headers = {
                'Cookie':'openh5_uuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; terminal=i; w_actual_lat=31187016; w_actual_lng=121422285; w_latlng=0,0; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_visitid=b741a8e4-1548-4fec-855a-224ca00535d6; _lxsdk_s=169b8900f14-469-004-eeb%7C%7C2; openh5_uuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; uuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; wm_order_channel=default; __mta=88962724.1553241813138.1553241813138.1553241813138.1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _ga=GA1.3.1512793742.1553241789; _lxsdk=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; _lxsdk_cuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8',
                'Accept':'application/json',
                'Referer':'http://h5.waimai.meituan.com/waimai/mindex/home',
                'Origin':'http://h5.waimai.meituan.com',
                'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
                'Content-Type':'application/x-www-form-urlencoded'
            }
            proxies={
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }
            data='startIndex=0&sortId=0&multiFilterIds=&sliderSelectCode=&sliderSelectMin=&sliderSelectMax=&geoType=2&rankTraceId=&wm_latitude=31414902&wm_longitude=121342657&wm_actual_latitude=0&wm_actual_longitude=0&_token='
            response = requests.post('http://i.waimai.meituan.com/openh5/homepage/poilist?_=', 
                headers=headers,
                proxies=proxies, 
                data=data,
                timeout=TEST_TIMEOUT)
            print(response.status_code)
            if response.status_code == 200:
                return True
        except (ConnectionError, ReadTimeout):
            return False

    def remove_proxy(self):
        """
        移除代理
        :return: None
        """
        self.redis = RedisClient()
        self.redis.remove(CLIENT_NAME)
        print('Successfully Removed Proxy')

    def set_proxy(self, proxy):
        """
        设置代理
        :param proxy: 代理
        :return: None
        """
        self.redis = RedisClient()
        if self.redis.set(CLIENT_NAME, proxy):
            print('Successfully Set Proxy', proxy)

    def adsl(self):
        """
        拨号主进程
        :return: None
        """
        while True:
            print('ADSL Start, Remove Proxy, Please wait')
            try:
                self.remove_proxy()
            except:
                while True:
                    (status, output) = subprocess.getstatusoutput(ADSL_BASH)
                    if status == 0:
                        self.remove_proxy()
                        break
            (status, output) = subprocess.getstatusoutput(ADSL_BASH)
            if status == 0:
                print('ADSL Successfully')
                ip = self.get_ip()
                if ip:
                    print('Now IP', ip)
                    print('Testing Proxy, Please Wait')
                    proxy = '{ip}:{port}'.format(ip=ip, port=PROXY_PORT)
                    if self.test_proxy(proxy):
                        print('Valid Proxy')
                        self.set_proxy(proxy)
                        print('Sleeping')
                        time.sleep(ADSL_CYCLE)
                    else:
                        print('Invalid Proxy')
                else:
                    print('Get IP Failed, Re Dialing')
                    time.sleep(ADSL_ERROR_CYCLE)
            else:
                print('ADSL Failed, Please Check')
                time.sleep(ADSL_ERROR_CYCLE)


def run():
    sender = Sender()
    sender.adsl()


if __name__ == '__main__':
    run()
