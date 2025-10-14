import pymysql
from pprint import pprint
from requesets_lib.common.user_info_manager import UserInfo

user_info_database = UserInfo.user_info_loader()["database"]

class DataBase:
    connection = pymysql.connect(
        host      = user_info_database["host"],
        port      = user_info_database["port"],
        user      = user_info_database["user"],
        password  = user_info_database["password"],
        database  = user_info_database["database"],
        charset   = user_info_database["charset"]
    )
    cursor = connection.cursor()
    def __init__(self):
        self.cursor = DataBase.cursor
        self.connection = DataBase.connection

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def __return_diction(self, results):
        if results is None:
            return None
        else:
            columns = [col[0] for col in self.cursor.description]
            results = dict(zip(columns, results))
            return results

    def search_common(self, command):
        sql = command
        self.cursor.execute(sql)
        results = self.cursor.fetchall()  # 获取最后一行数据

        return results
    
    def insert_common(self, command):
        sql = command
        self.cursor.execute(sql)
        self.connection.commit()

    def search_tiktok(self):
        sql = "SELECT * FROM tiktok order by id desc limit 1"  # 替换为你的表名
        self.cursor.execute(sql)
        results = self.cursor.fetchone()  # 获取最后一行数据

        results_dict = DataBase.__return_diction(self, results)  # 将结果转换为字典形式

        return results, results_dict

    def search_weibo(self):
        sql = "SELECT * FROM weibo order by id desc limit 1"  # 替换为你的表名
        self.cursor.execute(sql)
        results = self.cursor.fetchone()  # 获取最后一行数据

        results_dict = DataBase.__return_diction(self, results)  # 将结果转换为字典形式

        return results, results_dict 

    def search_redbook(self):
        sql = "SELECT * FROM red order by id desc limit 1"
        self.cursor.execute(sql)
        results = self.cursor.fetchone()  # 获取最后一行数据

        results_dict = DataBase.__return_diction(self, results)  # 将结果转换为字典形式

        return results, results_dict 

    def insert_tiktok(self, data):
        sql = "INSERT INTO tiktok (昵称, 抖音号, IP属地, 粉丝数, 关注数, 获赞数, 作品数, 总评论数, 喜欢作品数, 签名, 时间) VALUES " + "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, data)
        self.connection.commit()  # 提交事务
    
    def insert_tiktok_video(self,data):
        sql = "INSERT INTO tiktok_video (视频_id, 标题, 评论数, 点赞数, 分享数, 创建时间, 视频地址, 时间戳) VALUES " + "(%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, data)
        self.connection.commit()

    def insert_weibo(self, data):
        sql = "INSERT INTO weibo (昵称, 简介, 转评赞, 累计评论量, 累计获赞, 粉丝数, 关注数, 微博数, 时间) VALUES " + "(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, data)
        self.connection.commit() # 提交事务

    def insert_redbook(self, data):
        sql = "INSERT INTO red (小红书号, 昵称, IP地址, 简介, 作品数, 关注数, 粉丝数, 喜欢作品数, 时间) VALUES " + "(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, data)
        self.connection.commit()

    def check_video_exists(self, video_id):
        sql = "SELECT COUNT(*) FROM tiktok_video WHERE 视频_id = %s"
        self.cursor.execute(sql, (video_id,))
        count = self.cursor.fetchone()[0]
        return count > 0
    
    def search_video_by_id(self, video_id):
        sql = "SELECT * FROM tiktok_video WHERE 视频_id = %s order by id desc LIMIT 1"
        self.cursor.execute(sql, (video_id,))
        result = self.cursor.fetchone()
        results_dict = DataBase.__return_diction(self, result)  # 将结果转换为字典形式
        return results_dict


if __name__ == "__main__":
        # 测试代码
    database = DataBase()  # 创建数据库连接实例
    pprint(database.search_common("select video_id from tiktok"))
    # database.insert_weibo(tuple_data)  # 插入数据
    last_row = ( "趣多多", "1180458703", "ip", "简介", 0, 16, 3, 0, "2025-06-24 22:45:00")  # 示例数据
    # database.insert_redbook(last_row)  # 插入数据
