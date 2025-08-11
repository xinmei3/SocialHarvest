import pymysql
from pprint import pprint

class DataBase:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',  # 替换为你的数据库密码
        database='socialharvest',  # 替换为你的数据库名称
        charset='utf8mb4',
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
        sql = "INSERT INTO tiktok (昵称, 抖音号, IP属地, 粉丝数, 关注数, 获赞数, 作品数, 喜欢作品数, 签名, 时间) VALUES " + "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, data)
        self.connection.commit()  # 提交事务
    
    def insert_tiktok_video(self,data):
        sql = "INSERT INTO tiktok_video (视频_id, 标题, 评论数, 点赞数, 分享数, 创建时间, 视频地址) VALUES " + "(%s, %s, %s, %s, %s, %s, %s)"
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


if __name__ == "__main__":
        # 测试代码
    database = DataBase()  # 创建数据库连接实例
    # for item in database.search_common("select * from weibo_fans"):
    #     # tuple_in = (item[1], item[2], item[3][-10:])
    #     # print(item[1], item[2], item[3][-10:])
    #     command = "update weibo_fans set 微博号={} where 昵称 = '{}'".format(item[3][-10:], item[1])
    #     database.insert_common(command)
    # last_row, last_row_dict = database.search_tiktok()  # 获取最后一行数据
    # new_tuple = last_row[1:-1]
    # tuple_data = ('118', '46', '75', '66', '105', '81', 'example_content')  # 示例数据
    # database.insert_tiktok(tuple_data)  # 插入数据
    # database.insert_weibo(tuple_data)  # 插入数据
    last_row = ( "趣多多", "1180458703", "ip", "简介", 0, 16, 3, 0, "2025-06-24 22:45:00")  # 示例数据
    # database.insert_redbook(last_row)  # 插入数据
