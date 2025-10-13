import random
import time
import pprint
import requesets_lib.module.tiktok_video as tiktok_video
import requesets_lib.module.red as red
import requesets_lib.module.weibo as weibo
import requesets_lib.module.tiktok as tiktok
import requesets_lib.common.Email as Email
from requesets_lib.common.requests_common import RequestsCommon
from requesets_lib.common.database import DataBase
from requesets_lib.common.user_info_manager import UserInfo
# from requesets_lib.module.tiktok_data_process.TikTokDataProcessor import check_tiktok_work_data


user_info = UserInfo.user_info_loader()

FILE_PATH = user_info["File_path"]
PATH_TIKTOK_VIDEO = user_info["tiktok"]["file_path_video"]
PATH_TIKTOK_LIKE_LIST = user_info["tiktok"]["file_path_like_video_list"]
PATH_TIKTOK_VIDEO_LIST = user_info["tiktok"]["file_path_video_list"]
FILE_TIKTOK_USER_INFO = user_info["tiktok"]["file_tiktok_user_info"]

WEIBO_USER_ID = user_info["weibo"]["user_id"]
FILE_WEIBO_USER_INFO = user_info["weibo"]["file_weibo_user_info"]
FILE_TIKTOK_LIKE_LIST = user_info["tiktok"]["file_tiktoklike_video_list"]
FILE_TIKTOK_VIDEO_LIST = user_info["tiktok"]["file_tiktok_video_list"]

FILE_RED_USER_INFO = 'red_user_info.txt'

database = DataBase()
weibo_info = weibo.getWeiboInfo()
requests_common = RequestsCommon()

def time_stamp():
    time_stamp = time.time()
    local_time = time.localtime(time_stamp)
    str_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
    return str_time


def file_writer(filename, data):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(data + '\n')


def check_weibo():
    str_time = time_stamp()
    file_name = FILE_PATH + FILE_WEIBO_USER_INFO

    weibo_user_info = weibo_info.get_weibo_user_info()
    user_info_db, user_info_db_dict = database.search_weibo()

    if weibo_user_info is None:
        print("微博用户信息获取失败，跳过写入")
        Email.send_email(subject="微博用户信息获取失败", content="微博用户信息获取失败，请检查网络连接或API是否正常。")
        return

    user_info = "时间：{}\t昵称：{}\t简介：{}\t转评赞：{}\t累计评论量：{}\t累计获赞：{}\t粉丝数：{}\t关注数：{}\t微博数：{}".format(
        str_time,
        weibo_user_info["昵称"],
        weibo_user_info["简介"],
        weibo_user_info["转评赞"],
        weibo_user_info["累计评论量"],
        weibo_user_info["累计获赞"],
        weibo_user_info["粉丝数"],
        weibo_user_info["关注数"],
        weibo_user_info["微博数"]
    )
    print("weibo用户信息： ", user_info)
    user_info_tuple = (
        weibo_user_info["昵称"], 
        weibo_user_info["简介"], 
        weibo_user_info["转评赞"], 
        weibo_user_info["累计评论量"], 
        weibo_user_info["累计获赞"], 
        weibo_user_info["粉丝数"], 
        weibo_user_info["关注数"], 
        weibo_user_info["微博数"], 
        str_time
    )

    if user_info_tuple[:-1] == user_info_db[1:-1]:
        print("check_weibo: weibo数据未变化，跳过写入\n")
        file_writer(file_name, user_info)
    else:
        email_message = ""
        email_message += user_info + "\n\n"

        if weibo_user_info["关注数"] != user_info_db_dict["关注数"]:  # 如果关注数有变化, 获取关注用户信息
            email_message += "\n关注数从 {} 变为 {} \n".format(user_info_db_dict["关注数"], weibo_user_info["关注数"])
            weibo_follower_info, weibo_follower_count = weibo_info.get_follower_data(WEIBO_USER_ID)
            follower_info = []
            for follower in weibo_follower_info:
                follower_info.append("昵称：" + follower["screen_name"] + "\t主页链接： https://weibo.com/u/" + str(follower["id"]))
            
            email_message += "\n关注用户信息：\n" + "\n".join(follower_info)

        elif weibo_user_info["粉丝数"] != user_info_db_dict["粉丝数"]:  # 如果粉丝数有变化, 获取粉丝信息
            email_message += "\n粉丝数从 {} 变为 {} \n".format(user_info_db_dict["粉丝数"], weibo_user_info["粉丝数"])
            weibo_follower_info, weibo_fans_count = weibo_info.get_fans_data(WEIBO_USER_ID)
            fans_info = []
            for fan in weibo_follower_info:
                fans_info.append("昵称：" + fan["screen_name"] + "\t主页链接： https://weibo.com/u/" + str(fan["id"]))
            email_message += "\n粉丝用户信息：\n" + "\n".join(fans_info)

        Email.send_email(subject="微博用户信息更新", content=email_message)
        file_writer(file_name, "数据改变    " + user_info)
        print("check_weibo: weibo数据已更新，写入数据库", user_info_tuple)
        database.insert_weibo(user_info_tuple)


def check_tiktok():
    str_time = time_stamp()
    file_name = FILE_PATH + FILE_TIKTOK_USER_INFO

    tiktok_user_info = tiktok.get_tiktok_user_info()
    tiktok_video_info, tiktok_comment_number = tiktok_video.get_tiktok_video_info()
    user_info_db, user_info_db_dict = database.search_tiktok()

    if tiktok_user_info is None:
        print("check_tiktok: TikTok用户信息获取失败，跳过写入")
        Email.send_email(subject="TikTok用户信息获取失败", content="TikTok用户信息获取失败，请检查网络连接或API是否正常。")
        return

    tiktok_user_info["总评论数"] = tiktok_comment_number

    user_info = "时间：{}\t昵称：{}\t抖音号：{}\t{}\t粉丝数：{}\t关注数：{}\t获赞数：{}\t作品数：{}\t总评论数：{}\t喜欢作品数：{}\t签名：{}".format(
        str_time,
        tiktok_user_info["昵称"],
        tiktok_user_info["抖音号"],
        tiktok_user_info["IP属地"],
        tiktok_user_info["粉丝数"],
        tiktok_user_info["关注数"],
        tiktok_user_info["获赞数"],
        tiktok_user_info["作品数"],
        tiktok_user_info["总评论数"],
        tiktok_user_info["喜欢作品数"],
        tiktok_user_info["签名"]
    )
    print("TikTok用户信息： ", user_info)
    user_info_tuple = (
        tiktok_user_info["昵称"], 
        tiktok_user_info["抖音号"], 
        tiktok_user_info["IP属地"], 
        tiktok_user_info["粉丝数"],
        tiktok_user_info["关注数"], 
        tiktok_user_info["获赞数"], 
        tiktok_user_info["作品数"], 
        tiktok_user_info["总评论数"], 
        tiktok_user_info["喜欢作品数"], 
        tiktok_user_info["签名"], 
        str_time
    )

    if user_info_tuple[:-1] == user_info_db[1:-1]:
        print("check_tiktok: TikTok数据未变化，跳过写入\n")
        file_writer(file_name, user_info)
    else:
        email_message = ""
        email_message += user_info + "\n\n"

        attachment_list, message = tiktok.tiktok_data_process(tiktok_user_info, user_info_db_dict, str_time)
        email_message += message

        if attachment_list is None:
            Email.send_email(subject="TikTok用户信息更新", content=email_message)
        else:
            Email.send_email(subject="TikTok用户信息更新", content=email_message, attachment_paths=attachment_list)

        file_writer(file_name, "数据改变    " + user_info)
        print("check_tiktok: tiktok数据已更新，写入数据库", user_info_tuple)
        database.insert_tiktok(user_info_tuple)


def check_red():
    str_time = time_stamp()
    file_name = FILE_PATH + FILE_RED_USER_INFO

    red_user_info = red.get_red_user_info()
    user_info_db, user_info_db_dict = database.search_redbook()

    if red_user_info is None:
        print("check_red: 小红书用户信息获取失败，跳过写入")
        Email.send_email(subject="小红书用户信息获取失败", content="小红书用户信息获取失败，请检查网络连接或API是否正常。")
        return
    else:
        red_user_info_request = (
            red_user_info["小红书号"], 
            red_user_info["昵称"], 
            red_user_info["IP属地"], 
            red_user_info["简介"], 
            red_user_info["作品数"],
            red_user_info["关注数"], 
            red_user_info["粉丝数"], 
            red_user_info["获赞与收藏"], 
            str_time
        )
        
        red_user_info = "时间：{}\t昵称：{}\t小红书号：{}\t位置：{}\t签名：{}\t笔记数：{}\t关注数：{}\t粉丝数：{}\t互动量：{}".format(
                str_time,
                red_user_info["昵称"],
                red_user_info["小红书号"],
                red_user_info["IP属地"],
                red_user_info["简介"],
                red_user_info["作品数"],
                red_user_info["关注数"],
                red_user_info["粉丝数"],
                red_user_info["获赞与收藏"]
            )
        print("小红书用户信息：", red_user_info)
        if user_info_db[1:-1] == red_user_info_request[:-1]:
            print("check_red: 小红书数据未变化，跳过写入")
            file_writer(file_name, red_user_info)
        else:
            print(user_info_db[1:-1])
            print(red_user_info_request[:-1])
            Email.send_email(subject="小红书用户信息更新", content=red_user_info)
            file_writer(file_name, "数据改变    " + red_user_info)
            database.insert_redbook(red_user_info_request)


if __name__ == "__main__":
    check_tiktok()
    check_weibo()

    get_red_flag = 0
    flag = user_info["red"]["get_red_info"]
    if flag == "0":
        get_red_flag = random.randint(0, 1)  # 随机生成0或1
    elif flag == "1":
        get_red_flag = 1

    if get_red_flag:
        print("red_flag 为{}，获取小红书用户信息".format(get_red_flag))
        check_red()
    else:
        print("red_flag 为{}，跳过小红书用户信息获取".format(get_red_flag))
