import requests

def test_api():
    print('test_api_start')
    headers = {
        'Cookie':'uuid=1697b5d4f23c8-0d425bb2fadf7f3505-481d3500-fa000-1697b5d4f23c8; _lx_utm=utm_source%3D60066; _lxsdk=1697b5d4f23c8-0d425bb27f3505-481d3500-fa000-1697b5d4f23c8; _lxsdk_cuid=1697b5d4f23c8-0d425bb27f3505-481d3500-fa000-1697b5d4f23c8; wm_order_channel=default;w_actual_lat=31187016;w_actual_lng=121422285;w_latlng=0,0;',
        'Accept':'application/json',
        'Referer':'http://h5.waimai.meituan.com/waimai/mindex/kingkong?navigateType=910&firstCategoryId=910&secondCategoryId=910&title=%E7%BE%8E%E9%A3%9F',
        'Origin':'http://h5.waimai.meituan.com',
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Content-Type':'application/x-www-form-urlencoded'
    }
    # proxies={
    #     'http': 'http://' + '119.5.77.15:8888',
    #     'https': 'http://' + '119.5.77.15:8888'
    # }
    data='startIndex=0&sortId=&navigateType=910&firstCategoryId=910&secondCategoryId=910&multiFilterIds=&sliderSelectCode=&sliderSelectMin=&sliderSelectMax=&actualLat=&actualLng=&initialLat=31.414902&initialLng=121.342657&geoType=2&rankTraceId=&wm_latitude=31414902&wm_longitude=121342657&wm_actual_latitude=0&wm_actual_longitude=0&_token=' 
    response = requests.post('http://i.waimai.meituan.com/openh5/channel/kingkongshoplist?_=', 
        headers=headers,
        # proxies=proxies, 
        data=data,
        timeout=10000)
    print(response.text)

test_api()
