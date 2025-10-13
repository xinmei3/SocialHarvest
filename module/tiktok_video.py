import time
from pprint import pprint
import requesets_lib.common.database as database
import requesets_lib.common.requests_common as requests_common
import requesets_lib.common.user_info_manager as user_info_manager


user_info = user_info_manager.UserInfo.user_info_loader()

tiktok_user_info = user_info["tiktok"]
url_tiktok_work = tiktok_user_info["url_video_work"]
headers_tiktok = tiktok_user_info["headers_video_work"]

def get_tiktok_video_info():

    response_json = requests_common.RequestsCommon().get_json(url_tiktok_work, headers_tiktok)

    if not response_json or "aweme_list" not in response_json:
        print("get_tiktok_video_info: Error: 'aweme_list' not found in the response")
        return None

    video_list = response_json.get("aweme_list", [])

    video_list_final = []
    video_comment_count_total = 0
    for video in video_list:
        video_id = video.get('aweme_id')
        video_title = video.get('desc')
        video_comment_count = video.get('statistics', {}).get('comment_count', 0)
        video_like_count = video.get('statistics', {}).get('digg_count', 0)
        video_share_count = video.get('statistics', {}).get('share_count', 0)
        video_create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(video.get('create_time')))
        video_url = video.get('video', {}).get('play_addr', {}).get('url_list', [])[0]
        images = video.get('images')

        if images:
            image_number, image_url_list, video_url_list = process_tiktok_image(images)

        video_comment_count_total += video_comment_count

        # pprint(image_url_list)

        video_info = {
            "视频_id": video_id,
            "标题": video_title,
            "评论数": video_comment_count,
            "点赞数": video_like_count,
            "分享数": video_share_count,
            "创建时间": video_create_time,
            "视频地址": video_url,
            "图片数量": image_number,
            "图片地址": image_url_list,
            "视频地址(图片中的视频)": video_url_list
        }
        video_list_final.append(video_info)

    print("总评论数：", video_comment_count_total)
    return video_list_final, video_comment_count_total


def get_tiktok_video_file(title, url):
    video = requests_common.RequestsCommon().get_video(url, title, tiktok_user_info["headers_video_work"])

    if video is None:
        print(f"get_tiktok_video_file: 获取视频失败: {title}")
        return None
    else:
        print(f"get_tiktok_video_file: 获取视频成功: {title}")
        return True


def process_tiktok_image(images):
    image_number = 0
    image_url_list = []
    video_url_list = []

    if not images:  # image是空列表或None
        print("No images found.")
        return image_number, image_url_list, video_url_list

    for image in images:
        if "video" in image:  # 图片列表中包含视频
            video_url = image['video']['play_addr']['url_list'][0]
            video_url_list.append(video_url)

        img_url = image.get('download_url_list', [])[0]
        image_number += 1
        image_url_list.append(img_url)

        # print(f"获取 image {image_number}的链接: \n{img_url}")

    return image_number, image_url_list, video_url_list

def get_tiktok_image_video_file(image_name, image_url):
    image = requests_common.RequestsCommon().get_image(image_url, image_name, tiktok_user_info["headers_video_work"])

    if image is None:
        print(f"get_tiktok_image_video_file: 获取图片失败: {image_name}")
        return None
    else:
        print(f"get_tiktok_image_video_file:获取图片成功: {image_name}")
        return True

if __name__ == "__main__":
    filename = "C:\\Users\\张耀文\\Documents\\requesets_lib\\user_info\\tiktok_video_list.txt"
    video_info = get_tiktok_video_info(filename)

    for video in video_info:
        pprint(video)
        print("\n")

    Database = database.database_xiang()
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
