import requests
# curl -x 119.5.77.15:8888 
# 'http://i.waimai.meituan.com/openh5/homepage/poilist?_=&X-FOR-WITH=uSEjoE0N%2F0mcbzmXMjgjTn39etHmsuR7oNr2bwCs4CkTuvXG7%2B0KFFMSNRKv0uq8CHYi8dnuDmLo9u6BidiG5BfAAhqclb2AovMjTf2t5HT7kvjyQiRpPq3Dgg0KkKbrxX2vConslYMxxyjMNUiWgQ%3D%3D' 
# -H 'Cookie: openh5_uuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; terminal=i; w_actual_lat=31187016; w_actual_lng=121422285; w_latlng=0,0; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_visitid=b741a8e4-1548-4fec-855a-224ca00535d6; _lxsdk_s=169b8900f14-469-004-eeb%7C%7C2; openh5_uuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; uuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; wm_order_channel=default; __mta=88962724.1553241813138.1553241813138.1553241813138.1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _ga=GA1.3.1512793742.1553241789; _lxsdk=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; _lxsdk_cuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8' 
# -H 'Accept: application/json' 
# -H 'Referer: http://h5.waimai.meituan.com/waimai/mindex/home' 
# -H 'Origin: http://h5.waimai.meituan.com' 
# -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1' 
# -H 'Content-Type: application/x-www-form-urlencoded' 
# --data 'startIndex=0&sortId=0&multiFilterIds=&sliderSelectCode=&sliderSelectMin=&sliderSelectMax=&geoType=2&rankTraceId=&wm_latitude=31414902&wm_longitude=121342657&wm_actual_latitude=0&wm_actual_longitude=0&_token=' --compressed
headers = {
    'Cookie':'openh5_uuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; terminal=i; w_actual_lat=31187016; w_actual_lng=121422285; w_latlng=0,0; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_visitid=b741a8e4-1548-4fec-855a-224ca00535d6; _lxsdk_s=169b8900f14-469-004-eeb%7C%7C2; openh5_uuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; uuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; wm_order_channel=default; __mta=88962724.1553241813138.1553241813138.1553241813138.1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _ga=GA1.3.1512793742.1553241789; _lxsdk=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8; _lxsdk_cuid=169a3b30d43c8-068b95967384008-481d3500-fa000-169a3b30d43c8',
    'Accept':'application/json',
    'Referer':'http://h5.waimai.meituan.com/waimai/mindex/home',
    'Origin':'http://h5.waimai.meituan.com',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Content-Type':'application/x-www-form-urlencoded'
}
proxies={
    'http': 'http://' + '119.5.77.15:8888',
    'https': 'http://' + '119.5.77.15:8888'
}
# data = {
#     'startIndex':0,
#     'sortId':0,
#     'multiFilterIds':'',
#     'sliderSelectCode':'',
#     'sliderSelectMin':'',
#     'sliderSelectMax':'',
#     'geoType':2,
#     'rankTraceId':'',
#     'wm_latitude':31414902,
#     'wm_longitude':121342657,
#     'wm_actual_latitude':0,
#     'wm_actual_longitude':0,
#     '_token':''

# }
data='startIndex=0&sortId=0&multiFilterIds=&sliderSelectCode=&sliderSelectMin=&sliderSelectMax=&geoType=2&rankTraceId=&wm_latitude=31414902&wm_longitude=121342657&wm_actual_latitude=0&wm_actual_longitude=0&_token='
response = requests.post('http://i.waimai.meituan.com/openh5/homepage/poilist?_=', 
headers=headers,
proxies=proxies, 
data=data,
timeout=10000)
print(response.text)