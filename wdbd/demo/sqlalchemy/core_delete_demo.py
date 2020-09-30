#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   core_delete_demo.py
@Time    :   2020/09/30 09:01:27
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Core模式下的记录删除

代码清单：
- record_delete : 单表的条件删除

'''
from wdbd.demo.sqlalchemy.db_persistence import (cookies)
from sqlalchemy import delete, select
import wdbd.demo.sqlalchemy.connect_to_mysql as con


# TODO 要尝试 truncate 模式的删除
# TODO 有外键的情况下的级联删除


def data_setup():
    """准备试验数据

    往数据库中插入两条数据

    """
    print("测试用数据库准备")
    ins = cookies.insert()
    record_data = [
        {
            'cookie_name': 'D1',
            'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
            'cookie_sku': 'PB01', 'quantity': '24', 'unit_cost': '0.25'},
    ]
    # 执行插入
    conn = con.get_connection()
    result = conn.execute(ins, record_data)
    if result:
        conn.close()
        print("插入2条新记录！")
    print("数据准备完成")


def record_delete():
    """记录删除
    """
    conn = con.get_connection()

    # 查看删除前情况
    print("删除前:")
    print_all(conn)

    # 执行删除
    d = delete(cookies).where(cookies.c.cookie_name == "D1")
    print("执行的SQL是: \n{0}".format(str(d)))
    result = conn.execute(d)
    print("删除的记录数量 = {0}".format(result.rowcount))

    print("删除后:")
    print_all(conn)

    conn.close()


# 打印所有的记录
def print_all(conn):
    """打印所有的记录
    """
    s = select([cookies.c.cookie_name, cookies.c.quantity])
    for idx, record in enumerate(conn.execute(s)):
        print("{0} : {1} - {2}".format(idx+1, record.cookie_name, record.quantity))


if __name__ == "__main__":
    data_setup()

    record_delete()
