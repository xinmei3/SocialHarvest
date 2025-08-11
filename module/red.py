import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from common.requests_common import RequestsCommon


user_id = '1180458703'  # 替换为你的用户ID
max_id = None
URL_RED = "https://www.xiaohongshu.com/user/profile/5ff94a1d000000000100bf27?xhsshare=CopyLink&appuid=609513cd000000000101e44f&apptime=1681699386"


HEADER_RED = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',  # 替换为你的User-Agent
    'Cookie': 'abRequestId=d73583d2-86f3-5e76-aa0a-6c61bd8330f6; a1=19319b5c06aem8zq1z7vao3nnc0jf0t6x6whei01250000374805; webId=101d894b99c69a3cd926c5ecf0cc2e64; gid=yjqyjD2fyWC2yjqyjD2S8K38K0d6YuAyuWh0EyJlqIIS8x28Vi89Kd888qW4Y82880Y802iD; x-user-id-creator.xiaohongshu.com=61b1675c000000001000e4fb; customerClientId=478402480106079; xsecappid=xhs-pc-web; acw_tc=0a00d62217524201274523713e84ec43eef720f2d9f6c1042087e4847bed57; webBuild=4.72.0; loadts=1752420096742; websectiga=82e85efc5500b609ac1166aaf086ff8aa4261153a448ef0be5b17417e4512f28; sec_poison_id=9f0c09fa-4ce0-43a8-964e-6bc3a4e23b95; web_session=040069b1e1508557b4192587463a4b268b8661',
    'Referer': 'https://www.xiaohongshu.com/',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}

def get_red_user_info():
    response = requests.get(URL_RED, headers=HEADER_RED)
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return None
    if not response.text:
        print("响应内容为空")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    script = soup.find_all('script')[-1]

    state = str(script).replace('<script>', '').replace('</script>', '')
    state_with_script = state.replace('window.__INITIAL_STATE__=', '')
    state_with_script = state_with_script.replace('undefined', 'null')

    try:
        red_user_data = json.loads(state_with_script)
    except json.JSONDecodeError as e:
        print(f"解析JSON失败: {e}")
        return None

    basicInfo = red_user_data['user']['userPageData']['basicInfo']
    nickname = basicInfo['nickname'] # 用户昵称
    user_id = basicInfo['redId'] # 小红书号
    ip_location = basicInfo['ipLocation'] # IP位置
    description = basicInfo['desc']  # 用户简介

    interactions = red_user_data['user']['userPageData']['interactions']
    follows = 0
    fans = 0
    interaction = 0
    for item in interactions:
        if item['type'] == 'follows':
            follows = int(item['count'])
        elif item['type'] == 'fans':
            fans = int(item['count'])
        elif item['type'] == 'interaction':
            # interaction = item['count']
            interaction = int(item['count'])

    user_info = {
        '昵称'      : nickname,
        '小红书号'   : user_id,
        'IP属地'    : ip_location,
        '简介'     : description,
        '关注数'   : follows,
        '粉丝数'   : fans,
        '获赞与收藏': interaction
    }
    return user_info


if __name__ == "__main__":
    user_info = get_red_user_info()
    if user_info is None:
        print("未获取到用户信息")
        exit()
    else:
        print(f"昵称:       {user_info['昵称']}")
        print(f"小红书号:   {user_info['小红书号']}")
        print(f"IP属地:     {user_info['IP属地']}")
        print(f"简介:       {user_info['简介']}")
        print(f"关注数:     {user_info['关注数']}")
        print(f"粉丝数:     {user_info['粉丝数']}")
        print(f"获赞与收藏: {user_info['获赞与收藏']}")
