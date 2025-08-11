from common.requests_common import RequestsCommon
from common.user_info_loader import UserInfo
from pprint import pprint


REFERER_WEIBO = "https://weibo.com/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
CONNECTION_KEEP_ALIVE = "keep-alive"

HEADERS_WEIBO = {
    "User-Agent": USER_AGENT,
    "Cookie": "SINAGLOBAL=5172920912928.578.1727964718316; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW4VRKkCD0umBECsWzgziLV5JpX5KMhUgL.FoepS02Neoe0SKz2dJLoIpfki--fiKnNiKL2i--Ni-2Ei-2Ni--ci-zpi-27P7tt; ULV=1752159289522:61:5:2:3236626450464.7324.1752159289465:1751900668471; XSRF-TOKEN=v4SCoDe0QCZBjymGVQPm5ufa; ALF=1755099333; SUB=_2A25FcVOVDeRhGeVP7FMW8i3Pzj6IHXVmD-ldrDV8PUJbkNANLXnakW1NTPTpcyxcgQ-Y-9pFDDNPYQbnooCoArUf; WBPSESS=CtdwwwCyKWEc2EnGhvgdz08FSQGbJtHve5paM47jkDgYO1BS7ihKbRXsJFBLAyPc7gHemAIToB7gCziEy7Sh9jtKOPTPoZMQ0xZyHpOOz_Q4aIeeqg-AZ_BUWACy3uTEd88wxfMye9G92nX8rh4xiw==",
    "Referer": REFERER_WEIBO,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": CONNECTION_KEEP_ALIVE
}

USER_ID = "5752655895"
URL_WEIBO_HOME = "https://weibo.com/ajax/profile/info?uid=5752655895"

user_info = UserInfo.user_info_loader()
user_info_weibo = user_info["weibo"]

requests_common = RequestsCommon()

class getWeiboInfo:
    def __init__(self):
        self.url = URL_WEIBO_HOME
        self.headers = user_info_weibo["headers"]
        self.followers_count = None
        self.friends_count = None

    def get_fans_data(self, user_id):
        url = "https://weibo.com/ajax/friendships/friends?relate=fans&page={}&uid={}&type=all&newFollowerCount=0"

        response_json = requests_common.get_json(url.format(1, user_id), headers=HEADERS_WEIBO)
        fans_info = response_json['users']            # 获取第一页的粉丝列表
        fans_count = response_json['total_number']    # 获取总粉丝数
        for num in range(2, (fans_count // 20) + 2):
            response_json = requests_common.get_json(url.format(num, user_id), headers=HEADERS_WEIBO)
            fans_info.extend(response_json['users'])

        return fans_info, fans_count

    def get_follower_data(self, user_id):
        # url = "https://weibo.com/ajax/friendships/friends?page={}&uid={}"
        url = user_info_weibo["url_fans"]

        response_json = requests_common.get_json(url.format(1, user_id), headers=HEADERS_WEIBO)
        followers_info = response_json['users']            # 获取第一页的关注列表
        followers_count = response_json['total_number']    # 获取总关注数
        for num in range(2, (followers_count // 20) + 2):
            response_json = requests_common.get_json(url.format(num, user_id), headers=HEADERS_WEIBO)
            followers_info.extend(response_json['users'])

        return followers_info, followers_count

    def get_weibo_user_info(self):
        # response_json = requests_common.get_json(URL_WEIBO_HOME, headers=HEADERS_WEIBO)
        response_json = requests_common.get_json(user_info_weibo["url_home"], user_info_weibo["headers"])

        weibo_info_xiang = response_json['data']['user']
        nickname = weibo_info_xiang["screen_name"]                                             # 昵称
        signature = weibo_info_xiang["description"]                                            # 简介
        likes_received_all = weibo_info_xiang["status_total_counter"]["total_cnt_format"]      # 转评赞
        comments_received = int(weibo_info_xiang["status_total_counter"]["comment_cnt"])       # 累计评论量
        likes_received = int(weibo_info_xiang["status_total_counter"]["like_cnt"])             # 累计获赞
        followers_count = weibo_info_xiang["followers_count"]                                  # 粉丝
        friends_count = weibo_info_xiang["friends_count"]                                      # 关注
        statuses_count = weibo_info_xiang["statuses_count"]                                    # 微博数

        user_info = {
            "昵称"       : nickname,
            "简介"       : signature,
            "转评赞"     : likes_received_all,
            "累计评论量" : comments_received,
            "累计获赞"   : likes_received,
            "粉丝数"     : followers_count,
            "关注数"     : friends_count,
            "微博数"     : statuses_count
        }
        return user_info


if __name__ == "__main__":
    weibo_info = getWeiboInfo()
    user_info = weibo_info.get_weibo_user_info()
    if user_info:
        print(f"昵称: {user_info['昵称']}")
        print(f"简介: {user_info['简介']}")
        print(f"总获赞数: {user_info['转评赞']}")
        print(f"评论量: {user_info['累计评论量']}")
        print(f"获赞数: {user_info['累计获赞']}")
        print(f"粉丝数: {user_info['粉丝数']}")
        print(f"关注数: {user_info['关注数']}")
        print(f"微博数: {user_info['微博数']}")
    else:
        print("未能获取用户信息")
    # follower_data, followers_count = weibo_info.get_follower_data(USER_ID)
    follower_data, followers_count = weibo_info.get_follower_data(user_info_weibo["user_id"])
    fans_data, followers_count = weibo_info.get_fans_data(USER_ID)
    # with open('weibo_user_follower_info.json', 'w', encoding='utf-8') as f:
    #     json.dump(follower_data, f, ensure_ascii=False, indent=4)
    for idx, item in enumerate(follower_data):
        print(f"{idx+1}   昵称: {item['screen_name']}, \t主页链接: https://weibo.com/u/{item['id']}, 关注数: {item['followers_count']}, 粉丝数: {item['friends_count']}")
