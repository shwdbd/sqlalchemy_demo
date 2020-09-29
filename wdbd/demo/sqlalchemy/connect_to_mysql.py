#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   connect_to_mysql.py
@Time    :   2020/09/29 10:40:12
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Mysql数据库（阿里云在线库）连接
'''
from sqlalchemy import create_engine


# 数据库连接参数
server_url = "rm-8vbqc3l9ultgf5u37qo.mysql.zhangbei.rds.aliyuncs.com"
user_id = "fdata"
user_password = "fd_61875707"
server_port = "3306"
db_name = "sqlalchemy_demo"
engine_echo = False
engine_max_overflow = 0     # 超过连接池大小外最多创建的连接
engine_pool_size = 5        # 连接池大小
engine_pool_timeout = 30    # 池中没有线程最多等待的时间，否则报错
engine_pool_recycle = -1    # 多久之后对线程池中的线程进行一次连接的回收（重置）


# 取得数据库连接对象
def get_engine():
    try:
        # 数据库连接字符串
        conn_str = 'mysql+mysqlconnector://{user_id}:{user_password}@{server_url}:{server_port}/{db_name}'.format(
            server_url=server_url,
            user_id=user_id,
            user_password=user_password,
            server_port=server_port,
            db_name=db_name)

        engine = create_engine(conn_str, echo=engine_echo,
                               max_overflow=engine_max_overflow,
                               pool_size=engine_pool_size,
                               pool_timeout=engine_pool_timeout,
                               pool_recycle=engine_pool_recycle
                               )
        return engine
    except Exception:
        print("连接数据库（建立引擎）失败！")
        return None


def get_connection():
    """取得数据库连接对象

    Returns:
        [type]: [description]
    """
    return get_engine().connect()


if __name__ == "__main__":
    conn = get_connection()
    print(conn)
