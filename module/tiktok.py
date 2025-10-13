# -*- coding: utf-8 -*-
import os
from requesets_lib.common.user_info_manager import UserInfo
from requesets_lib.common.requests_common import RequestsCommon
from requesets_lib.common.database import DataBase
from requesets_lib.common.process_str import remove_emoji, safe_file_name, format_time_string
import requesets_lib.module.tiktok_video as tiktok_video
import requesets_lib.module.tiktok_like_video as tiktok_like_video
from pprint import pprint


user_info = UserInfo.user_info_loader()
user_info_tiktok = user_info["tiktok"]

database = DataBase()
requests_common = RequestsCommon()

HEADERS_TIKTOK = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "Cookie": "ttwid=1%7CC4e-ctAMuvxO7ja29TcPNSp5XZENpRGti1rHvoHUfuM%7C1727964868%7C7b1f3167986b7ab81089adfc061db3349af60a5c3ac5a3c9c5c11a5e8e1f87cd; UIFID_TEMP=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4109a12adc1c3f7f26fa2b018a1762357c2147030d2f37cbe71dd62a1f0efb64858788dc82aa484c683b2008a0f453159; hevc_supported=true; xgplayer_user_id=54110199621; fpk1=U2FsdGVkX1+39hdgmbDj6T8ShBekr3lUFPbfPTHsGrngj45fMR/tuRX2Xm26MogEWquBA4iMEZkhIQKSOR0XfA==; fpk2=d94a27a56e6a143d4c900b9014d6ba5d; bd_ticket_guard_client_web_domain=2; UIFID=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4109a12adc1c3f7f26fa2b018a176235714142f663feeb21098188bf4013ef366563741f139de2078c9fe5c5a9e16e2b0c7d1fa1e6624a6be9bdcdcb270eaa660f92d81e5155ac350e039912a6ddffd03617a15174e734d88135a7a0ab96909e4333c0f699250832af144f04604d513c7b0a65888de3d30b6af5a78714ceff2af; SelfTabRedDotControl=%5B%5D; store-region=cn-ln; store-region-src=uid; live_use_vvc=%22false%22; xgplayer_device_id=40266552717; is_dash_user=1; my_rd=2; d_ticket=3bfbb5672b9a2898b27d109744e1514afd824; s_v_web_id=verify_m98o1t5a_8ntZgkr9_RCtL_4tqm_8c5s_zREsXpAbujws; passport_csrf_token=d116ea1f2ab856f488845f2f2e530dbc; passport_csrf_token_default=d116ea1f2ab856f488845f2f2e530dbc; SearchMultiColumnLandingAbVer=1; SEARCH_RESULT_LIST_TYPE=%22multi%22; __security_mc_1_s_sdk_crypt_sdk=14cc0c37-43ba-a2c7; __security_mc_1_s_sdk_cert_key=69b62ff1-4b0a-a83e; MONITOR_WEB_ID=c57da653-e729-4937-a49d-6db89a37363b; is_staff_user=false; __security_mc_1_s_sdk_sign_data_key_sso=d6634e8b-46f0-8b05; __security_mc_1_s_sdk_sign_data_key_web_protect=6656f954-4446-a32d; download_guide=%223%2F20250525%2F0%22; EnhanceDownloadGuide=%220_0_1_1748184304_0_0%22; dy_swidth=2560; dy_sheight=1440; publish_badge_show_info=%220%2C0%2C0%2C1748618192417%22; strategyABtestKey=%221748653548.272%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.759%7D; douyin.com; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; sso_uid_tt=fff63e7b3089120b0c3701d85bf85472; sso_uid_tt_ss=fff63e7b3089120b0c3701d85bf85472; toutiao_sso_user=dccde6283a76508a6310aa180051b2dd; toutiao_sso_user_ss=dccde6283a76508a6310aa180051b2dd; sid_ucp_sso_v1=1.0.0-KGYyZDE5YTk0YjUxZTEzZGE3MTliYWI1OTM5MTYxNzM4YWNmM2UwYzQKCRDD7urBBhjvMRoCbGYiIGRjY2RlNjI4M2E3NjUwOGE2MzEwYWExODAwNTFiMmRk; ssid_ucp_sso_v1=1.0.0-KGYyZDE5YTk0YjUxZTEzZGE3MTliYWI1OTM5MTYxNzM4YWNmM2UwYzQKCRDD7urBBhjvMRoCbGYiIGRjY2RlNjI4M2E3NjUwOGE2MzEwYWExODAwNTFiMmRk; __ac_nonce=0683ab7430090b8f08cd0; __ac_signature=_02B4Z6wo00f01wFGWZgAAIDAnyL5C4krlHcBZl0AAKh1MkAXr1MKdWHMBeh6NUVFaK-uQrPpoqZxQ4TJclA4qq6dyl2LLSn10KG79SPOjazO5eumf5feg79f1FBPRK4mPlhcPc2jRtccQ.Tn29; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2560%2C%5C%22screen_height%5C%22%3A1440%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; biz_trace_id=dfcf38a3; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2736353d3632313d32333d313234272927676c715a75776a716a666a69273f2763646976602778; bit_env=zhYL6nDKT0jiVkqtlbKUh-hsy1VjcxCs68Hy-2hVXqp8v_cRgxQ_LwrnlPbyt0q1wo1XM3m5OB9WQtk-s905teouGOZj3MKX6I0IKIMp8OYjYTgoxZNqEbOLCYV7eBvXBo69hcz1g8QzL1yY7-pzPVJ9XPeNGvmkns5djNs0vZQylRUZdkYKD_-vNKwu40rVVzCQyL9TDOKKgm26fyIVUIUgqouwRucUuz4fI8zQvIbZgjIYmqA_vB_7hjSExk6MlfsKOfhiHzk-NhBOncrD0j6fAXKthY4QlLS3mNPzoH5dzL8t90TbNFYau-yDorfJ44JxBEaAoYVtRxnzCb-N1GFUZDgubba3iaEq8Mj4cm-1p4rlnQfza7zqKkALrwsF9uEoAtla2qOzUlueFa_-sAu4mfjFHl_C7IQgIWTSjsIqozwIJEAGayt9eGdLRw1lo91CQUiqo03BRIzekQnUBJhBYUewZy3wC7NRPCmyWlnoRbd-bjPqZJWSt44w3gUsumB3TV41SqicNiR4o5d5wyHcHe-SHd1d8ERm_dPv1po%3D; gulu_source_res=eyJwX2luIjoiMWUyYmM4OTQ1ZmExYWFmYjRiYmI4YTNjYmFiNDRkNjcwZmE2NjE5YWNiMjk0ZTIxYWY0NDJjNGRiYjU1ODAwNSJ9; passport_auth_mix_state=k6w8l8dpn45xzn4ba68f025zbt9lz8vba783q3ew8yx1rrif; passport_assist_user=ClPoUi9xevFLJR7zNckiWvLrRcY30Bn127Fwr8_eXWkYuwWUgfA-qEXpeIIAIwogoD9ME-P3pswnYPQL6ED-vj31OfPl7-YTYI7MBk3Tw4_pWE9STRpKCjy35xjoKonjS1-ASBOFiQqENioSq9jBradFf9esEUoi5PMoSo3SPDPdhkVrOeLxWJk-HtRDaAh87NmrhUkQ1evyDRiJr9ZUIAEiAQNrW2UI; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sid_guard=ce73c1f0c5977dfaba027af002a73bf4%7C1748678498%7C5184000%7CWed%2C+30-Jul-2025+08%3A01%3A38+GMT; uid_tt=b39da3d42329f3c634ee77190bfccb36469fbfe816ecfaac0efff6713f6c16c8; uid_tt_ss=b39da3d42329f3c634ee77190bfccb36469fbfe816ecfaac0efff6713f6c16c8; sid_tt=ce73c1f0c5977dfaba027af002a73bf4; sessionid=ce73c1f0c5977dfaba027af002a73bf4; sessionid_ss=ce73c1f0c5977dfaba027af002a73bf4; sid_ucp_v1=1.0.0-KGU3NDBhYWM0NzZmZjA5M2IzNzk2MWVjZTI4YWJlNjljMjRmNWI3NTcKIgi8iJSym4H8kGgQ4u7qwQYY7zEgDDD85IfBBjgHQPQHSAQaAmhsIiBjZTczYzFmMGM1OTc3ZGZhYmEwMjdhZjAwMmE3M2JmNA; ssid_ucp_v1=1.0.0-KGU3NDBhYWM0NzZmZjA5M2IzNzk2MWVjZTI4YWJlNjljMjRmNWI3NTcKIgi8iJSym4H8kGgQ4u7qwQYY7zEgDDD85IfBBjgHQPQHSAQaAmhsIiBjZTczYzFmMGM1OTc3ZGZhYmEwMjdhZjAwMmE3M2JmNA; login_time=1748678498635; _bd_ticket_crypt_cookie=915c5a961e9ea450b942aa187a3c06f4; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAyZkTH0g5o-M-mr26gp5tM_ScFLMaY3kPEgipGtKVFxTOSVAvCBKUrDQ4MCGOeQtY%2F1748707200000%2F0%2F1748678500166%2F0%22; __security_server_data_status=1; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQjFWYkxlUHkzcVZVOW54ampjTEtuSE9QZStmaVg3dWR3N2p5OU9FOGhqY1I5ZlFvd3puVmVsVTd5aSt2YXVjaGxMT3J1cXVqbUljMWVKVndJaWhISnM9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A1%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; home_can_add_dy_2_desktop=%221%22; odin_tt=3a4fec3d9baf3b91189545b6813ff7247983d0ebc25147a923f5bc337df6faa1e4c61284f96ecf91473eaa54bb1647da2d2ee7a44f49432ed86c05464b4abe58; WallpaperGuide=%7B%22showTime%22%3A1748662482322%2C%22closeTime%22%3A0%2C%22showCount%22%3A6%2C%22cursor1%22%3A146%2C%22cursor2%22%3A46%2C%22hoverTime%22%3A1746868266057%7D; xg_device_score=7.630007575365517; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAyZkTH0g5o-M-mr26gp5tM_ScFLMaY3kPEgipGtKVFxTOSVAvCBKUrDQ4MCGOeQtY%2F1748707200000%2F0%2F1748678516319%2F0%22; IsDouyinActive=false; passport_fe_beating_status=false",
    "Referer" : "https://www.douyin.com/",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive"
}

# HEADERS_TIKTOK = user_info_tiktok["headers"]


def get_tiktok_user_info():
    response_json = requests_common.get_json(user_info_tiktok["url"], headers=HEADERS_TIKTOK)

    if not response_json:
        return None

    tiktok_user_info = response_json["user"]

    nickname         = tiktok_user_info["nickname"]          # 昵称
    unique_id        = tiktok_user_info["unique_id"]         # 抖音号
    follower_count   = tiktok_user_info["follower_count"]    # 粉丝数
    following_count  = tiktok_user_info["following_count"]   # 关注数
    total_favorited  = tiktok_user_info["total_favorited"]   # 获赞数
    aweme_count      = tiktok_user_info["aweme_count"]       # 作品数
    favoriting_count = tiktok_user_info["favoriting_count"]  # 喜欢作品数
    signature        = tiktok_user_info["signature"]         # 签名
    ip_location      = tiktok_user_info["ip_location"]       # IP 地址

    user_info = {
        '昵称'       : nickname,
        '抖音号'     : unique_id,
        '粉丝数'     : follower_count,
        '关注数'     : following_count,
        '获赞数'     : total_favorited,
        '总评论数'   : 0,  # tiktok没有评论数这个字段，暂时设为0
        '作品数'     : aweme_count,
        '喜欢作品数'  : favoriting_count,
        '签名'       : signature,
        'IP属地'     : ip_location
    }
    print("get_tiktok_user_info: ", user_info)

    return user_info

def tiktok_data_process(data_from_internet, data_from_db, time):
    attachment = []
    message = ""

    if data_from_internet["昵称"] != data_from_db["昵称"]:
        message += "昵称从：{} 变为：{}\n".format(data_from_db['昵称'], data_from_internet["昵称"])
        print("tiktok_data_process: 昵称从：{} 变为：{}".format(data_from_db['昵称'], data_from_internet["昵称"]))
    
    if data_from_internet["抖音号"] != data_from_db["抖音号"]:
        message += "抖音号从：{} 变为：{}\n".format(data_from_db['抖音号'], data_from_internet["抖音号"])
        print("tiktok_data_process: 抖音号从：{} 变为：{}".format(data_from_db['抖音号'], data_from_internet["抖音号"]))

    if data_from_internet["粉丝数"] != data_from_db["粉丝数"]:
        message += "粉丝数从：{} 变为：{}\n".format(data_from_db['粉丝数'], data_from_internet["粉丝数"])
        print("tiktok_data_process: 粉丝数从：{} 变为：{}".format(data_from_db['粉丝数'], data_from_internet["粉丝数"]))

    if data_from_internet["关注数"] != data_from_db["关注数"]:
        message += "关注数从：{} 变为：{}\n".format(data_from_db['关注数'], data_from_internet["关注数"])
        print("tiktok_data_process: 关注数从：{} 变为：{}".format(data_from_db['关注数'], data_from_internet["关注数"]))

    if data_from_internet["作品数"] != data_from_db["作品数"]:
        message += "作品数从：{} 变为：{}\n".format(data_from_db['作品数'], data_from_internet["作品数"])
        print("tiktok_data_process: 作品数从：{} 变为：{}".format(data_from_db['作品数'], data_from_internet["作品数"]))

        video_list_file = user_info["File_path"] + user_info_tiktok["file_path_video_list"] + time.replace(" ", "-").replace(":", "-") + "_" + user_info_tiktok["file_tiktok_video_list"]
        tiktok_video_list, total_comment_number = tiktok_video.get_tiktok_video_info()
        UserInfo.save_user_info(tiktok_video_list, video_list_file)
        attachment.append(video_list_file)

        if data_from_internet["作品数"] > data_from_db["作品数"]:
            new_video_count = data_from_internet["作品数"] - data_from_db["作品数"]
            print("tiktok_data_process: tiktok作品数增加，获取最新的{}个作品信息".format(new_video_count))

            for num in range(new_video_count):
                # format_create_time = tiktok_video_list[num]['创建时间'].replace(" ", "-").replace(":", "-")
                format_create_time = format_time_string(tiktok_video_list[num]['创建时间'])
                format_video_title = safe_file_name(remove_emoji(tiktok_video_list[num]['标题']))

                if tiktok_video_list[num]["图片地址"]: # 图集视频，下载背景音乐
                    target_dir = user_info["File_path"] + user_info_tiktok["file_path_video"] + format_create_time + "_" + format_video_title + "\\"
                    os.mkdir(target_dir, exist_ok=True)
                    # 下载背景音乐
                    bgm_name = target_dir + format_video_title + ".mp3"
                    bgm_url = tiktok_video_list[num]['视频地址']
                    if tiktok_video.get_tiktok_video_file(bgm_name, bgm_url):
                        attachment.append(bgm_name)
                    else:
                        print("下载抖音背景音乐失败：", bgm_name)
                        message += "下载抖音背景音乐失败：{}\n".format(bgm_name)
                    # 下载图片
                    for i in range(tiktok_video_list[num]["图片数量"]):
                        image_name = user_info["File_path"] + user_info_tiktok["file_path_video"] + format_create_time + "_" + format_video_title + "_图片" + str(i+1) + ".jpg"
                        image_url = tiktok_video_list[num]['图片地址'][i]
                        print("下载抖音图集图片：", image_name)
                        if tiktok_video.get_tiktok_image_video_file(image_name, image_url):
                            attachment.append(image_name)
                        else:
                            print("下载抖音图集图片失败：", image_name)
                            message += "下载抖音图集图片失败：{}\n".format(image_name)

                if tiktok_video_list[num]["视频地址(图片中的视频)"]:
                    target_dir = user_info["File_path"] + user_info_tiktok["file_path_video"] + format_create_time + "_" + format_video_title + "\\"
                    os.mkdir(target_dir, exist_ok=True)
                    bgm_name = target_dir + format_video_title + ".mp3"
                    bgm_url = tiktok_video_list[num]['视频地址']
                    if tiktok_video.get_tiktok_video_file(bgm_name, bgm_url):
                        attachment.append(bgm_name)
                    else:
                        print("下载抖音背景音乐失败：", bgm_name)
                        message += "下载抖音背景音乐失败：{}\n".format(bgm_name)

                    for i in range(len(tiktok_video_list[num]["视频地址(图片中的视频)"])):
                        image_video_name = user_info["File_path"] + user_info_tiktok["file_path_video"] + format_create_time + "_" + format_video_title + "_图片中视频" + str(i+1) + ".mp4"
                        image_video_url = tiktok_video_list[num]['视频地址(图片中的视频)'][i]
                        print("下载抖音图集图片中的视频：", image_video_name)
                        if tiktok_video.get_tiktok_video_file(image_video_name, image_video_url):
                            attachment.append(image_video_name)
                        else:
                            print("下载抖音图集图片中的视频失败：", image_video_name)
                            message += "下载抖音图集图片中的视频失败：{}\n".format(image_video_name)

                video_name = user_info["File_path"] + user_info_tiktok["file_path_video"] + format_create_time + "_" + format_video_title + ".mp4"
                video_url = tiktok_video_list[num]['视频地址']
                print("tiktok_data_process:下载抖音视频：", video_name)
                if tiktok_video.get_tiktok_video_file(video_name, video_url):
                    attachment.append(video_name)
                else:
                    print("下载抖音视频失败：", video_name)
                    message += "下载抖音视频失败：{}\n".format(video_name)


                database.insert_tiktok_video((tiktok_video_list[num]["视频_id"], tiktok_video_list[num]["标题"], tiktok_video_list[num]["评论数"], tiktok_video_list[num]["点赞数"], tiktok_video_list[num]["分享数"], tiktok_video_list[num]["创建时间"], tiktok_video_list[num]["视频地址"], time))

    if data_from_internet["获赞数"] != data_from_db["获赞数"]:
        message += "获赞数从：{} 变为：{}\n".format(data_from_db['获赞数'], data_from_internet["获赞数"])
        print("tiktok_data_process: 获赞数从：{} 变为：{}".format(data_from_db['获赞数'], data_from_internet["获赞数"]))

        video_list_file = user_info["File_path"] + user_info_tiktok["file_path_video_list"] + time.replace(" ", "-").replace(":", "-") + "_" + user_info_tiktok["file_tiktok_video_list"]
        tiktok_video_list, total_comment_number = tiktok_video.get_tiktok_video_info()
        UserInfo.save_user_info(tiktok_video_list, video_list_file)
        attachment.append(video_list_file)
        for video in tiktok_video_list:
            video_id = video["视频_id"]
            video_info_dict = database.search_video_by_id(video_id)
            if video_info_dict:
                if video["点赞数"] != video_info_dict["点赞数"]:
                    message += "视频《{}》获赞数从：{} 变为：{}\n".format(video["标题"], video_info_dict["点赞数"], video["点赞数"])
                    database.insert_tiktok_video((video["视频_id"], video["标题"], video["评论数"], video["点赞数"], video["分享数"], video["创建时间"], video["视频地址"], time))
            else:
                # 没查到，视为新视频，可以直接插入或跳过
                database.insert_tiktok_video((video["视频_id"], video["标题"], video["评论数"], video["点赞数"], video["分享数"], video["创建时间"], video["视频地址"], time))

    if data_from_internet["总评论数"] != data_from_db["总评论数"]:
        message += "总评论数从：{} 变为：{}\n".format(data_from_db['总评论数'], data_from_internet["总评论数"])
        print("tiktok_data_process: 总评论数从：{} 变为：{}".format(data_from_db['总评论数'], data_from_internet["总评论数"]))

        video_list_file = user_info["File_path"] + user_info_tiktok["file_path_video_list"] + time.replace(" ", "-").replace(":", "-") + "_" + user_info_tiktok["file_tiktok_video_list"]
        tiktok_video_list, total_comment_number = tiktok_video.get_tiktok_video_info()
        UserInfo.save_user_info(tiktok_video_list, video_list_file)
        attachment.append(video_list_file)
        for video in tiktok_video_list:
            video_id = video["视频_id"]
            video_info_dict = database.search_video_by_id(video_id)
            if video_info_dict:
                if video["评论数"] != video_info_dict["评论数"]:
                    message += "视频《{}》评论数从：{} 变为：{}\n".format(video["标题"], video_info_dict["评论数"], video["评论数"])
                    database.insert_tiktok_video((video["视频_id"], video["标题"], video["评论数"], video["点赞数"], video["分享数"], video["创建时间"], video["视频地址"], time))
            else:
                # 没查到，视为新视频，可以直接插入或跳过
                database.insert_tiktok_video((video["视频_id"], video["标题"], video["评论数"], video["点赞数"], video["分享数"], video["创建时间"], video["视频地址"], time))

    if data_from_internet["喜欢作品数"] != data_from_db["喜欢作品数"]:
        message += "喜欢作品数从：{} 变为：{}\n".format(data_from_db['喜欢作品数'], data_from_internet["喜欢作品数"])
        print("tiktok_data_process: 喜欢作品数从：{} 变为：{}".format(data_from_db['喜欢作品数'], data_from_internet["喜欢作品数"]))

        like_video_list_file = user_info["File_path"] + user_info_tiktok["file_path_like_video_list"] + time.replace(" ", "-").replace(":", "-") + "_" + user_info_tiktok["file_tiktoklike_video_list"]
        tiktok_like_video_list = tiktok_like_video.get_like_list()
        UserInfo.save_user_info(tiktok_like_video_list, like_video_list_file)
        attachment.append(like_video_list_file)

    if data_from_internet["签名"] != data_from_db["签名"]:
        message += "签名从：{} 变为：{}\n".format(data_from_db['签名'], data_from_internet["签名"])
        print("tiktok_data_process: 签名从：{} 变为：{}".format(data_from_db['签名'], data_from_internet["签名"]))

    if data_from_internet["IP属地"] != data_from_db["IP属地"]:
        message += "IP属地从：{} 变为：{}\n".format(data_from_db['IP属地'], data_from_internet["IP属地"])
        print("tiktok_data_process: IP属地从：{} 变为：{}".format(data_from_db['IP属地'], data_from_internet["IP属地"]))

    return attachment, message


if __name__ == "__main__":
    user_info = get_tiktok_user_info()
    if user_info is None:
        print("未获取到用户信息")
    else:
        print("昵称:", user_info['昵称'])
        print("抖音号:", user_info['抖音号'])
        print("粉丝数:", user_info['粉丝数'])
        print("关注数:", user_info['关注数'])
        print("获赞数:", user_info['获赞数'])
        print("作品数:", user_info['作品数'])
        print("喜欢作品数:", user_info['喜欢作品数'])
        print("签名:", user_info['signature'])
