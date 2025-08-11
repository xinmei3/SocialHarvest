import requests
import json
from pprint import pprint
import time


URL_TIKTOK_LIKE_FIRST = "https://www-hj.douyin.com/aweme/v1/web/aweme/favorite/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAHpssvF9y7F9lx-CAY8EKmdMnUTHkcNiT6EKXgX3iXh0&max_cursor=0&min_cursor=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&pc_libra_divert=Windows&support_h265=1&support_dash=1&cpu_core_num=12&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2560&screen_height=1440&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=137.0.0.0&browser_online=true&engine_name=Blink&engine_version=137.0.0.0&os_name=Windows&os_version=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7421552512153306650&uifid=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4109a12adc1c3f7f26fa2b018a176235714142f663feeb21098188bf4013ef366563741f139de2078c9fe5c5a9e16e2b0c7d1fa1e6624a6be9bdcdcb270eaa660f92d81e5155ac350e039912a6ddffd03617a15174e734d88135a7a0ab96909e4333c0f699250832af144f04604d513c7b0a65888de3d30b6af5a78714ceff2af&verifyFp=verify_mbs1oaak_WY03Wp9U_cfBg_4bEJ_Aei1_JI2G1u9OeiAN&fp=verify_mbs1oaak_WY03Wp9U_cfBg_4bEJ_Aei1_JI2G1u9OeiAN&msToken=OchEA_NH_w9VIA_OqXwUhMJB9cK1PkwQKNFgKxRRVVo_mXOuc--FvgYZ0AT3Y1uzbgpgmpxj44JGewu58EM-GSe9OVeO7QuI8ehnCUVO3L3hQqfYXmL6xD0axJCctSOXKmSDeNk4y2-I0_7v5D82cSc5JyUkBKgoog1UVO5WoZOHuIcZuMx-CEY%3D&a_bogus=mJURgeXJQpQVPdMtuKaDt43lkA9lrs8ywPT2SacP7OP6G1zau8N-dxcHjxLR-FgPNSpkw9I77EUlYdxcKGUsZFrkqmkkuTzjwzI5IgmL2qwVTMX%2FLrfxCwsqyJHT8OiE8coyJIUlWU5OIdC4g3aiUB59CApJ4QJpQHa6dr4GT9tf6MG9PHFQuPbdEXFnBQo-uj%3D%3D"

HEADERS_TIKTOK = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "Cookie": "ttwid=1%7CC4e-ctAMuvxO7ja29TcPNSp5XZENpRGti1rHvoHUfuM%7C1727964868%7C7b1f3167986b7ab81089adfc061db3349af60a5c3ac5a3c9c5c11a5e8e1f87cd; UIFID_TEMP=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4109a12adc1c3f7f26fa2b018a1762357c2147030d2f37cbe71dd62a1f0efb64858788dc82aa484c683b2008a0f453159; hevc_supported=true; xgplayer_user_id=54110199621; fpk1=U2FsdGVkX1+39hdgmbDj6T8ShBekr3lUFPbfPTHsGrngj45fMR/tuRX2Xm26MogEWquBA4iMEZkhIQKSOR0XfA==; fpk2=d94a27a56e6a143d4c900b9014d6ba5d; bd_ticket_guard_client_web_domain=2; UIFID=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4109a12adc1c3f7f26fa2b018a176235714142f663feeb21098188bf4013ef366563741f139de2078c9fe5c5a9e16e2b0c7d1fa1e6624a6be9bdcdcb270eaa660f92d81e5155ac350e039912a6ddffd03617a15174e734d88135a7a0ab96909e4333c0f699250832af144f04604d513c7b0a65888de3d30b6af5a78714ceff2af; SelfTabRedDotControl=%5B%5D; store-region=cn-ln; store-region-src=uid; live_use_vvc=%22false%22; xgplayer_device_id=40266552717; is_dash_user=1; my_rd=2; d_ticket=3bfbb5672b9a2898b27d109744e1514afd824; s_v_web_id=verify_m98o1t5a_8ntZgkr9_RCtL_4tqm_8c5s_zREsXpAbujws; passport_csrf_token=d116ea1f2ab856f488845f2f2e530dbc; passport_csrf_token_default=d116ea1f2ab856f488845f2f2e530dbc; SearchMultiColumnLandingAbVer=1; SEARCH_RESULT_LIST_TYPE=%22multi%22; __security_mc_1_s_sdk_crypt_sdk=14cc0c37-43ba-a2c7; __security_mc_1_s_sdk_cert_key=69b62ff1-4b0a-a83e; MONITOR_WEB_ID=c57da653-e729-4937-a49d-6db89a37363b; is_staff_user=false; __security_mc_1_s_sdk_sign_data_key_sso=d6634e8b-46f0-8b05; __security_mc_1_s_sdk_sign_data_key_web_protect=6656f954-4446-a32d; download_guide=%223%2F20250525%2F0%22; EnhanceDownloadGuide=%220_0_1_1748184304_0_0%22; dy_swidth=2560; dy_sheight=1440; publish_badge_show_info=%220%2C0%2C0%2C1748618192417%22; strategyABtestKey=%221748653548.272%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.759%7D; douyin.com; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; sso_uid_tt=fff63e7b3089120b0c3701d85bf85472; sso_uid_tt_ss=fff63e7b3089120b0c3701d85bf85472; toutiao_sso_user=dccde6283a76508a6310aa180051b2dd; toutiao_sso_user_ss=dccde6283a76508a6310aa180051b2dd; sid_ucp_sso_v1=1.0.0-KGYyZDE5YTk0YjUxZTEzZGE3MTliYWI1OTM5MTYxNzM4YWNmM2UwYzQKCRDD7urBBhjvMRoCbGYiIGRjY2RlNjI4M2E3NjUwOGE2MzEwYWExODAwNTFiMmRk; ssid_ucp_sso_v1=1.0.0-KGYyZDE5YTk0YjUxZTEzZGE3MTliYWI1OTM5MTYxNzM4YWNmM2UwYzQKCRDD7urBBhjvMRoCbGYiIGRjY2RlNjI4M2E3NjUwOGE2MzEwYWExODAwNTFiMmRk; __ac_nonce=0683ab7430090b8f08cd0; __ac_signature=_02B4Z6wo00f01wFGWZgAAIDAnyL5C4krlHcBZl0AAKh1MkAXr1MKdWHMBeh6NUVFaK-uQrPpoqZxQ4TJclA4qq6dyl2LLSn10KG79SPOjazO5eumf5feg79f1FBPRK4mPlhcPc2jRtccQ.Tn29; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2560%2C%5C%22screen_height%5C%22%3A1440%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; biz_trace_id=dfcf38a3; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2736353d3632313d32333d313234272927676c715a75776a716a666a69273f2763646976602778; bit_env=zhYL6nDKT0jiVkqtlbKUh-hsy1VjcxCs68Hy-2hVXqp8v_cRgxQ_LwrnlPbyt0q1wo1XM3m5OB9WQtk-s905teouGOZj3MKX6I0IKIMp8OYjYTgoxZNqEbOLCYV7eBvXBo69hcz1g8QzL1yY7-pzPVJ9XPeNGvmkns5djNs0vZQylRUZdkYKD_-vNKwu40rVVzCQyL9TDOKKgm26fyIVUIUgqouwRucUuz4fI8zQvIbZgjIYmqA_vB_7hjSExk6MlfsKOfhiHzk-NhBOncrD0j6fAXKthY4QlLS3mNPzoH5dzL8t90TbNFYau-yDorfJ44JxBEaAoYVtRxnzCb-N1GFUZDgubba3iaEq8Mj4cm-1p4rlnQfza7zqKkALrwsF9uEoAtla2qOzUlueFa_-sAu4mfjFHl_C7IQgIWTSjsIqozwIJEAGayt9eGdLRw1lo91CQUiqo03BRIzekQnUBJhBYUewZy3wC7NRPCmyWlnoRbd-bjPqZJWSt44w3gUsumB3TV41SqicNiR4o5d5wyHcHe-SHd1d8ERm_dPv1po%3D; gulu_source_res=eyJwX2luIjoiMWUyYmM4OTQ1ZmExYWFmYjRiYmI4YTNjYmFiNDRkNjcwZmE2NjE5YWNiMjk0ZTIxYWY0NDJjNGRiYjU1ODAwNSJ9; passport_auth_mix_state=k6w8l8dpn45xzn4ba68f025zbt9lz8vba783q3ew8yx1rrif; passport_assist_user=ClPoUi9xevFLJR7zNckiWvLrRcY30Bn127Fwr8_eXWkYuwWUgfA-qEXpeIIAIwogoD9ME-P3pswnYPQL6ED-vj31OfPl7-YTYI7MBk3Tw4_pWE9STRpKCjy35xjoKonjS1-ASBOFiQqENioSq9jBradFf9esEUoi5PMoSo3SPDPdhkVrOeLxWJk-HtRDaAh87NmrhUkQ1evyDRiJr9ZUIAEiAQNrW2UI; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sid_guard=ce73c1f0c5977dfaba027af002a73bf4%7C1748678498%7C5184000%7CWed%2C+30-Jul-2025+08%3A01%3A38+GMT; uid_tt=b39da3d42329f3c634ee77190bfccb36469fbfe816ecfaac0efff6713f6c16c8; uid_tt_ss=b39da3d42329f3c634ee77190bfccb36469fbfe816ecfaac0efff6713f6c16c8; sid_tt=ce73c1f0c5977dfaba027af002a73bf4; sessionid=ce73c1f0c5977dfaba027af002a73bf4; sessionid_ss=ce73c1f0c5977dfaba027af002a73bf4; sid_ucp_v1=1.0.0-KGU3NDBhYWM0NzZmZjA5M2IzNzk2MWVjZTI4YWJlNjljMjRmNWI3NTcKIgi8iJSym4H8kGgQ4u7qwQYY7zEgDDD85IfBBjgHQPQHSAQaAmhsIiBjZTczYzFmMGM1OTc3ZGZhYmEwMjdhZjAwMmE3M2JmNA; ssid_ucp_v1=1.0.0-KGU3NDBhYWM0NzZmZjA5M2IzNzk2MWVjZTI4YWJlNjljMjRmNWI3NTcKIgi8iJSym4H8kGgQ4u7qwQYY7zEgDDD85IfBBjgHQPQHSAQaAmhsIiBjZTczYzFmMGM1OTc3ZGZhYmEwMjdhZjAwMmE3M2JmNA; login_time=1748678498635; _bd_ticket_crypt_cookie=915c5a961e9ea450b942aa187a3c06f4; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAyZkTH0g5o-M-mr26gp5tM_ScFLMaY3kPEgipGtKVFxTOSVAvCBKUrDQ4MCGOeQtY%2F1748707200000%2F0%2F1748678500166%2F0%22; __security_server_data_status=1; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQjFWYkxlUHkzcVZVOW54ampjTEtuSE9QZStmaVg3dWR3N2p5OU9FOGhqY1I5ZlFvd3puVmVsVTd5aSt2YXVjaGxMT3J1cXVqbUljMWVKVndJaWhISnM9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A1%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; home_can_add_dy_2_desktop=%221%22; odin_tt=3a4fec3d9baf3b91189545b6813ff7247983d0ebc25147a923f5bc337df6faa1e4c61284f96ecf91473eaa54bb1647da2d2ee7a44f49432ed86c05464b4abe58; WallpaperGuide=%7B%22showTime%22%3A1748662482322%2C%22closeTime%22%3A0%2C%22showCount%22%3A6%2C%22cursor1%22%3A146%2C%22cursor2%22%3A46%2C%22hoverTime%22%3A1746868266057%7D; xg_device_score=7.630007575365517; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAyZkTH0g5o-M-mr26gp5tM_ScFLMaY3kPEgipGtKVFxTOSVAvCBKUrDQ4MCGOeQtY%2F1748707200000%2F0%2F1748678516319%2F0%22; IsDouyinActive=false; passport_fe_beating_status=false",
    "Referer" : "https://www.douyin.com/",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive"
}

FILE_PATH = 'C:\\Users\\张耀文\\Documents\\requesets_lib\\user_info\\'
FILE_TIKTOK_LIKE_LIST = 'tiktok_like_list.txt'


def time_stamp():
    time_stamp = time.time()
    local_time = time.localtime(time_stamp)
    str_time = time.strftime('%Y%m%d%H%M%S', local_time)
    return str_time


def get_like_list(filename):
    """
    获取抖音用户的喜欢列表filename
    :return: 返回喜欢列表数据
    """
    response = requests.get(URL_TIKTOK_LIKE_FIRST, headers=HEADERS_TIKTOK)
    like_list = []
    if response.status_code == 200:
        like_list_json = response.json()
        for num in range(len(like_list_json['aweme_list'])):
            for item in like_list_json['aweme_list']:
                list_like = []
                list_like.append({
                    # '序号': num + 1,  # 序号
                    '标题': item['desc'],  # 标题
                    '视频id': item['aweme_id'],  
                    '作者昵称': item['author']['nickname'],  # 作者昵称
                    '点赞数': item['statistics']['digg_count'],  # 点赞数
                    '评论数': item['statistics']['comment_count'],  # 评论数
                    '分享数': item['statistics']['share_count'],  # 分享数
                    '视频播放地址': item['video']['play_addr']['url_list'][0],  # 视频播放地址
                    '创建时间': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['create_time'])),  # 创建时间
                    '描述': item.get('desc', '')  # 描述
                })
                like_list.append(list_like)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(like_list, f, ensure_ascii=False, indent=4)
        return like_list
    else:
        response.raise_for_status()


if __name__ == "__main__":
    like_list_json = get_like_list(filename=FILE_PATH + FILE_TIKTOK_LIKE_LIST)
    print("TikTok Like List:")
    for item in like_list_json:
        pprint(item)
    # with open('tiktok_like_list_{}.json'.format(time_stamp()), 'w', encoding='utf-8') as f:
    #     json.dump(like_list_json, f, ensure_ascii=False, indent=4)
