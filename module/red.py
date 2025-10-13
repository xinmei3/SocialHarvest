import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from requesets_lib.common.user_info_manager import UserInfo


HEADER_RED = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',  # 替换为你的User-Agent
    'Cookie': 'abRequestId=d73583d2-86f3-5e76-aa0a-6c61bd8330f6; a1=19319b5c06aem8zq1z7vao3nnc0jf0t6x6whei01250000374805; webId=101d894b99c69a3cd926c5ecf0cc2e64; gid=yjqyjD2fyWC2yjqyjD2S8K38K0d6YuAyuWh0EyJlqIIS8x28Vi89Kd888qW4Y82880Y802iD; x-user-id-creator.xiaohongshu.com=61b1675c000000001000e4fb; customerClientId=478402480106079; xsecappid=xhs-pc-web; acw_tc=0a00d5b317592411126147129e703d29825f0b5b76a6b3d8783a02715f77ca; webBuild=4.81.0; loadts=1759241110811; websectiga=3fff3a6f9f07284b62c0f2ebf91a3b10193175c06e4f71492b60e056edcdebb2; sec_poison_id=de2d42a9-81c2-4131-9f9b-35ac2636fca4; web_session=040069b1e1508557b419d8abee3a4bfea11c5b; unread={%22ub%22:%2268d949ca000000001003e277%22%2C%22ue%22:%2268d7af02000000001101d636%22%2C%22uc%22:32}',
    'Referer': 'https://www.xiaohongshu.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}

user_info = UserInfo.user_info_loader()
user_info_red = user_info["red"]

URL_RED = user_info_red["url"]


def get_red_user_info():
    response = requests.get(URL_RED, headers=HEADER_RED)
    # response = requests.get(user_info_red["url"], HEADER_RED)
    if response.status_code != 200:
        print(f"get_red_user_info: 请求失败，状态码: {response.status_code}")
        return None
    if not response.text:
        print("get_red_user_info: 响应内容为空")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    script = soup.find_all('script')[-1]

    state = str(script).replace('<script>', '').replace('</script>', '')
    state_with_script = state.replace('window.__INITIAL_STATE__=', '')
    state_with_script = state_with_script.replace('undefined', 'null')

    # pprint(state_with_script)

    try:
        red_user_data = json.loads(state_with_script)
    except json.JSONDecodeError as e:
        print(f"get_red_user_info: 解析JSON失败: {e}")
        return None

    basicInfo = red_user_data['user']['userPageData']['basicInfo']
    nickname = basicInfo['nickname'] # 用户昵称
    user_id = basicInfo['redId'] # 小红书号
    ip_location = basicInfo['ipLocation'] # IP位置
    description = basicInfo['desc']  # 用户简介
    notes = red_user_data['user']['notes']  # 作品数，某些用户可能没有该字段
    note_count = 0
    for note in notes:
        if note:
            note_count += 1
        else:
            break
    
    interactions = red_user_data['user']['userPageData']['interactions']
    follows = 0
    fans = 0
    interaction = 0
    for item in interactions:
        if item['type'] == 'follows':
            try:
                follows = int(item['count'])
            except ValueError:
                follows = item['count']
        if item['type'] == 'fans':
            try:
                fans = int(item['count'])
            except ValueError:
                fans = item['count']
        if item['type'] == 'interaction':
            try:
                interaction = int(item['count'])
            except ValueError:
                interaction = item['count']

    user_info = {
        '昵称'       : nickname,
        '小红书号'   : user_id,
        'IP属地'     : ip_location,
        '简介'       : description,
        '作品数'     : note_count,
        '关注数'     : follows,
        '粉丝数'     : fans,
        '获赞与收藏' : interaction
    }
    print("get_red_user_info:", user_info)

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
