#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   core_join_demo.py
@Time    :   2020/09/30 09:38:01
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Core模式下的多表关联查询
'''
from wdbd.demo.sqlalchemy.db_persistence import (users, orders)
from sqlalchemy import select, update, insert
import wdbd.demo.sqlalchemy.connect_to_mysql as con


def data_setup():
    """准备试验数据

    模拟数据：
    - 1条users信息
    - 2条orders信息

    """
    print("测试用数据库准备")
    conn = con.get_connection()

    # 插入users信息
    ins = insert(users).values(user_id=1, username="Wang", email_address="", phone="", password="")
    conn.execute(ins)

    # 插入orders信息
    ins = insert(orders).values(order_id=1, user_id="1")
    conn.execute(ins)
    ins = insert(orders).values(order_id=2, user_id="1")
    conn.execute(ins)

    conn.close()
    print("数据准备完成")


# 多表关联查询
def table_join():
    """多表关联查询

    查询order_id=2的用户名称
    """
    conn = con.get_connection()

    columns = [orders.c.order_id, orders.c.user_id, users.c.user_id, users.c.username]
    the_orders = select(columns)
    the_orders = the_orders.select_from(orders.join(users)).where(orders.c.order_id == 2)
    for idx, record in enumerate(conn.execute(the_orders)):
        print("{0} : {1} - {2}".format(idx+1, record.order_id, record.username))
        # 1 : 2 - Wang

    conn.close()


if __name__ == "__main__":
    # data_setup()

    table_join()
