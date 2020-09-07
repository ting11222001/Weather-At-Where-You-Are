# Libraries for below main construction block - index function.
# Allow users to make a request to a web page e.g. an external API to get data.
import requests
import find_nearest

# Read the API keys from the .env file and use them
import os
from dotenv import load_dotenv
load_dotenv()

def pop6h_forecast():
    # 抓最近氣象站的逐6小時兩天內降雨機率趨勢
    # 鄉鎮天氣預報-全臺灣各鄉鎮市區預報資料 F-D0047-093
    # required arguments: dataid & locationId
    locationId_dic = {
    '宜蘭縣': 'F-D0047-001',
    '桃園市': 'F-D0047-005',
    '新竹縣': 'F-D0047-009',
    '苗栗縣': 'F-D0047-013',
    '彰化縣': 'F-D0047-017',
    '南投縣': 'F-D0047-021',
    '雲林縣': 'F-D0047-025',
    '嘉義縣': 'F-D0047-029',
    '屏東縣': 'F-D0047-033',
    '臺東縣': 'F-D0047-037',
    '花蓮縣': 'F-D0047-041',
    '澎湖縣': 'F-D0047-045',
    '基隆市': 'F-D0047-049',
    '新竹市': 'F-D0047-053',
    '嘉義市': 'F-D0047-057',
    '臺北市': 'F-D0047-061',
    '高雄市': 'F-D0047-065',
    '新北市': 'F-D0047-069',
    '臺中市': 'F-D0047-073',
    '臺南市': 'F-D0047-077',
    '連江縣': 'F-D0047-081',
    '金門縣': 'F-D0047-085'}
    # 接API
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-093?Authorization={}&locationId={}&locationName={}&format={}&elementName={}&sort={}'
    auth_arg = os.getenv('PROJECT_API_KEY')
    weather, my_lat, my_lon = find_nearest.find_nearest()
    # locationId: 縣市
    if weather['station_city'] in locationId_dic:
        locationId_arg = locationId_dic[weather['station_city']]
    # locationName: 鄉鎮
    locationName_arg = weather['station_town']
    # 回傳資料格式
    format_arg = 'JSON'
    # PoP6h: 降雨機率6小時分段
    ele_arg = 'PoP6h'
    # time: 升冪排序 
    sort_arg = 'time'
    req = requests.get(url.format(auth_arg, locationId_arg, locationName_arg, format_arg, ele_arg, sort_arg)).json()
    data = req['records']['locations'][0]
    data_location = data['location'][0]
    data_pop6h = data_location['weatherElement'][0]
    data_pop6h_time = data_pop6h['time']
    # 回傳json檔
    data_pop6h_time_dic = {}
    for point in data_pop6h_time:
        start_time = point['startTime']
        pop6h_value = point['elementValue'][0]['value']
        data_pop6h_time_dic[start_time] = int(pop6h_value)
    return data_pop6h_time_dic
