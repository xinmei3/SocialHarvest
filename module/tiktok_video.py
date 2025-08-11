import requests
import json
from pprint import pprint
import common.database as database
import time


url_tiktok_work = "https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAHpssvF9y7F9lx-CAY8EKmdMnUTHkcNiT6EKXgX3iXh0&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&from_user_page=1&update_version_code=170400&pc_client_type=1&pc_libra_divert=Windows&support_h265=1&support_dash=1&cpu_core_num=12&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=2560&screen_height=1440&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=138.0.0.0&browser_online=true&engine_name=Blink&engine_version=138.0.0.0&os_name=Windows&os_version=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7421552512153306650&uifid=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4109a12adc1c3f7f26fa2b018a176235714142f663feeb21098188bf4013ef366563741f139de2078c9fe5c5a9e16e2b0c7d1fa1e6624a6be9bdcdcb270eaa660f92d81e5155ac350e039912a6ddffd03617a15174e734d88135a7a0ab96909e4333c0f699250832af144f04604d513c7b0a65888de3d30b6af5a78714ceff2af&msToken=lZtOpM-1NSR_JFDE5ADFVpeatrewsgRSIzgXk6l4GS-Zqj3-TBQZf-qXaRixT61s00BYAxJGYBTtj14Sy68FSMgfmSU0A4FwZ9ykFVUJ6Q74FK1CKqMjQnYMD2sCC8AoQMVIJ1fXhv21GDvTh-xFbPbD3JXoMLY1BZa7xz8beUebNCE-tWgboQ%3D%3D&a_bogus=mXsjD7WLDpRnadFtmCJ59tCUpZE%2FrPuyBFTObKPT9xYuTXzP5uPSwra4axz-4zK6uRpwk93HxDMAYExcKzUsZFrkomkfSBkyQ0IVngmo0qwXbUwkEqR2CwsqCJeT8QkETAKWJAUU1t5cIx%2F4DpawUQly7Api4YvpKrrfda4GY9ek6FG9FHqxuxGdxwzaQR95%2Fj%3D%3D&verifyFp=verify_mbs1oaak_WY03Wp9U_cfBg_4bEJ_Aei1_JI2G1u9OeiAN&fp=verify_mbs1oaak_WY03Wp9U_cfBg_4bEJ_Aei1_JI2G1u9OeiAN&x-secsdk-web-expire=1751725810093&x-secsdk-web-signature=259dfbba3b37e25649b355efc2bc533f"

headers_tiktok = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "Cookie": "UIFID_TEMP=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4109a12adc1c3f7f26fa2b018a1762357c2147030d2f37cbe71dd62a1f0efb64858788dc82aa484c683b2008a0f453159; hevc_supported=true; xgplayer_user_id=54110199621; fpk1=U2FsdGVkX1+39hdgmbDj6T8ShBekr3lUFPbfPTHsGrngj45fMR/tuRX2Xm26MogEWquBA4iMEZkhIQKSOR0XfA==; fpk2=d94a27a56e6a143d4c900b9014d6ba5d; bd_ticket_guard_client_web_domain=2; UIFID=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4109a12adc1c3f7f26fa2b018a176235714142f663feeb21098188bf4013ef366563741f139de2078c9fe5c5a9e16e2b0c7d1fa1e6624a6be9bdcdcb270eaa660f92d81e5155ac350e039912a6ddffd03617a15174e734d88135a7a0ab96909e4333c0f699250832af144f04604d513c7b0a65888de3d30b6af5a78714ceff2af; SelfTabRedDotControl=%5B%5D; store-region=cn-ln; store-region-src=uid; live_use_vvc=%22false%22; xgplayer_device_id=40266552717; is_dash_user=1; my_rd=2; d_ticket=3bfbb5672b9a2898b27d109744e1514afd824; SearchMultiColumnLandingAbVer=1; SEARCH_RESULT_LIST_TYPE=%22multi%22; MONITOR_WEB_ID=c57da653-e729-4937-a49d-6db89a37363b; is_staff_user=false; __security_server_data_status=1; enter_pc_once=1; s_v_web_id=verify_mbs1oaak_WY03Wp9U_cfBg_4bEJ_Aei1_JI2G1u9OeiAN; passport_csrf_token=dfb743f832fed4744c92e6623cfde289; passport_csrf_token_default=dfb743f832fed4744c92e6623cfde289; FOLLOW_RED_POINT_INFO=%221%22; publish_badge_show_info=%221%2C0%2C0%2C1751181454017%22; vdg_s=1; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.598%7D; __security_mc_1_s_sdk_crypt_sdk=2d543bca-4665-80d9; __security_mc_1_s_sdk_cert_key=83e8e4e5-477c-b8c3; strategyABtestKey=%221751697589.445%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA8XJVc6CJRliPpOG1olveDrkTl1vY283zVMz8nu7uOuMBBiOGHT2_r28AdEu4Ygvb%2F1751731200000%2F0%2F1751697594864%2F0%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A1%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __security_mc_1_s_sdk_sign_data_key_sso=53d2457d-430f-838e; passport_auth_status=b9ef960116749a197c6d4626e53b727b%2C; passport_auth_status_ss=b9ef960116749a197c6d4626e53b727b%2C; _bd_ticket_crypt_doamin=2; passport_assist_user=ClMOu1ed5MNni_AsI2aLPDUsKpeB--9Dosv1_8K8JgL5SUHBs78R5Bi2ehbzRAMyWeG7ybMGgvWDLcKfD_srAD8WpC92KXPzrFhlDsV5hnlHzP7VGBpKCjwAAAAAAAAAAAAATzIoDFr-VJI1MRDqXY55iD-mDoe2EfFgXAXySh25au3LL5j4DGj42pGheREPwO1BsZMQjPP1DRiJr9ZUIAEiAQPuEUQn; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sid_guard=be785bd8249c09bdc322b74a569c4a75%7C1751698163%7C5184000%7CWed%2C+03-Sep-2025+06%3A49%3A23+GMT; uid_tt=1e43bfdfb936b336654e350afb0fdc5455431b477e10159be43efd5b7df21f47; uid_tt_ss=1e43bfdfb936b336654e350afb0fdc5455431b477e10159be43efd5b7df21f47; sid_tt=be785bd8249c09bdc322b74a569c4a75; sessionid=be785bd8249c09bdc322b74a569c4a75; sessionid_ss=be785bd8249c09bdc322b74a569c4a75; session_tlb_tag=sttt%7C14%7Cvnhb2CScCb3DIrdKVpxKdf_________UbqmpWGOdP60OBcSjtrqQ3c1cKmMmUZkwhh6b2ytSnNA%3D; sid_ucp_v1=1.0.0-KGY1ODQ5YjQ3NjQwMGFmMWFhMTRiYjk0NzVhMzY0MzQxYWQ0ZTZkOGIKIgi8iJSym4H8kGgQ85WjwwYY7zEgDDD85IfBBjgFQPsHSAQaAmxmIiBiZTc4NWJkODI0OWMwOWJkYzMyMmI3NGE1NjljNGE3NQ; ssid_ucp_v1=1.0.0-KGY1ODQ5YjQ3NjQwMGFmMWFhMTRiYjk0NzVhMzY0MzQxYWQ0ZTZkOGIKIgi8iJSym4H8kGgQ85WjwwYY7zEgDDD85IfBBjgFQPsHSAQaAmxmIiBiZTc4NWJkODI0OWMwOWJkYzMyMmI3NGE1NjljNGE3NQ; login_time=1751698150232; __security_mc_1_s_sdk_sign_data_key_web_protect=44b487bb-467c-9f49; _bd_ticket_crypt_cookie=c8a8bc1a91580a275b137eacf37d1516; ttwid=1%7CC4e-ctAMuvxO7ja29TcPNSp5XZENpRGti1rHvoHUfuM%7C1751698165%7C1ca45548102faf86b8dcd9dfbd58f728330e6bd5012c06d8dbeb3c0d52350672; WallpaperGuide=%7B%22showTime%22%3A1751698254932%2C%22closeTime%22%3A0%2C%22showCount%22%3A4%2C%22cursor1%22%3A59%2C%22cursor2%22%3A18%7D; __ac_nonce=06869358f00f77f919603; __ac_signature=_02B4Z6wo00f01yYG3UQAAIDAuGJ91N9dc28mJtnAAKHyGuavt0GwPdayjCit4CpIMy1F2mQjB98EzqU2S-tfQcOqDlWXAmDmjJfZFge0lg3aReYFhTKNm19KQ5NprhaLkqiRfGSUVnl9gc8z5f; dy_swidth=2560; dy_sheight=1440; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2560%2C%5C%22screen_height%5C%22%3A1440%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAyZkTH0g5o-M-mr26gp5tM_ScFLMaY3kPEgipGtKVFxTOSVAvCBKUrDQ4MCGOeQtY%2F1751731200000%2F0%2F0%2F1751726645303%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQjFWYkxlUHkzcVZVOW54ampjTEtuSE9QZStmaVg3dWR3N2p5OU9FOGhqY1I5ZlFvd3puVmVsVTd5aSt2YXVjaGxMT3J1cXVqbUljMWVKVndJaWhISnM9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; odin_tt=82380b5b99a8f724064aed8d812cf69a189531d231d611ef85b3949f6c40ca2431ccbc89f82021da8f940cdac3f15e8c37893ee9467e86885d0d388e688f9fed; download_guide=%221%2F20250705%2F0%22; passport_fe_beating_status=false; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22",
    "Referer" : "https://www.douyin.com/",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive"
}


def get_tiktok_video_info(filename):
    response = requests.get(url_tiktok_work, headers=headers_tiktok)
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return []

    try:
        response_json = json.loads(response.text)
    except json.JSONDecodeError:
        print("Error decoding JSON response")
        return []

    video_list = response_json.get("aweme_list", [])

    video_list_final = []
    for work in video_list:
        video_id = work.get('aweme_id')
        video_title = work.get('desc')
        video_comment_count = work.get('statistics', {}).get('comment_count', 0)
        video_like_count = work.get('statistics', {}).get('digg_count', 0)
        video_share_count = work.get('statistics', {}).get('share_count', 0)
        video_create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(work.get('create_time')))
        video_url = work.get('video', {}).get('play_addr', {}).get('url_list', [])[0]

        video_info = {
            "视频_id": video_id,
            "标题": video_title,
            "评论数": video_comment_count,
            "点赞数": video_like_count,
            "分享数": video_share_count,
            "创建时间": video_create_time,
            "视频地址": video_url
        }
        video_list_final.append(video_info)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(video_list_final, f, ensure_ascii=False, indent=4)
    return video_list_final


if __name__ == "__main__":
    filename = "C:\\Users\\张耀文\\Documents\\requesets_lib\\user_info\\tiktok_video_list.txt"
    video_info = get_tiktok_video_info(filename)

    for video in video_info:
        pprint(video)
        print("\n")


    Database = database.database_xiang()
    # print("TikTok Work List:")
    # pprint.pprint(video_list)

    for video in video_info:
        if Database.check_video_exists(video["视频_id"]):
            print(f"Video {video['视频_id']} already exists in the database.")
        else:
            # Insert the video information into the database
            Database.insert_tiktok_video((
                video["视频_id"],
                video["标题"],
                video["评论数"],
                video["点赞数"],
                video["分享数"],
                video["创建时间"],
                video["视频地址"]
            ))
            print(f"Inserted video {video['视频_id']} into the database.")
